from tkinter import * 
import time
from tkinter import ttk,messagebox
import math
from PIL import Image,ImageTk
from tkinter.constants import TRUE
import pymysql
from homepage import homepage

class login:
    #login window
    def __init__(self,window):
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.config(bg="black")
        self.window.title("Login Window CMS")
        # bg
        leftbg=Label(self.window,bg="#08A3D2",bd=0)
        leftbg.place(x=0,y=0,relheight=1,width=500)
        rightbg=Label(self.window,bg="#031F3C",bd=0)
        rightbg.place(x=500,y=0,relheight=1,relwidth=1)

        #login frame
        loginframe=Frame(self.window,bg="white")
        loginframe.place(x=370,y=70,width=800,height=500)
        
        # heading
        title=Label(loginframe,text="Login Here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=400,y=10)
        
        # user logo
        self.user = PhotoImage(file='Images/test.png')
        label = Label(loginframe, image = self.user).place(x=450,y=100)
        
        #row-1
        password=Label(loginframe,text="Password",font=("times new roman",25,"bold"),bg="white",fg="grey").place(x=365,y=250)
        self.text_pass=Entry(loginframe,font=("times new roman",15),bg="lightgrey",show='*')
        self.text_pass.place(x=370,y=300,width=300,height=30)
        
        # login butn
        self.logbtn=ImageTk.PhotoImage(file="Images/log.jpg")
        btnlog=Button(loginframe,image=self.logbtn,bg="white",command=self.log_in,bd=0,cursor="hand2").place(x=370,y=370)

        #canvas
        self.canvas = Canvas(self.window, width=365, height=370,bg="black",bd=0,relief='ridge',highlightthickness=0)
        self.canvas.place(x=200,y=140)

        # clocktitle=Label(self.canvas,text="Developer's Clock",font=("times new roman",25,"bold"),bg="white",fg="red").place(x=80,y=4)
        
        # clock image
        self.bg = PhotoImage(file='Images/clock.png')
        self.canvas.create_image(180, 180, image=self.bg)

        # create clock hands
        self.center_x = 180
        self.center_y = 180

        self.seconds_hand_len = 95
        self.minutes_hand_len = 80
        self.hours_hand_len = 60

        # seconds hand
        self.seconds_hand = self.canvas.create_line(200, 200, 200 + self.seconds_hand_len, 200 + self.seconds_hand_len, width=1.5, fill='red')
        # minutes hand
        self.minutes_hand = self.canvas.create_line(200, 200, 200 + self.minutes_hand_len, 200 + self.minutes_hand_len, width=2, fill='white')
        # hours hand
        self.hours_hand = self.canvas.create_line(200, 200, 200 + self.hours_hand_len, 200 + self.hours_hand_len, width=4, fill='white')

        self.update_clock()
        
    #login validation
    def log_in(self):
        if self.text_pass.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.window)
        elif self.text_pass.get()!="password":
            messagebox.showerror("Error","Wrong Password...\n If u think it is an error, try contacting Admin.",parent=self.window)
        else:
            messagebox.showerror("Success","Logged In Successfully")
            self.new=homepage(self.window)
        
    #clock update
    def update_clock(self):
        self.hours = int(time.strftime("%I"))
        self.minutes = int(time.strftime("%M"))
        self.seconds = int(time.strftime("%S"))

        self.am_or_pm = time.strftime("%p") # for digi
        # updating seconds hand
        self.seconds_x = self.seconds_hand_len * math.sin(math.radians(self.seconds * 6)) + self.center_x
        self.seconds_y = -1 * self.seconds_hand_len * math.cos(math.radians(self.seconds * 6)) + self.center_y
        self.canvas.coords(self.seconds_hand, self.center_x, self.center_y, self.seconds_x, self.seconds_y)

        # updating minutes hand
        self.minutes_x = self.minutes_hand_len * math.sin(math.radians(self.minutes * 6)) + self.center_x
        self.minutes_y = -1 * self.minutes_hand_len * math.cos(math.radians(self.minutes * 6)) + self.center_y
        self.canvas.coords(self.minutes_hand, self.center_x, self.center_y, self.minutes_x, self.minutes_y)

        # updating hours hand
        self.hours_x = self.hours_hand_len * math.sin(math.radians(self.hours * 30 + self.minutes * 0.5)) + self.center_x  #self.hours * 30
        self.hours_y = -1 * self.hours_hand_len * math.cos(math.radians(self.hours * 30 + self.minutes * 0.5)) + self.center_y  #self.hours * 30
        self.canvas.coords(self.hours_hand, self.center_x, self.center_y, self.hours_x, self.hours_y)
        
        self._job=self.window.after(1000, self.update_clock)
        
if __name__=="__main__":
    window = Tk()
    ob=login(window)
    window.mainloop()