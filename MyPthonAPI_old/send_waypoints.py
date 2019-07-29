

import carla
import time
import random

def main():
	
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0) # seconds
		world = client.get_world()
		map = world.get_map()
		blueprint_library = world.get_blueprint_library()		
		print(world)
		# print(world.get_actors())
		# print(world.get_actors())
		for actor in world.get_actors():
			if actor.attributes.get('role_name') == 'hero':
				ego = actor
				break
		
		print("ego vehicle {}".format(ego))
		
		# Attach to ego 
		
		waypoint = map.get_waypoint(ego.get_location())

		ego.set_simulate_physics(False)
		
		while True:
    			# Find next waypoint 2 meters ahead.
    			waypoint = random.choice(waypoint.next(2.0))
    			# print("Road ID : {} , Lane ID : {}".format(waypoint.road_id, waypoint.lane_id))
    			# Teleport the vehicle.
    			# print(waypoint.transform.location.x)
    			# print(waypoint.transform.location.y)
    			# print("X Location : {}, Y Location : {}".format(waypoint.transform.location.x,waypoint.transform.location.y))
    			print(waypoint.transform.location.x, waypoint.transform.location.y)
    			ego.set_transform(waypoint.transform)
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


