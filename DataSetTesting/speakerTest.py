import time
import vlc
from os import path
from pydub import AudioSegment
from pygame import mixer

# files                                                                         
#src = "/home/pi/Downloads/boing.mp3"
#dst = "boing.wav"

# convert wav to mp3                                                            
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")

sound = vlc.MediaPlayer("boing.wav")
sound.stop()
sound.play()


#sound = vlc.Instance()
#player = instance.media_player_new()

#class TonePlayer(object):
 #   
  #  def __init__(self, file_name):
   #     self.file_name = file_name
        
    #def 
        
#tone_player = TonePlayer("/home/pi/Downloads/boing.mp3")
    