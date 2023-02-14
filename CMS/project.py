from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import tkinter as tk

class project:
    def __init__(self,window):
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.config(bg="black")
        self.window.title("About Project")
        T = Text(window, height = 18, width = 85, bg="white", fg="#08A3D2", bd=4, font=("times new roman",20,"bold"))
        T.pack()
        T.place(x=35,y=50)
        data="Crowd Management:\n\nThe act of assisting and controlling big crowds on your ship while maintaining passenger calm during emergencies or chaotic situations is known as crowd management.\nCrowd management stands for the decisions and actions taken to supervise and control densely populated spaces and it involves multiple challenges, from recognition and assessment to application of actions tailored to the current situation\n\n******Requirements:******\nIDE: Visual Studio Code\nLANGUAGE: Python\n***Various Python Libraries like Opencv, Tkinter, Pygame...etc.\n\nSSD:\nWe are using a SSD (Single Shot Detector) with a MobileNet architecture. In general, it only takes a single shot to detect whatever is in an image. That is, one for generating regionproposals, one for detecting the object of each proposal.Compared to other 2 shot detectors like R-CNN, SSD is quite fast.MobileNet, as the name implies, is a DNN designed to run on resource constrained devices. For example, mobiles, ip cameras, scanners etc.Thus, SSD seasoned with a MobileNet should theoretically result in a faster, more efficient object detector.\n\nCentroid Tracker:\nCentroid tracker is one of the most reliable trackers out there.To be straightforward, the centroid tracker computes the centroid of the bounding boxes.That is, the bounding boxes are (x, y) co-ordinates of the objects in an image.Once the co-ordinates are obtained by our SSD, the tracker computes the centroid (center) of the box. In other words, the center of an object.Then an unique ID is assigned to every particular object deteced, for tracking over the sequence of frames."
        T.insert(tk.END, data)
        
        
        
if __name__ == "__main__":
    window=Tk()
    obj=project(window)
    window.mainloop()