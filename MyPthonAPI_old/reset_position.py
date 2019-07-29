import carla
client = carla.Client('localhost', 2000)
client.set_timeout(10.0) # seconds
world = client.get_world()
map = world.get_map()
blueprint_library = world.get_blueprint_library()
for actor in world.get_actors():
        if actor.attributes.get('role_name') == 'hero':
                ego = actor
                break
                
print("ego vehicle {}".format(ego))

# ego vehicle Actor(id=132, type=vehicle.nissan.micra)

transform=ego.get_transform()
transform.location.x = -66.1467
transform.location.y = 135.467
transform.location.z = 135.467
transform.location.z = 0
transform.rotation.pitch = 0
transform.rotation.yaw = -1.2968
transform.rotation.roll = 0
ego.set_transform(transform)
