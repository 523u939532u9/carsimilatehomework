import carla
import cv2
import numpy as np
import time

class DriverFatigueAlert:
    def __init__(self):
        self.eye_close_frame = 0
        self.alert_threshold = 15
        self.is_fatigue = False

    # 保留原有疲劳预警核心判定与提示逻辑
    def trigger_fatigue_warn(self):
        self.is_fatigue = True
        print("⚠️ 疲劳驾驶预警：驾驶员长时间闭眼，请靠边休息！")
        blank_img = np.zeros((480,640,3), dtype=np.uint8)
        cv2.putText(blank_img, "FATIGUE WARNING!", (50,80), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
        cv2.imshow("Driver View", blank_img)
        cv2.waitKey(1)

if __name__ == "__main__":
    # 连接CARLA UE4仿真
    client = carla.Client("localhost", 2000)
    client.set_timeout(8.0)
    world = client.get_world()

    bp_lib = world.get_blueprint_library()
    car_bp = bp_lib.filter("model3")[0]
    spawn_point = world.get_map().get_spawn_points()[0]
    ego_car = world.spawn_actor(car_bp, spawn_point)

    # 车辆起步行驶
    move_control = carla.VehicleControl(throttle=0.3, steer=0)
    ego_car.apply_control(move_control)
    print("车辆开始正常行驶...")

    fatigue_judge = DriverFatigueAlert()
    start_time = time.time()

    try:
        while True:
            world.tick()
            run_time = time.time() - start_time
            # 行驶3秒自动触发疲劳预警
            if run_time >= 3 and fatigue_judge.is_fatigue is False:
                fatigue_judge.trigger_fatigue_warn()
    except KeyboardInterrupt:
        ego_car.destroy()
        cv2.destroyAllWindows()