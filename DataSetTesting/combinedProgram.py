import vlc
from os import path
from picamera import PiCamera
from time import sleep
import numpy
from PIL import Image

# -----uncomment the following when using a pi connected to the camera-----
camera = PiCamera()

camera.start_preview()
#camera.stop_preview()

camera.resolution = (300,300)
camera.framerate = 60
camera.brightness = 60
camera.saturation = 60 
camera.rotation = 180

camera.start_preview()

#while True:
for i in range(15):
    sleep(0)
    camera.capture('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset3/image'+str(i)+'.jpg', format = None, use_video_port=True)

camera.stop_preview()    
    
def getAvgColor(image):
    pixel_values = list(image.getdata())
    width, height = image.size
    avgR = 0
    avgG = 0
    avgB = 0
        
    for j in range(len(pixel_values)):
        avgR += pixel_values[j][0]
        avgG += pixel_values[j][1]
        avgB += pixel_values[j][2]
            #print(avg)
    avgR /= (width*height)
    avgG /= (width*height)
    avgB /= (width*height)
        
    avg = (avgR, avgG, avgB)
    return avg
    
def recognizeFace():
    y = 0
    n = 0
    for i in range(15):
        #img = open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg')
        avg = getAvgColor(Image.open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset3/image'+str(i)+'.jpg', "r"));
#         img = Image.open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset1/image'+str(i)+'.jpg', "r")
#         width, height = img.size
#         pixel_values = list(img.getdata())
#         #print(pixel_values)
#         avgR = 0
#         avgG = 0
#         avgB = 0
#         
#         for j in range(len(pixel_values)):
#             avgR += pixel_values[j][0]
#             avgG += pixel_values[j][1]
#             avgB += pixel_values[j][2]
#             #print(avg)
#         avgR /= (width*height)
#         avgG /= (width*height)
#         avgB /= (width*height)
        
        #avg = (avgR, avgG, avgB)
        if avg >= (160, 160, 160):
            y += 1
        if avg < (160, 160, 160):
            n += 1
            
    print(y)
    print(n)
    if y > n:
        print("yes light")
        sound = vlc.MediaPlayer("boing.wav")
        sound.stop()
        sound.play()
    if n > y:
        print("no light")
    if n == y:
        print("helena wtf do i do in this situation")
            
        
    #print(pixel_values)

recognizeFace()
#print(getAvgColor(Image.open('/home/pi/MachineLearningDoorbell/DataSetTesting/dataset3/image14.jpg')))

        