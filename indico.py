import pygame
import pygame.camera
import time
import indicoio
import os

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1920,1080))
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
		
		for i in range(0,int(len(dict))):
			if(dict[i]['bottom_right_corner'][0]-dict[i]['top_left_corner'][0] > 60000 or dict[i]['bottom_right_corner'][1]-dict[i]['top_left_corner'][1] > 60000 or dict[i]['top_left_corner'][0] > 60000 or dict[i]['top_left_corner'][1] > 60000):
				continue;
			crop_rect = (dict[i]['top_left_corner'][0], dict[i]['top_left_corner'][1], abs(dict[i]['bottom_right_corner'][0]-dict[i]['top_left_corner'][0]), 
																					   abs(dict[i]['bottom_right_corner'][1]-dict[i]['top_left_corner'][1]))
			cropped = image.subsurface(crop_rect)
			pygame.image.save(cropped, str(foo)+"cropped"+str(c_id)+".jpg")

			os.rename("/home/lx_user/Documents/programming/web/uanimate/"+str(foo)+"cropped"+str(c_id)+".jpg", "/home/lx_user/Documents/programming/web/uanimate/test/"+str(foo)+"cropped"+str(c_id)+".jpg")
			c_id+=1
		
		foo+=1
	except (RuntimeError, TypeError, NameError, ValueError, IndexError, IOError):
		print("wtf")


for i in range(0,40):
	time.sleep(1)
	capture()