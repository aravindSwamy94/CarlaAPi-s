import carla
import time
import numpy
import scipy.misc

def to_bgra_array(image):
    	"""Convert a CARLA raw image to a BGRA numpy array."""
    	# if not isinstance(image, sensor.Image):
        #	raise ValueError("Argument must be a carla.sensor.Image")
    	array = numpy.frombuffer(image.raw_data, dtype=numpy.dtype("uint8"))
    	array = numpy.reshape(array, (image.height, image.width, 4))
	return array


def labels_to_array(image):
    	"""
    	Convert an image containing CARLA semantic segmentation labels to a 2D array
    	containing the label of each pixel.
    	"""
	return to_bgra_array(image)[:, :, 2]


def red_to_semantic(image):
	
    	"""
    	Convert an image containing CARLA semantic segmentation labels to
    	Cityscapes palette.
    	"""
    	classes = {
        	0: [0, 0, 0],         # None
        	1: [70, 70, 70],      # Buildings
        	2: [190, 153, 153],   # Fences
        	3: [72, 0, 90],       # Other
        	4: [220, 20, 60],     # Pedestrians
        	5: [153, 153, 153],   # Poles
        	6: [157, 234, 50],    # RoadLines
        	7: [128, 64, 128],    # Roads
        	8: [244, 35, 232],    # Sidewalks
        	9: [107, 142, 35],    # Vegetation
        	10: [0, 0, 255],      # Vehicles
        	11: [102, 102, 156],  # Walls
        	12: [220, 220, 0]     # TrafficSigns
    	}
    	array = labels_to_array(image)
    	result = numpy.zeros((array.shape[0], array.shape[1], 3))
    	for key, value in classes.items():
        	result[numpy.where(array == key)] = value
	
	
	frame = image.frame_number
	address = '/home/kishor/GWM/Carla_Sim/sem_out/%0.6d.png' % frame
	
	scipy.misc.imsave(address, result)
	
	return result


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
		camera_rgb.set_attribute('image_size_x', '1920')
		camera_rgb.set_attribute('image_size_y', '1080')
		camera_rgb.set_attribute('fov', '110')
		transform = carla.Transform(carla.Location(x=0.8, z=1.7))
		camera_rgb_attach = world.spawn_actor(camera_rgb, transform, attach_to=ego_vehicle)

		# camera_rgb_attach.listen(lambda image: image.save_to_disk('semantic_output/%06d.png' % image.frame_number))

		camera_rgb_attach.listen(lambda image: red_to_semantic(image))
	
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

