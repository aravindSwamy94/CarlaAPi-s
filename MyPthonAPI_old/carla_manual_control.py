#!/usr/bin/env python3

# Copyright (c) 2017 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB), and the INTEL Visual Computing Lab.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

# Keyboard controlling for carla. Please refer to carla_use_example for a
# simpler and more documented example.

"""
Welcome to CARLA manual control.
Use ARROWS or WASD keys for control.
    W            : throttle
    S            : brake
    AD           : steer
    Q            : toggle reverse
    Space        : hand-brake
    R            : restart level
STARTING in a moment...
"""

from __future__ import print_function

import argparse
import logging
import sys
import time

import numpy as np

import matplotlib.pyplot as plt

import pygame
from pygame.locals import *

from carla import CARLA
from carla import Control


def join_classes(labels_image):
    classes_join = {
        0: [0, 0, 0],
        1: [64, 64, 64],
        2: [96, 96, 96],
        3: [255, 255, 255],
        4: [255, 0, 0],
        5: [128, 128, 128],
        6: [196, 196, 196],
        7: [128, 0, 128],
        8: [255, 0, 255],
        9: [0, 255, 0],
        10: [0, 0, 255],
        11: [32, 32, 32],
        12: [220, 220, 0]
    }
    compressed_labels_image = np.zeros((labels_image.shape[0], labels_image.shape[1], 3))
    for (key, value) in classes_join.items():
        compressed_labels_image[np.where(labels_image == key)] = value
    return compressed_labels_image


def grayscale_colormap(img, colormap):
    """Make colormaps from grayscale."""
    cmap = plt.get_cmap(colormap)
    rgba_img = cmap(img)
    rgb_img = np.delete(rgba_img, 3, 2)
    return rgb_img


def convert_depth(depth):
    """Convert depth to human readable format."""
    depth = depth.astype(np.float32)
    gray_depth = ((depth[:, :, 0] +                 # Red
                   depth[:, :, 1] * 256.0 +         # Green
                   depth[:, :, 2] * 256.0 * 256.0)) # Blue
    gray_depth /= (256.0 * 256.0 * 256.0 - 1)
    color_depth = grayscale_colormap(gray_depth, 'jet') * 255
    return color_depth

if sys.version_info >= (3, 3):

    import shutil

    def get_terminal_width():
        return shutil.get_terminal_size((80, 20)).columns

else:

    def get_terminal_width():
        return 120


