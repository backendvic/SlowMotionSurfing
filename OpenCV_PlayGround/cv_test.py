import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#img = cv2.imread("bottomturn1.jpg")


#faces = face_cascade.detectMultiScale(img, 1.3, 5)

#for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #roi_color = img[y:y+h, x:x+w]

#cv2.imshow('image', img)
#cv2.waitKey()


body_cascade = cv2.CascadeClassifier('cascades/haarcascade_upperbody.xml')
img = cv2.imread("bottomturn1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = body_cascade .detectMultiScale(gray, 1.1, 8)

for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]
cv2.imshow('image', img)
cv2.waitKey()
