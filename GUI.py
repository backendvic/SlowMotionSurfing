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
import threading
import imageio
from PIL import Image, ImageTk
import cv2
from queue import Queue
import time

video_name = "C:\\Users\\akoni\\Desktop\\Akoni's school\\CST 205\\Project3\\CST-205-Project3\\Kolohe.MP4" #This is your video file path
video = imageio.get_reader("Kolohe.MP4")

root = Tk() #Main window
root.title('Project 3') # Window title

Fcanvas = Canvas(bg="black", height=250, width=450)
#frame=Frame(bg="black",height=250, width=450)
def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image 

def snd2():
    print("Nothing happens...")
    
def snd3():
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()




var = IntVar()
rb2 = Radiobutton(root, text= "Play Video 1", variable = var, value=1, command=snd2)
rb3 = Radiobutton(root, text= "Play Video 2", variable = var, value=2, command=snd3)
rb2.pack(anchor = W)
rb3.pack(anchor = W)

my_label = Label(root)
my_label.pack()

Fcanvas.pack()
#frame.pack()
root.mainloop()

