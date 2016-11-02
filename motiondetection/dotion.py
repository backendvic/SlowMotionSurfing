import argparse
import datetime
import imutils
import time
import cv2
vath = "/home/vixmix91/Desktop/OpenCV_PlayGround/Kolohe.mp4"

ap=argparse.ArgumentParser()
ap.add_argument("-v","--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type = int, default=500, help = "minimum area size")
args = vars(ap.parse_args())

camera = cv2.VideoCapture(args["video"])
#camera = cv2.VideoCapture(0)
firstFrame=None

fNumber = 0

while True:
	(grabbed, frame) = camera.read()
	text="unoccupied"
	
	if not grabbed:
		break
	
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	
	
	
	if firstFrame is None:
		firstFrame=gray	


	(grabbed, frame) = camera.read()
	text="unoccupied"

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	thresh = cv2.dilate(thresh,None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for c in cnts:

		if cv2.contourArea(c) < args["min_area"]:
			continue
		
		(x,y,w,h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
		text = "occupied"
	cv2.imwrite("Output" + str(fNumber) + ".png", thresh)
	fNumber += 1