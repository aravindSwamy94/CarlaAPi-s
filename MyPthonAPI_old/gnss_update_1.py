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
		print(world.get_actors())
		ego_vehicle = world.get_actors().filter('vehicle.*')
		print(ego_vehicle)

		for actor in ego_vehicle:
			print(actor)
			ego_vehicle = actor

		print(ego_vehicle.get_location())

		gnss_sensor = world.get_blueprint_library().find('sensor.other.gnss')
		transform = carla.Transform(carla.Location(x=0.8, z=1.7))
		gnss_sensor_attach = world.spawn_actor(gnss_sensor, transform, attach_to=ego_vehicle)

		gnss_sensor_attach.listen(lambda data: print(data))
		# print("Save image")


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


