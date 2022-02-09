
from picamera import PiCamera
from time import sleep

# ---------------------- on first run -----------------------------
#camera = PiCamera()
#------------------------------------------------------------------

camera.resolution = (200, 200)
camera.framerate = 60
camera.brightness = 60
camera.saturation = 60 
camera.rotation = 180


i = 0
for i in range(5):
    sleep(0)
    camera.capture('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1'+str(i)+'.jpg', format = None, use_video_port=False)
    print(i)
    
print("done")

