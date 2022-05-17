# "MachineLearning"Doorbell
Repository compiling the progress of our Software Engineering 2 Project, Motion Detection *Possibly to be Machine Learning* Doorbell. 

This repository documents how we developed a motion detection camera program, created a dataset full of our classmates, and *possibly* enhanced this motion detection program through a machine learning model. After recognizing an individual's face, a sound effect will play automatically to signal the teacher.

**Hardware:**
  1. RaspberryPI 4 Model B for computing
  2. RasPi HD HQ Camera - 12MP
  3. Flex cable (ours is 1 meter long)
  4. 6mm 3MP Wide Angle Lens for RasPi
  5. 3.5A USB-C Power Supply for Pi
  6. Any USB Powered Speakers (5VDC 1A peak)
  7. Customized 3D designed camera stand
     -Recommend using Tinkercad or Blender for 3D design 
  8. SD Card (16 gb or 32 gb)

**Software:**
  1. Python
  2. RasPICamera
  3. VLC (library for speakers)
  4. RealVNC (to access Pi via PC)
     -Downlaod VNC Viewer and VNC Server on both Pi and PC
     -Very simple setups via internet
  5. RasPi imager of choice
  -*(we dabbled a bit in TensorFlow and PyTorch as well)*
  5.*possibly not yet implemented* Machine Learning Libraries detailed in links below.
  
  -Process-
  1. Image card (this is ultimately saving your work from the RasPi onto the PC)
     -Download Raspberry Pi Imager
     -Insert SD card into PC
     -Install recommended 32-bit RasPi OS
     -Select SD card
     -Write
     
  2. Download this repository on RasPi
     -Follow this file to setup and maintain Git on Pi: https://docs.google.com/document/d/1eWng-q4m3h4TwRcapSAPxexKST6AjQMfA9iVv2GRnwM/edit#
     
  3. Set up hardware
     I. Set up RasPi camera
       -Can follow this video: youtube.com/watch?v=T8T6S5eFpqE (pay attention to flex cable insertion sides)
     II. Connect speakers via USB and audio jack into Pi
       -Go in RasPi config by typing in 'sudo raspi-config' in the terminal and enable speakers 
     III. Use or design a 3D stand for camera and mount (we used Blender software) it by any method (we used command strips)
        -Blender tutorial video used to gather basics, then experiment: https://www.youtube.com/watch?v=JUhWdGcOHPw 
     IV. Place speakers in ideal location to project sound
     V. Connect Pi to power and place within range of camera cord
     
  4. Establish VNC connection (we used RealVNC, it is very simple to use as it goes through the internet instead of a router)
  *Being able to VNC allows you to work on the Pi without needing to take it down from wherever you set it up, as long as it is powered*
     I. Create an account and have someone in your group create a RealVNC team
       -By doing this, other people in your team will be able to access everything in your address book without having to re-add it
     II. Install VNC Viewer and VNC Server on both the Pi and the PC you want to VNC from
       -If you use a different PC at any point you will have to redo all of this, so be consistent with which PC you use
     III. Find the IP address of the Pi in the VNC Server and input it into the VNC Viewer on the PC
     IV. Click on the RasPi in your address book and login with the Pi's credentials if prompted
       -Be sure to have a Pi that everyone can access and knows the password of
       
  5. Download neccessary libraries for machine learning and speakers onto the Pi
    -Install VLC Media module for speaker connection
    -Follow this website to download all ML libraries: https://core-electronics.com.au/guides/object-identify-raspberry-pi/ 
 


Current Issue: Still working on full implementation of the Machine Learning portion of doorbell, although it fully accomplishes purpose as a motion detection doorbell. 
