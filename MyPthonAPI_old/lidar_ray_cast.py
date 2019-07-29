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

		camera_rgb = world.get_blueprint_library().find('sensor.camera.semantic_segmentation')
		# camera_rgb.set_attribute('image_size_x', '1920')
		# camera_rgb.set_attribute('image_size_y', '1080')
		# camera_rgb.set_attribute('fov', '110')
		transform = carla.Transform(carla.Location(x=0.8, z=1.7))
		# camera_rgb_attach = world.spawn_actor(camera_rgb, transform, attach_to=ego_vehicle)

		ray_casting = camera_rgb_attach.listen(lambda image: image.save_to_disk('output/%06d.png' % image.frame_number))
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

