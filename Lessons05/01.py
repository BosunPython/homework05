
camera = {"Bullet": "2Mp", "Turret": "4Mp", "Dome": "5Mp"}
brands_camera = {1: "Hikvision", 2: "Dahua", 3: "UNV"}
def func_camera(a,b):
    result = camera | brands_camera
    return result
all_cameras = func_camera(camera, brands_camera)
print(all_cameras)

