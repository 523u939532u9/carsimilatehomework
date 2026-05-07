import carla
import time
from module1_spawn import spawn_vehicle
from module2_cruise import get_speed, cruise_control

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
        print("✅ 作业2运行成功：定速巡航")
        target = 20
        for _ in range(500):
            world.tick()
            speed = get_speed(vehicle)
            ctrl = cruise_control(speed, target)
            vehicle.apply_control(carla.VehicleControl(**ctrl))
            time.sleep(0.05)
    finally:
        if vehicle:
            vehicle.destroy()
        settings.synchronous_mode = False
        world.apply_settings(settings)

if __name__ == "__main__":
    main()