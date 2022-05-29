from msilib.schema import Font
import os

from tkinter import ttk
from turtle import title
from tkinter import *
from PIL import ImageTk, Image
from Train import train
from facerecognition import facerec
from attendace import attendance

from Student import Student

class Face_rec_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        # # first img
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\face_header_pc.jpg")
        img=img.resize((800,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=150)

        #top second img
        imgt2=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\bnr_190710_c2qkjz.jpg")
        imgt2=imgt2.resize((750,150),Image.LANCZOS)
        self.photoimgt2=ImageTk.PhotoImage(imgt2)
        f_lbl=Label(self.root,image=self.photoimgt2)
        f_lbl.place(x=800,y=0,width=750,height=150)

        #bg img
        bgimg=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\Background-opera-speeddials-community-web-simple-backgrounds.jpg")
        bgimg=bgimg.resize((1530,640),Image.LANCZOS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=150,width=1530,height=640)

        title_lbl=Label(self.root,text="FACE  RECOGNITION  SYSTEM  SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=150,width=1530,height=45)

        # self.title(bgimg)
        # title.place(x=0,y=0,width=1530,height=45)

         #function button
        def Student_details():
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

        def train_data():
            self.new_window=Toplevel(self.root)
            self.app=train(self.new_window)

        def facerecognition():
            self.new_window=Toplevel(self.root)
            self.app=facerec(self.new_window)

        def attendance_details():
            self.new_window=Toplevel(self.root)
            self.app=attendance(self.new_window)


        def open_img():
            os.startfile("data")
 

        # second img
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\Facial-Recognition-–-Shaping-the-future-of-Identity-Verification-Market-825x500.jpg")
        img2=img2.resize((200,150),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(self.root,command=Student_details,image=self.photoimg2,cursor="hand2")
        b2.place(x=300,y=250,width=200,height=150)
        b2_1=Button(self.root,text="Enroll",command=Student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=300,y=400,width=200,height=50)

        # third img
        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\iStock-925574662.jpg")
        img3=img3.resize((200,150),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root,command=attendance_details,image=self.photoimg3,cursor="hand2")
        b3.place(x=700,y=500,width=200,height=150)
        b3_2=Button(self.root,text="Database",command=attendance_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3_2.place(x=700,y=650,width=200,height=50)

        #fourth img
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\main-banner15.webp")
        img4=img4.resize((200,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(self.root,command=facerecognition,image=self.photoimg4,cursor="hand2")
        b4.place(x=1100,y=250,width=200,height=150)
        b4_2=Button(self.root,text="Attendance",command=facerecognition,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_2.place(x=1100,y=400,width=200,height=50)

        #fifth img
        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\50-506135_gallery-iphone-icon-png-4k-pictures-full-hq.png")
        img5=img5.resize((200,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b5=Button(self.root,image=self.photoimg5,cursor="hand2",command=open_img)
        b5.place(x=300,y=500,width=200,height=150)
        b5_2=Button(self.root,text="Photos",cursor="hand2",command=open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_2.place(x=300,y=650,width=200,height=50)

        #sixth img
        img6=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\21079021.jpg")
        img6=img6.resize((200,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b6=Button(self.root,image=self.photoimg6,cursor="hand2")
        b6.place(x=700,y=250,width=200,height=150)
        b6_2=Button(self.root,text="TRAIN DATA",command=train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6_2.place(x=700,y=400,width=200,height=50)

        #seventh img
        img7=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\349-3492816_crystal-clear-action-exit-icon-shutdown-windows-8 (1).png")
        img7=img7.resize((200,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b7=Button(self.root,image=self.photoimg7,cursor="hand2")
        b7.place(x=1100,y=500,width=200,height=150)
        b7_2=Button(self.root,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_2.place(x=1100,y=650,width=200,height=50)

       
    
        

        



if __name__=="__main__":
    root=Tk()
    obj=Face_rec_system(root)
    root.mainloop()