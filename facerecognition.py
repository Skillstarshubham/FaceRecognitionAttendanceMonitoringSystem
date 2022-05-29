from ast import Return
from cProfile import label
from msilib.schema import Font
from optparse import Values
from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
#from tkinter import _XYScrollCommand
from turtle import title, width
# from typing_extensions import Self
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class facerec():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")

        # #attendance
        # def mark_attendance():
        #     with open("shubham.csv","r+",newline="\n") as f:
        #         myDatalist=f.readlines()
        #         name_list=[]
        #         for line in myDatalist:
        #             entry=line.split((","))
        #             name_list.append(entry[0])
        #         if((i not in name_list) and (r not in name_list) and (b not in name_list) and (n not in name_list))

        def face_recog():
            def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int(100*(1-predict/300))

                    conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select Name from student where Reg="+str(id))
                    n=my_cursor.fetchone()
                    

                    my_cursor.execute("select Roll from student where Reg="+str(id))
                    r=my_cursor.fetchone()
                    # r="+".join(r)

                    my_cursor.execute("select Department from student where Reg="+str(id))
                    b=my_cursor.fetchone()
                    # b="+".join(b)

                    my_cursor.execute("select Reg from student where Reg="+str(id))
                    i=my_cursor.fetchone()
                    # i="+".join(i)

                    if confidence>77:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        #cv2.putText(img,"known face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{b}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Reg:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        mark_attendance(n,r,b,i)


                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,h,w,y]

                return coord

            def recognize(img,clf,facecascade):
                coord=draw_boundry(img,facecascade,1.1,10,(255,25,255),"Face",clf)
                return img

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img2=video_cap.read()
                img2=recognize(img2,clf,faceCascade)
                cv2.imshow("Welcome To face REcognition",img2)

                if cv2.waitKey(1)==ord('q'):
                    break
            video_cap.release()
            cv2.destroyAllWindows()

        #attendance
        def mark_attendance(n,r,b,i):
            with open("shubham.csv","r+",newline="\n") as f:
                myDatalist=f.readlines()
                name_list=[]
                for line in myDatalist:
                    entry=line.split((","))
                    name_list.append(entry[0])
                if n not in name_list:
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{n},{r},{b},{i},{dtString},{d1},present")

         #bg img
        bgimg=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\Background-opera-speeddials-community-web-simple-backgrounds.jpg")
        bgimg=bgimg.resize((1530,640),Image.LANCZOS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=150,width=1530,height=640)


        title_lbl=Label(self.root,text="Face    Recognition",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        b2_1=Button(self.root,text="Face recognition",cursor="hand2",command=face_recog,font=("times new roman",35,"bold"),bg="green",fg="white")
        b2_1.place(x=300,y=400,width=930,height=50)







if __name__=="__main__":
    root=Tk()
    obj=facerec(root)
    root.mainloop()     