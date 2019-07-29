
import glob
import os
import sys
import carla

import argparse
import random
import time
import xml.etree.ElementTree as ET



def analyse(data):
	
	#print("Other actor {}, data.distance {}".format(data.other_actor, data.distance))
    pass

def getMapInfo(roadid):
    lat=49.000000
    lon=8.000000
    tree = ET.parse('Town01.xml')
    root = tree.getroot()
    latlon = root.find('header').find('geoReference').text
    for child in root.iter('road'):
        if(int(child.attrib['id'])==roadid):
            distX=float(child.find('planView').find('geometry').attrib['x'])
            distY=float(child.find('planView').find('geometry').attrib['y'])
            dist= math.sqrt((distX*distX)+ (distY*distY))            
            break

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0) # seconds
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    map = world.get_map()
    sensor_obs = world.get_blueprint_library().find('sensor.other.obstacle')
    transform = carla.Transform(carla.Location(x=0.8, z=1.7))
    for actor in world.get_actors():
        if actor.attributes.get('role_name') == 'hero':
            ego = actor
            egoWaypoint = map.get_waypoint(ego.get_location())
            break
    sensor_obs_attach = world.spawn_actor(sensor_obs, transform, attach_to=ego)
    sensor_obs_attach.listen(lambda data: analyse(data))
    #sensor_obs.set_attribute('distance', '10')
    #sensor_obs.set_attribute('hit_radius', '0.25')
    #sensor_obs.set_attribute('debug_linetrace', 'false')
    #print(world)
    while True:
        for actor in world.get_actors():
            if actor.attributes.get('role_name') == 'hero':
                ego = actor
                egoWaypoint = map.get_waypoint(ego.get_location())
                break
        for actor in world.get_actors().filter("vehicle.*"):
            if actor.attributes.get('role_name') == 'hero':
                continue
            actorWaypoint= map.get_waypoint(actor.get_location())
            if((egoWaypoint.lane_id == actorWaypoint.lane_id) and (egoWaypoint.road_id == actorWaypoint.road_id)):
                print("actor {} OBSTACLE_FOLLOW".format(actor))
            else:
                pass
                #print ("actor{} LANE_FOLLOW".format(actor))
        time.sleep(1)
    

if __name__ == '__main__':
    main()
