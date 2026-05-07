import math

def get_speed(vehicle):
    v = vehicle.get_velocity()
    return 3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)

def cruise_control(current_speed, target_speed):
    if current_speed < target_speed:
        return {"throttle": 0.4, "brake": 0.0}
    return {"throttle": 0.0, "brake": 0.0}