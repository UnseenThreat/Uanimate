import cv2
import numpy as np
import time

def main():
	cap = cv2.VideoCapture(0)
	print(cap.isOpened())
	while(True):
		ret, frame=cap.read();
		cv2.imshow('image', frame)
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()