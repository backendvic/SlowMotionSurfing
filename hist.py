import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('C:/dev/Project3_CST231_Team43/histogram/Kolohe.mp4')# may want to not have this hard coded
ret, frame = cap.read()
count = 0
list = []
while(ret and count < 470):
    ret, frame = cap.read()
    count+=1
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, frame) = cv2.threshold(frame, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # instead of doing histogram stuff we could calculate the average color of a region of our frame
    # at this point frame is a black and white image of our video
	# 130, 175, 220 are the frames we ideally want assuming 15 fps
    sum = 0
    average = 0
    for y in range(250):#caps at 720 y val
        for x in range(700):# caps at 1280 x val
            if frame[y,x] > 0:
                sum += frame[y,x]
    average = sum / (250*700)
    #print(count, average)
    if average > 50:
        list.append(count)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
# based on the video we know that we dont want the frames with the foreground whitewater skewing the average    
for x in list:
    if x > 240:
        list.remove(x)
magic = 0
listcount = 0
betterlist = []
#print(list)
#we need to convert our list values to 3 frame numbers
for x in range(len(list)-1):
    if list[x+1] - list[x] < 20:
        magic += list[x]
        listcount += 1
    elif x+1 == len(list):
        magic+=list[len(list)-1]
        listcount += 1
    else:
        betterlist.append(int(magic/listcount))
        magic = 0
        listcount = 0

cap.release()
print(betterlist)
#return betterlist
