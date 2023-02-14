from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os


class Team:
    def __init__(self,window):
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.config(bg="black")
        self.window.title("About Team")

        title=Label(window,text="About Team Members",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=430,y=30)
        
        self.f1=Frame(self.window,bg="white")
        self.f1.place(x=0,y=110,relwidth=1,height=470)
        
        bg=Image.open("Images/team_dp.jpg")
        bg=bg.resize((160,120),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        
        t1=Label(self.f1,image=self.bg).place(x=50,y=50)
        t2=Label(self.f1,image=self.bg).place(x=700,y=50)
        t3=Label(self.f1,image=self.bg).place(x=50,y=300)
        t4=Label(self.f1,image=self.bg).place(x=700,y=300)
        
        heading1=Label(self.f1,text="Name - Ujjwal Jain\nRoll No - 1918777\nSection - B",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=230,y=70)
        heading2=Label(self.f1,text="Name - Rahul Walia\nRoll No - 1918587\nSection - I",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=880,y=70)
        heading3=Label(self.f1,text="Name - Shivansh Mehrotra\nRoll No - 1918705\nSection - J",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=230,y=320)
        heading4=Label(self.f1,text="Name - Garvit Tyagi\nRoll No - 1918831\nSection - K",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=880,y=320)

        

        


if __name__ == "__main__":
    window=Tk()
    obj=Team(window)
    window.mainloop()