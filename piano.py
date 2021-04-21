#made with the help of https://pyshine.com/How-to-play-piano-using-Python/

from threading import Thread
import pygame as pg
import time

def play_notes(notePath,duration):
	time.sleep(duration)
	pg.mixer.Sound(notePath).play()
	time.sleep(duration)
	print(notePath)

def play_song(note_list):
	pg.mixer.init()
	pg.init()
	pg.mixer.set_num_channels(len(note_list))

	path  = 'Sounds/'

	cnt =1

	th = {}


	for t in note_list:
		th[t] = Thread(target = play_notes,args = (path+'{}.ogg'.format(t),0.3))
		th[t].start()
		th[t].join()
		if cnt%7==0:
			time.sleep(1)
		cnt+=1

