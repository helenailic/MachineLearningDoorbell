import vlc
from os import path
from picamera import PiCamera
from time import sleep
import numpy
from PIL import Image


#camera = PiCamera()

#camera.resolution = (300,300)
#camera.framerate = 60
#camera.brightness = 60
#camera.saturation = 60 
#camera.rotation = 180

#while true:
#    for i in range(10):
#        sleep(0)
#        camera.capture('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg', format = None, use_video_port=True)
#recognizeFace()    
    
#def recognizeFace():
y = 0
n = 0
for i in range(10):
    #img = open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg')
    img = Image.open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg', "r")
    #width, height = img.size
    pixel_values = list(img.getdata())
    for j in range(len(pixel_values)):
        #print(j)
    #print(pixel_values)
        