import carla
import time
import random
import math

debug = 0

def iConvertTo360(x):
	if x >0:
		x+=0.0
	else:
		x=360+x
	return x


def iGetRotatedPoint(car_bounding_box,point_angle,car_transform):
	rDistance= math.sqrt((car_bounding_box.extent.x * car_bounding_box.extent.x)+(car_bounding_box.extent.y*car_bounding_box.extent.y))
	car_angle=car_transform.rotation.yaw
	car_angle=iConvertTo360(car_angle)
	point_angle=math.degrees(point_angle)
	point_angle= iConvertTo360(point_angle)
	car_bounding_box.location.x =  car_bounding_box.location.x + (rDistance * math.sin(math.radians(point_angle)))
	car_bounding_box.location.y =  car_bounding_box.location.y + (rDistance * math.cos(math.radians(point_angle)))
	tempX= car_bounding_box.location.x
	tempY= car_bounding_box.location.y
	car_bounding_box.location.y = car_transform.location.y + (math.cos(math.radians(360-car_angle)) * (tempY- car_transform.location.y)) - (math.sin(math.radians(360-car_angle)) * (tempX- car_transform.location.x))
	car_bounding_box.location.x = car_transform.location.x + (math.sin(math.radians(360-car_angle)) * (tempY- car_transform.location.y)) + (math.cos(math.radians(360-car_angle)) * (tempX- car_transform.location.x))
	return car_bounding_box.location



def getActorBoundingBox2DPoints(Actor,Map,World):
	points = []
	transform=Actor.get_transform()
	
	bounding_box = Actor.bounding_box
	bounding_box.location = bounding_box.location + transform.location
	angle1 = math.atan2 (bounding_box.extent.x,bounding_box.extent.y)
	point1= iGetRotatedPoint(bounding_box,angle1,transform)
	points.append(point1)

	bounding_box = Actor.bounding_box
	bounding_box.location = bounding_box.location + transform.location
	rDistance= math.sqrt((bounding_box.extent.x*bounding_box.extent.x)+(bounding_box.extent.y*bounding_box.extent.y))
	angle2 = math.atan2 (bounding_box.extent.x,-bounding_box.extent.y)
	point2= iGetRotatedPoint(bounding_box,angle2,transform)
	points.append(point2)

	bounding_box = Actor.bounding_box
	bounding_box.location = bounding_box.location + transform.location
	rDistance= math.sqrt((bounding_box.extent.x*bounding_box.extent.x)+(bounding_box.extent.y*bounding_box.extent.y))
	angle3 = math.atan2 (-bounding_box.extent.x, -bounding_box.extent.y )
	point3= iGetRotatedPoint(bounding_box,angle3,transform)
	points.append(point3)

	bounding_box = Actor.bounding_box
	bounding_box.location = bounding_box.location + transform.location 
	rDistance= math.sqrt((bounding_box.extent.x*bounding_box.extent.x)+(bounding_box.extent.y*bounding_box.extent.y))
	angle4 = math.atan2 (-bounding_box.extent.x, bounding_box.extent.y)
	point4= iGetRotatedPoint(bounding_box,angle4,transform)
	points.append(point4)
	
	if debug:
		for i in range(len(points)):
			World.debug.draw_point(points[i], size=0.2, color=carla.Color(r=255), life_time=-1.0, persistent_lines=True)
	return points


def iResultantVelocity(Actor):
	velX = Actor.get_velocity().x * Actor.get_velocity().x
	velY = Actor.get_velocity().y * Actor.get_velocity().y
	velZ = Actor.get_velocity().z * Actor.get_velocity().z
	return math.sqrt(velX+velY+velZ)

def getDatasetFeatures(Actor,Map,World):

	safeDistance = 4 * iResultantVelocity(Actor)
	for actor in World.get_actors().filter('vehicle.*'):
		
		if actor.attributes.get('role_name') == 'hero':
			pass
		else:
			diffX = (Actor.get_location().x - actor.get_location().x) * (Actor.get_location().x - actor.get_location().x)
			diffY = (Actor.get_location().y - actor.get_location().y) * (Actor.get_location().y - actor.get_location().y) 
			dstBtwActorAndObst = math.sqrt(diffX + diffY)
			
			if dstBtwActorAndObst < 100 :
		
				delLi= dstBtwActorAndObst - safeDistance
				delVi= iResultantVelocity(Actor)- iResultantVelocity(actor)
				return 	delLi,delVi,Actor.get_location(), Actor.get_velocity(),Actor.get_angular_velocity(),Actor.get_transform().rotation.yaw,actor.get_location(),actor.get_transform().rotation.yaw,actor.get_velocity(),actor.bounding_box.extent.x*2,actor.bounding_box.extent.y*2,actor.bounding_box.extent.z*2,getActorBoundingBox2DPoints(actor,Map,World),actor.type_id
			else:
				return 



def main():
	try:
		client = carla.Client('localhost', 2000)
		client.set_timeout(10.0)
		world = client.get_world()
		map = world.get_map()
		blueprint_library = world.get_blueprint_library()
		for actor in world.get_actors():
			if actor.attributes.get('role_name') == 'hero':
				ego = actor
				break

		f=open("dataset.csv","w")
		f.write("delLi,delVi,egoLocationX,egoLocationY,egoLocationZ,egoVelocityX,egoVelocityY,egoVelocityZ,egoAngularVelocityX,egoAngularVelocityY,egoAngularVelocityZ,egoHeading,obstacleLocationX,obstacleLocationY,obstacleLocationZ,obstacleHeading,obstacleVelocityX,obstacleVelocityY,obstacleVelocityZ,obstacleLength,obstacleWidth,obstacleHeight,obstacleBoundingBoxPointsP1X,obstacleBoundingBoxPointsP1Y,obstacleBoundingBoxPointsP2X,obstacleBoundingBoxPointsP2Y,obstacleBoundingBoxPointsP3X,obstacleBoundingBoxPointsP3Y,obstacleBoundingBoxPointsP4X,obstacleBoundingBoxPointsP4Y,obstacleType\n")
		map_waypoints=map.generate_waypoints(1.0)
		
		while True:
			try:
				delLi,delVi,egoLocation, egoVelocity,egoAngularVelocity,egoHeading,obstacleLocation,obstacleHeading,obstacleVelocity,obstacleLength,obstacleWidth,obstacleHeight,obstacleBoundingBoxPoints,obstacleType=getDatasetFeatures(ego,map,world)
				f.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(delLi,delVi,egoLocation.x,egoLocation.y,egoLocation.z,egoVelocity.x,egoVelocity.y,egoVelocity.z,egoAngularVelocity.x,egoAngularVelocity.y,egoAngularVelocity.z,egoHeading,obstacleLocation.x,obstacleLocation.y,obstacleLocation.z,obstacleHeading,obstacleVelocity.x,obstacleVelocity.y,obstacleVelocity.z,obstacleLength,obstacleWidth,obstacleHeight,obstacleBoundingBoxPoints[0].x,obstacleBoundingBoxPoints[0].y,obstacleBoundingBoxPoints[1].x,obstacleBoundingBoxPoints[1].y,obstacleBoundingBoxPoints[2].x,obstacleBoundingBoxPoints[2].y,obstacleBoundingBoxPoints[3].x,obstacleBoundingBoxPoints[3].y,str(obstacleType)[0:7]))
				f.write("\n")
				time.sleep(0.1)
			except TypeError:
				pass

		
	finally:
		f.close()
		print("Finally..!!!")
		
	

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')
