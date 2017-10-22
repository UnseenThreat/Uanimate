import pygame
import pygame.camera
import time
import indicoio
import os
import re

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1280,720))
cam.start()
foo = 0
indicoio.config.api_key = "73367ede6573be5444c62bc56a4beaf1"

def capture():
	try:
		global foo
		img = cam.get_image()
		pygame.image.save(img,"test"+str(foo)+".jpg")
		os.rename("/home/lx_user/Documents/programming/web/uanimate/test"+str(foo)+".jpg", "/home/lx_user/Documents/programming/web/uanimate/test/test"+str(foo)+".jpg")
		dict=indicoio.facial_localization("/home/lx_user/Documents/programming/web/uanimate/test/test"+str(foo)+".jpg")

		image = pygame.image.load("/home/lx_user/Documents/programming/web/uanimate/test/test"+str(foo)+".jpg")
		
		c_id = 0
		
		#fear is disgust
		happy = 0.0 
		sad = 0.0 
		angry = 0.0 
		fear = 0.0 
		surprise = 0.0 
		neutral = 0.0
		total = 0.0

		for i in range(0,int(len(dict))):
			if(dict[i]['bottom_right_corner'][0]-dict[i]['top_left_corner'][0] > 60000 or dict[i]['bottom_right_corner'][1]-dict[i]['top_left_corner'][1] > 60000 or dict[i]['top_left_corner'][0] > 60000 or dict[i]['top_left_corner'][1] > 60000):
				continue;
			crop_rect = (dict[i]['top_left_corner'][0], dict[i]['top_left_corner'][1], abs(dict[i]['bottom_right_corner'][0]-dict[i]['top_left_corner'][0]), 
																					   abs(dict[i]['bottom_right_corner'][1]-dict[i]['top_left_corner'][1]))
			cropped = image.subsurface(crop_rect)
			pygame.image.save(cropped, str(foo)+"cropped"+str(c_id)+".jpg")

			# code for the emotion
			results=indicoio.fer(str(foo)+"cropped"+str(c_id)+".jpg")
			# print(results)

			if('Happy' in results):
				happy += results['Happy']
			if('Sad' in results):
				sad   += results['Sad']
			if('Angry' in results):
				angry += results['Angry']
			if('Fear' in results):
				fear  += results['Fear']
			if('Surprise' in results):
				surprise += results['Surprise']
			if('Neutral' in results):
				neutral  += results['Neutral']
			total    += (happy + sad + angry + fear + surprise + neutral)

			os.rename("/home/lx_user/Documents/programming/web/uanimate/"+str(foo)+"cropped"+str(c_id)+".jpg", "/home/lx_user/Documents/programming/web/uanimate/test/"+str(foo)+"cropped"+str(c_id)+".jpg")
			c_id+=1
		
		#open the file for reading:
		file = open('/home/lx_user/Documents/programming/web/uanimate/results.txt','w')
		#convert to string:
		file.write(str(happy)+" "+str(sad)+" "+str(angry)+" "+str(fear)+" "+str(surprise)+" "+str(neutral)+" "+str(total))
		file.close()
		foo+=1
	except (RuntimeError, TypeError, NameError, ValueError, IndexError, IOError, KeyError):
		print("wtf")


for i in range(0,100):
	time.sleep(1)
	capture()