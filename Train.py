from cProfile import label
from msilib.schema import Font
from optparse import Values
from tkinter import*
from tkinter import ttk
#from tkinter import _XYScrollCommand
from turtle import title, width
# from typing_extensions import Self
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Train Data")

        def train_classifier():
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L')
                imagenp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imagenp)
                ids.append(id)
                cv2.imshow("Training",imagenp)
                cv2.waitKey(1)==13
        
            ids=np.array(ids)

        # train the classifier
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("result","training is done")

        title_lbl=Label(self.root,text="TRAIN     DATA",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # b2=Button(self.root,image=self.photoimg2,cursor="hand2")
        # b2.place(x=300,y=250,width=200,height=150)
        b2_1=Button(self.root,text="Train      data",cursor="hand2",command=train_classifier,font=("times new roman",45,"bold"),bg="green",fg="white")
        b2_1.place(x=300,y=400,width=930,height=50)

    # def train_classifier():
    #     data_dir=("data")
    #     path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    #     faces=[]
    #     ids=[]

    #     for image in path:
    #         img=Image.open(image).convert('L')
    #         imagenp=np.array(img,'uint8')
    #         id=int(os.path.split(image)[1].split('.'[1]))

    #         faces.append(imagenp)
    #         ids.append(id)
    #         cv2.imshow("Training",imagenp)
    #         cv2.waitKey(1)==13
        
    #     ids=np.array(ids)

    #     # train the classifier
    #     clf=cv2.face.LBPHFaceRecognizer_create()
    #     clf.train(faces,ids)
    #     clf.write("classifier.xml")
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("result","training is done")












if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()     