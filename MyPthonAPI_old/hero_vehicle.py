import carla
import time

def main():
	
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0) # seconds
		world = client.get_world()
		blueprint_library = world.get_blueprint_library()		
		print(world)
		print(world.get_actors())
		# print(world.get_actors())
		for actor in world.get_actors():
			if actor.attributes.get('role_name') == 'hero':
				ego = actor
				break
		
		print("ego vehicle {}".format(ego))
		
		# Attach to ego 

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


