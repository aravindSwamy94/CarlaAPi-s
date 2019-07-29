import carla
import time

def main():
	
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0) # seconds
		world = client.get_world()
		blueprint_library = world.get_blueprint_library()
		vehicles = blueprint_library.filter('vehicle.*')
		# print(vehicles)
		ego_vehicle = world.get_actors().filter('vehicle.*')
		print(ego_vehicle)

		for actor in ego_vehicle:
			print(actor)
			ego_vehicle = actor

		print(ego_vehicle.get_location())

		camera_rgb = world.get_blueprint_library().find('sensor.camera.rgb')
		camera_rgb.set_attribute('image_size_x', '1920')
		camera_rgb.set_attribute('image_size_y', '1080')
		camera_rgb.set_attribute('fov', '110')
		transform = carla.Transform(carla.Location(x=0.8, z=1.7))
		camera_rgb_attach = world.spawn_actor(camera_rgb, transform, attach_to=ego_vehicle)

		camera_rgb_attach.listen(lambda image: image.save_to_disk('output/%06d.png' % image.frame_number))
		print("Save image")


		while True:
			time.sleep(1)
	
	finally:
		print("Finally..!!!")


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')

'''
def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--host',
        metavar='H',
        default='127.0.0.1',
        help='IP of the host server (default: 127.0.0.1)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    argparser.add_argument(
        '-n', '--number-of-vehicles',
        metavar='N',
        default=10,
        type=int,
        help='number of vehicles (default: 10)')
    argparser.add_argument(
        '-d', '--delay',
        metavar='D',
        default=2.0,
        type=float,
        help='delay in seconds between spawns (default: 2.0)')
    argparser.add_argument(
        '--safe',
        action='store_true',
        help='avoid spawning vehicles prone to accidents')
    args = argparser.parse_args()

    actor_list = []

    try:

        client = carla.Client(args.host, args.port)
        client.set_timeout(2.0)
        world = client.get_world()
        blueprints = world.get_blueprint_library().filter('vehicle.*')

        if args.safe:
            blueprints = [x for x in blueprints if int(x.get_attribute('number_of_wheels')) == 4]
            blueprints = [x for x in blueprints if not x.id.endswith('isetta')]

        def try_spawn_random_vehicle_at(transform):
            blueprint = random.choice(blueprints)
            if blueprint.has_attribute('color'):
                color = random.choice(blueprint.get_attribute('color').recommended_values)
                blueprint.set_attribute('color', color)
            blueprint.set_attribute('role_name', 'autopilot')
            vehicle = world.try_spawn_actor(blueprint, transform)
            if vehicle is not None:
                actor_list.append(vehicle)
                vehicle.set_autopilot()
                print('spawned %r at %s' % (vehicle.type_id, transform.location))
                return True
            return False

        # @todo Needs to be converted to list to be shuffled.
        spawn_points = list(world.get_map().get_spawn_points())
        random.shuffle(spawn_points)

        print('found %d spawn points.' % len(spawn_points))

        count = args.number_of_vehicles

        for spawn_point in spawn_points:
            if try_spawn_random_vehicle_at(spawn_point):
                count -= 1
            if count <= 0:
                break

        while count > 0:
            time.sleep(args.delay)
            if try_spawn_random_vehicle_at(random.choice(spawn_points)):
                count -= 1

        print('spawned %d vehicles, press Ctrl+C to exit.' % args.number_of_vehicles)

        while True:
            time.sleep(10)

    finally:

        print('\ndestroying %d actors' % len(actor_list))
        for actor in actor_list:
            actor.destroy()


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')
        
'''
