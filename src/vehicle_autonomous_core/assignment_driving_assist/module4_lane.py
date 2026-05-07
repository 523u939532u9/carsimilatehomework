import math
import carla

def lane_keep(vehicle, carla_map):
    wp = carla_map.get_waypoint(vehicle.get_location(), project_to_road=True)
    if not wp:
        return 0.0
    dx = vehicle.get_location().x - wp.transform.location.x
    dy = vehicle.get_location().y - wp.transform.location.y
    yaw = math.radians(vehicle.get_transform().rotation.yaw)
    cross = dx * math.sin(yaw) - dy * math.cos(yaw)
    return max(-0.15, min(0.15, -cross * 0.2))