
from picamera import PiCamera
from time import sleep

# ---------------------- on first run -----------------------------
#camera = PiCamera()
#------------------------------------------------------------------

camera.resolution = (300,300)
camera.framerate = 60
camera.brightness = 60
camera.saturation = 60 
camera.rotation = 180

i = 0
for i in range(50):
    sleep(0)
    camera.capture('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg', format = None, use_video_port=True)
    print(i)
    
print("done")

