# CARLA 0.9.X API Proposal
# ========================
#
# Core concepts:
#
#   - World: a loaded map.
#   - Blueprint: specifications for creating an actor.
#   - Actor: anything that plays a role in the simulation.
#   - Sensor: an actor that produces a data stream.
#   - Agent: an AI that controls an actor.

import carla

from carla import Location, Rotation, Transform


### Use case ###################################################################

client = carla.Client('localhost', 2000)

client.set_timeout(1000)

world = client.get_world()

blueprint_library = world.get_blueprint_library()
vehicle_blueprints = blueprint_library.filter('vehicle.mustang.*')
blueprint = random.choice(vehicle_blueprints)

transform = Transform(Location(50.0, 50.0, 2.0))
player_vehicle = world.spawn_actor(blueprint, transform)

vehicle_camera = carla.Camera('MyCameraDepth', type='Depth')
vehicle_camera.attach_to(player_vehicle, Transform(Location(z=60.0)))
vehicle_camera.listen(lambda image: image.save_to_disk())

static_camera = carla.Camera('SecurityCamera', type='SceneFinal')
static_camera.attach_to(world, Transform(Location(x=30.0), Rotation(yaw=90)))
static_camera.listen(lambda image: image.save_to_disk())

while True:
    control = carla.VehicleControl(throttle=0.6, reverse=True)
    player_vehicle.apply_control(control)

    time.sleep(1)


### Spawning error handling ####################################################

actor = world.try_spawn_actor(blueprint, Transform())
if actor is None:
    return

try:
    actor = world.spawn_actor(blueprint, Transform())
except SpawnException as e:
    print('cannot spawn actor: %s' % e)
    print('try at %s' % e.suggested_transform)


### Spawning multiple actors at once ###########################################

actors = world.try_spawn_actors([
    [blueprint, Transform(Location(x=20.0))],
    [blueprint, Transform(Location(x=40.0))],
    [blueprint, Transform(Location(x=60.0))],
    [blueprint, Transform(Location(x=0.0))]])


## Teleporting actors ##########################################################

# Actors' transforms can be set, effectively teleporting the actor without using
# the physics engine.

actor.set_transform(Transform(Location(x=10.0, y=10.0)))


### Control multiple actors at once ############################################

world.apply_control_to_actors([
    [actor0, carla.VehicleControl(throttle=2.0)],
    [actor1, carla.VehicleControl(throttle=4.0)],
    [actor2, carla.VehicleControl(throttle=0.0)]])


### Everything is an actor, everything can be controlled #######################

# We will have different kinds of control, and in principle they can be applied
# to any actor. However, there are some that are specific for certain types of
# actors.

bps = blueprint_library.filter('pedestrian.*')
pedestrian = world.spawn_actor(random.choice(bps), Transform())
try:
    pedestrian.apply_control(carla.VehicleControl())
except InvalidControlType as e:
    print('cannot control a pedestrian as a vehicle!')


### Locking actors #############################################################

# When an actor is locked, this client instance is the only one able to control
# the actor.

actor = world.spawn_actor('*', Transform(), lock=True) # Should they start
if not actor.is_locked():                              # locked by default?
    actor.lock()

# However, locking is only relevant if we have methods of retrieving existing
# actors in the scene.


### Sensors are asynchronous ###################################################

# At the server-side, sensors produce data asynchronously, every time a data
# blob arrives (one image, one set of lidar points, etc), the callback
# registered at "listen" is called.

sensor.listen(functor) # function, lambda, callable object.


### Sensor adapters ############################################################

# It would be nice if we can provide sensor adapters, e.g.

# Holding a queue of the data.
data_queue = carla.DataQueue(sensor) # self-registers a listen callback.
data_queue.try_pop()
data_queue.pop()

# Synchronizing two or more sensors.
composite = carla.CompositeSensor(camera_rgb, camera_depth)
composite.listen(lambda rgb, depth: make_point_cloud(rgb, depth)) # syncs rgb and depth
                                                                  # with same frame number.


### Current Carla measurements are migrated to sensors #########################

# (temporary names, we need to think about names everywhere)

carla.GroundTruthGPS()         # actor's location.
carla.GroundTruthIMU()         # actor's transform, speed, acceleration.
carla.LaneDetector()           # percentage of actor off-road and opposite lane.
carla.CollisionDetector()      # actor's collision accum. for pedestrians, vehicles, other.
carla.AutopilotControlSensor() # this one will be fully moved to client-side eventually.

# TODO: How to migrate current non-player agents info.

# Extra overhead:
# Every sensor data needs to be tagged with time-stamps: platform time, game time, frame number.
# Positionable sensors should also send their world position every frame.


### Positionable sensors can be moved ##########################################

camera = carla.Camera('SecurityCamera')
camera.attach_to(world, Transform(Location(z=4.0), Rotation(pitch=-15)))
camera.listen(lambda image: image.save_to_disk())

current_yaw = 0
while True:
    t = Transform(rotation=Rotation(yaw=current_yaw))
    camera.set_transform(t)
    current_yaw = (current_yaw + 1) % 360
    time.sleep(1)


### Example using current autopilot ############################################

# Using autopilot without modifications.
vehicle = world.spawn_actor(blueprint, Transform())
vehicle.apply_control(carla.AutopilotControl()) # only once.

# Modifying autopilot input.
vehicle = world.spawn_actor(blueprint, Transform())
def add_noise(control):
    control.steer += random.uniform(-0.2, 0.2)
    return control
sensor = carla.AutopilotControlSensor()
sensor.attach_to(vehicle)
sensor.listen(lambda control: vehicle.apply_control(add_noise(control)))

# My idea on how this will work in the future.
vehicle = world.spawn_actor(blueprint, Transform())
agent = carla.AutopilotAgent() # Users can easily write their agents.
agent.possess(vehicle)


### Synchronous mode ###########################################################

# I'm still not sure if it should be done at actor level or world level.

# Actor level. (this is how it is done pre-0.9).
vehicle.set_synchronous(True)
while True:
    vehicle.apply_control(...) # The world does not advance until this message
                               # is received. (Until control for every
                               # synchronous actor is received).

# World level.
world.set_synchronous(True)
while True:
    vehicle.apply_control(...)
    world.tick()  # The world does not advance until this message is received.
                  # pros: synchronization in single place.
                  # cons: two messages (control and tick).


### Spectator ##################################################################

# For debugging and video recording, being able to control the spectator (view
# in the simulator window) it's a plus.

spectator = world.get_spectator()
spectator.set_transform(...)
