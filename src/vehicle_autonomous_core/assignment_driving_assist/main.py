import carla
import time
from module1_spawn import spawn_vehicle
from module2_cruise import get_speed, cruise_control
from module3_obstacle import check_obstacle
from module4_lane import lane_keep

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()
    carla_map = world.get_map()

    settings = world.get_settings()
    settings.synchronous_mode = True
    settings.fixed_delta_seconds = 0.05
    world.apply_settings(settings)

    vehicle = None
    try:
        vehicle = spawn_vehicle(world, carla_map)
        print("✅ 作业4运行成功：车道保持")
        target = 20
        for _ in range(1000):
            world.tick()
            speed = get_speed(vehicle)
            has_obstacle, dist = check_obstacle(vehicle, world)
            steer = lane_keep(vehicle, carla_map)
            ctrl = carla.VehicleControl()
            if has_obstacle:
                ctrl.throttle = 0
                ctrl.brake = 1
            else:
                c = cruise_control(speed, target)
                ctrl.throttle = c["throttle"]
                ctrl.brake = c["brake"]
            ctrl.steer = steer
            vehicle.apply_control(ctrl)
            time.sleep(0.05)
    finally:
        if vehicle:
            vehicle.destroy()
        settings.synchronous_mode = False
        world.apply_settings(settings)

if __name__ == "__main__":
    main()