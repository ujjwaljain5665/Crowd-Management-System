from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk
import os
from Team import Team
from project import project

class homepage:
    def __init__(self,window):

        # window
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.title("CMS")
        
        # Bg image
        bg=Image.open("Images/bg1.jpg")
        bg=bg.resize((1280,720),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        # top frame
        self.f1=Frame(self.window,bg="white")
        self.f1.place(x=0,y=40,relwidth=1,height=200)
        # top frame -> first image
        img=Image.open("Images/bg.jpg")
        img=img.resize((300,200),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)
        imglbl=Label(self.f1,image=self.img).place(x=30,y=0,width=300,height=200)
        # top frame -> Heading
        heading=Label(self.f1,text="Crowd Management System",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=400,y=50)

        # Buttons
        # Monitor_Button
        btn_img1=Image.open("Images/dashboard.jpg")
        btn_img1=btn_img1.resize((160,120),Image.ANTIALIAS)
        self.btn_img1=ImageTk.PhotoImage(btn_img1)
        b1=Button(self.window,image=self.btn_img1,command=self.CMS,cursor="hand2").place(x=240,y=350,width=160,height=120)
        b1_1=Button(self.window,text="Monitor",command=self.CMS,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=240,y=470,width=160,height=40)

        # About_Project_Button
        btn_img2=Image.open("Images/about.jpg")
        btn_img2=btn_img2.resize((160,120),Image.ANTIALIAS)
        self.btn_img2=ImageTk.PhotoImage(btn_img2)
        b2=Button(self.window,image=self.btn_img2,command=self.about_project,cursor="hand2").place(x=450,y=350,width=160,height=120)
        b2_2=Button(self.window,text="About Project",command=self.about_project,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=450,y=470,width=160,height=40)

        # ABout_Team_Button
        btn_img3=Image.open("Images/team.jpg")
        btn_img3=btn_img3.resize((160,120),Image.ANTIALIAS)
        self.btn_img3=ImageTk.PhotoImage(btn_img3)
        b3=Button(self.window,image=self.btn_img3,command=self.about_team,cursor="hand2").place(x=660,y=350,width=160,height=120)
        b3_3=Button(self.window,text="About team",command=self.about_team,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=660,y=470,width=160,height=40)

        # Exit_Button
        btn_img4=Image.open("Images/exit.jpg")
        btn_img4=btn_img4.resize((160,120),Image.ANTIALIAS)
        self.btn_img4=ImageTk.PhotoImage(btn_img4)
        b4=Button(self.window,image=self.btn_img4,command=self.windexit,cursor="hand2").place(x=870,y=350,width=160,height=120)
        b4_4=Button(self.window,text="Exit",command=self.windexit,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=870,y=470,width=160,height=40)

    # to open about project window
    def about_project(self):
        self.new_window=Toplevel(self.window)
        self.new=project(self.new_window)

    # to open about team window
    def about_team(self):
        self.new_window=Toplevel(self.window)
        self.new=Team(self.new_window)

    # to open monitoring window
    def CMS(self):
        os.system("cms.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel")

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("CMS","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=homepage(window)
    window.mainloop()