print("Project 3")
print("SURF")
"""
Team 43
Victor
Cody
Akoni
"""

import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2


cap=cv2.VideoCapture("testmaster.MP4")


root = Tk() #Main window
root.geometry('500x400')
root.title('Project 3') # Window title

Fcanvas = Canvas(bg="black", height=350, width=450)

def snd1():
    image = 'Surf'
    
    while cap.isOpened():
        ret, frame = cap.read()
      #  cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.imshow('image', frame)
        #cv2.resizeWindow('frame', 580,720)
        
        
        if  cv2.waitKey(26) & 0xFF == ord('q'):
            break
        
def snd2():
    filename = askopenfilename()

    file = cv2.VideoCapture(filename)

    while file.isOpened():
        ret, fra = file.read()
        cv2.imshow('Video', fra)
        if cv2.waitKey(26) & 0xFF == ord('q'):
            break
    file.release()


but=Button(root, text="Play Surf Video")
but.config(command=snd1)
but.pack(anchor = CENTER)

but2=Button(root, text="Play Different Video")
but2.config(command=snd2)
but2.pack(anchor = CENTER)

"""
rb1 = Radiobutton(root, text= "Play Surf Video", variable = var, value=1, command=snd1)
rb2 = Radiobutton(root, text= "Play Different Video", variable = var, value=2, command=snd2)

rb1.pack(anchor = W)
rb2.pack(anchor = W)
"""


#Fcanvas.pack()
root.mainloop()
cap.release()
cv2.destroyAllWindows()
