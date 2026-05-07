import math

def check_obstacle(vehicle, world):
    min_dist = 999.0
    for actor in world.get_actors().filter("vehicle.*"):
        if actor.id == vehicle.id:
            continue
        dx = actor.get_location().x - vehicle.get_location().x
        dy = actor.get_location().y - vehicle.get_location().y
        dist = math.sqrt(dx**2 + dy**2)
        if dist < min_dist:
            min_dist = dist
    return min_dist < 8.0, min_dist