class App(object):
    def __init__(
            self,
            port=2000,
            host='127.0.0.1',
            config='./CarlaSettings.ini',
            resolution=(2400, 600),
            verbose=True):
        self._running = True
        self._display_surf = None
        self.port = port
        self.host = host
        self.config = config
        self.verbose = verbose
        self.resolution = resolution
        self.size = self.weight, self.height = resolution
        self.reverse_gear = False

    def on_init(self):
        pygame.init()
        print(__doc__)
        time.sleep(3)
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        logging.debug('Started the PyGame Library')
        self._running = True
        self.step = 0
        self.prev_step = 0
        self.prev_time = time.time()

        self.carla = CARLA(self.host, self.port)

        positions = self.carla.loadConfigurationFile(self.config)
        self.num_pos = len(positions)
        print("Staring Episode on Position ", self.num_pos)
        self.carla.newEpisode(np.random.randint(self.num_pos))
        self.prev_restart_time = time.time()
        # Adding Joystick controls here
        self.js = pygame.joystick.Joystick(0)
        self.js.init()
        axis = self.js.get_axis(1)
        jsInit = self.js.get_init()
        jsId = self.js.get_id()
        print("Joystick ID: %d Init status: %s Axis(1): %d" % (jsId, jsInit, axis))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.step += 1
        keys = pygame.key.get_pressed()

        numAxes = self.js.get_numaxes()
        jsInputs = [ float(self.js.get_axis(i)) for i in range(numAxes)]

        print('Js inputs [%s]' % ', '.join(map(str, jsInputs)))
        restart = False

        control = Control()

        pressed_keys = []
        if keys[K_LEFT] or keys[K_a]:
            control.steer = -1.0
            pressed_keys.append('left')
        if keys[K_RIGHT] or keys[K_d]:
            control.steer = 1.0
            pressed_keys.append('right')
        if keys[K_UP] or keys[K_w]:
            control.throttle = 1.0
            pressed_keys.append('reverse' if self.reverse_gear else 'forward')
        if keys[K_DOWN] or keys[K_s]:
            control.brake = 1.0
            pressed_keys.append('brake')
        if keys[K_SPACE]:
            control.hand_brake = True
            pressed_keys.append('hand-brake')
        if keys[K_q]:
            self.reverse_gear = not self.reverse_gear
            pressed_keys.append('toggle reverse')
        if keys[K_r]:
            pressed_keys.append('reset')
            if time.time() - self.prev_restart_time > 2.:
                self.prev_restart_time = time.time()
                restart = True

        if time.time() - self.prev_restart_time < 2.:
            control.throttle = 0.0
            control.steer = 0.0

        control.steer = jsInputs[0]

        brakeCmd = (((jsInputs[1] - (-1)) * (1.0 - 0)) / (1.0 - (-1.0))) + 0
        throttleCmd = (((jsInputs[2] - (-1)) * (1.0 - 0)) / (1.0 - (-1.0))) + 0

        control.brake = brakeCmd
        control.throttle = throttleCmd

        control.reverse = self.reverse_gear
        self.carla.sendCommand(control)

        measurements = self.carla.getMeasurements()
        pack = measurements['PlayerMeasurements']
        self.img_vec = measurements['BGRA']
        self.depth_vec = measurements['Depth']
        self.labels_vec = measurements['Labels']

        if time.time() - self.prev_time > 1.:
            message = 'Step {step} ({fps:.1f} FPS): '
            message += '{speed:.2f} km/h, '
            message += '{other_lane:.0f}% other lane, {offroad:.0f}% off-road'
            message += ': pressed [%s]' % ', '.join(pressed_keys)

            message = message.format(
                step=self.step,
                fps=float(self.step - self.prev_step) / (time.time() - self.prev_time),
                speed=pack.forward_speed,
                other_lane=100 * pack.intersection_otherlane,
                offroad=100 * pack.intersection_offroad)

            empty_space = max(0, get_terminal_width() - len(message))
            sys.stdout.write('\r' + message + empty_space * ' ')
            sys.stdout.flush()

            self.prev_step = self.step
            self.prev_time = time.time()

        if restart:
            print('\n *** RESTART *** \n')
            player_pos = np.random.randint(self.num_pos)
            print('  Player pos %d \n' % (player_pos))
            self.carla.newEpisode(player_pos)


    def on_render(self):
        """
        The render method plots the First RGB, the First Depth and First
        Semantic Segmentation Camera.
        """
        pos_x = 0

        if self.depth_vec:
            self.depth_vec[0] = self.depth_vec[0][:, :, :3]
            self.depth_vec[0] = self.depth_vec[0][:, :, ::-1]
            self.depth_vec[0] = convert_depth(self.depth_vec[0])
            surface = pygame.surfarray.make_surface(
                np.transpose(self.depth_vec[0], (1, 0, 2)))
            self._display_surf.blit(surface, (pos_x, 0))
            pos_x += self.depth_vec[0].shape[1]

        if self.img_vec:
            self.img_vec[0] = self.img_vec[0][:, :, :3]
            self.img_vec[0] = self.img_vec[0][:, :, ::-1]
            surface = pygame.surfarray.make_surface(
                np.transpose(self.img_vec[0], (1, 0, 2)))
            self._display_surf.blit(surface, (pos_x, 0))
            pos_x += self.img_vec[0].shape[1]

        if self.labels_vec:
            self.labels_vec[0] = join_classes(self.labels_vec[0][:, :, 2])
            surface = pygame.surfarray.make_surface(
                np.transpose(self.labels_vec[0], (1, 0, 2)))
            self._display_surf.blit(surface, (pos_x, 0))
            pos_x += self.labels_vec[0].shape[1]

        pygame.display.flip()

    def on_cleanup(self):
        self.carla.closeConections()
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            try:

                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()

            except Exception as e:
                logging.exception(e)
                self._running = False
                break

        self.on_cleanup()


def main():
    parser = argparse.ArgumentParser(
        description='Run the carla client manual that connects to CARLA server')
    parser.add_argument(
        'host',
        metavar='HOST',
        type=str,
        help='host to connect to')
    parser.add_argument(
        'port',
        metavar='PORT',
        type=int,
        help='port to connect to')

    parser.add_argument(
        "-c",
        "--config",
        help="the path for the server .ini config file that the client sends",
        type=str,
        default="./CarlaSettings.ini")

    parser.add_argument(
        "-l",
        "--log",
        help="activate the log file",
        action="store_true")
    parser.add_argument(
        "-lv",
        "--log_verbose",
        help="put the log file to screen",
        action="store_true")
    args = parser.parse_args()

    if args.log or args.log_verbose:
        LOG_FILENAME = 'log_manual_control.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
        if args.log_verbose:  # set of functions to put the logging to screen

            root = logging.getLogger()
            root.setLevel(logging.DEBUG)
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            root.addHandler(ch)

    theApp = App(port=args.port, host=args.host, config=args.config)
    theApp.on_execute()


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
print('\nCancelled by user. Bye!')
