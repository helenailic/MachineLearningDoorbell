import vlc
from os import path
from picamera import PiCamera
from time import sleep
from PIL import Image
import math
sound = vlc.MediaPlayer("/home/pi/boing.mp3")

#start camera
camera = PiCamera()
camera.resolution = (300,300)
camera.framerate = 60
camera.brightness = 60
camera.saturation = 60 
camera.rotation = 180

# isSamePixel method that takes in two pixels and checks if they are close
def isSamePixel(pixel1, pixel2):
  isSame = True
  if abs(pixel1[0] - pixel2[0]) > 15:
    isSame = False
  if abs(pixel1[1] - pixel2[1]) > 15:
    isSame = False
  if abs(pixel1[2] - pixel2[2]) > 15:
    isSame = False
  return isSame

# take an example image
camera.capture('/home/pi/orig.jpg', format = None, use_video_port=True)
sleep(1)

# loop the following 5 times:
n = 0
i = 0
for i in range(500):
  # take another image and see if more than 100 pixels changed from the first image
  camera.capture('/home/pi/new.jpg', format = None, use_video_port=True)
  original = Image.open('/home/pi/orig.jpg', "r")
  new = Image.open('/home/pi/new.jpg', "r")
  width1, height1 = original.size
  width2, height2 = new.size
  pixel_values1 = list(original.getdata())
  pixel_values2 = list(new.getdata())
  changedPixels = 0
  
  # if it does, then increase a number
  for j in range(len(pixel_values1)):
    if isSamePixel(pixel_values1[j], pixel_values2[j]):
        pass
    else:
        changedPixels += 1

  if changedPixels > 10000:
    n += 1;
    print(changedPixels)
    sound.stop()
    sound.play()

  # take a new reference image
  camera.capture('/home/pi/orig.jpg', format = None, use_video_port=True)
  
  # wait 1 second
  sleep(1)

# if n >= 3, then play the sound effect because there was motion
