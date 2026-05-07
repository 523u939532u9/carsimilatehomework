def get_speed_limit(vehicle, carla_map):
    # 由于部分 CARLA 版本不支持 get_speed_limit，我们用一个固定的安全限速
    # 你可以根据需要调整这个值，比如城市道路 50，高速 100
    return 50.0