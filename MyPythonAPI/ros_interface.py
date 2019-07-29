import getActorInformation2
import rospy
import carla
import time
from std_msgs.msg import String
import prediction_pb2
from prediction_pb2 import PredictionObstacles

from datetime import datetime
def main():
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0)
		world = client.get_world()
		map = world.get_map()
		map.save_to_disk("/home/aravind/Desktop/GWM_Tasks/Carla/Precompiled/CARLA_0.9.4/CarlaUE4/Content/Carla/Maps/OpenDrive/town03.xml")
		blueprint_library = world.get_blueprint_library()
		for actor in world.get_actors():
			if actor.attributes.get('role_name') == 'hero':
				ego = actor
				break
		'''
		transform = ego.get_transform()
		transform.location.x= 229.931
		transform.location.y= 81.3834
		transform.location.z= 0.085772
		transform.rotation.pitch=0.596672
		transform.rotation.yaw=92.8762
		transform.rotation.roll=0.0139714
		ego.set_transform(transform)		
		map_waypoints=map.generate_waypoints(1.0)
		'''
		rospy.init_node('Prediction_Publisher', anonymous=True)
		pub = rospy.Publisher('/carla/prediction', String, queue_size=10)
		rate = rospy.Rate(10) # 10hz
		while not rospy.is_shutdown():
			obstacles = prediction_pb2.PredictionObstacles()


			# Create a loop for all the obstacles that are reuired for trajectory information
			obstaclePredicted = getActorInformation2.getActorTrajectories(ego,map,world)
			obstacle = obstacles.prediction_obstacle.add()
			obstacle.CopyFrom(obstaclePredicted)


			s = String()
			s.data= obstacles.SerializeToString()
			pub.publish(s)
			rate.sleep()
	finally:
		print "Finally..!!!"
		
if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print '\ndone.'
