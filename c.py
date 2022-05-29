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

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Student portal")

        #variable
        self.var_batch=StringVar()
        self.var_department=StringVar()
        self.var_section=StringVar()
        self.var_reg=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_r1=StringVar()

        def fetch_data():
            conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()


        def update_data():
            if self.var_batch.get()=="Select batch" or self.var_name.get()=="" or self.var_reg.get()=="":
                messagebox.showerror("Error","All fiels are required")
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this students detail")
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                        my_cursor=conn.cursor()
                        my_cursor.execute(("UPDATE student SET Batch=%s,Department=%s,Section=%s,Name=%s,Roll No.=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s WHERE Reg. No.=%s"),(                                                                                                                                                                                                     self.var_batch.get(),
                                                                                                                                                                                                    self.var_batch.get(),
                                                                                                                                                                                                    self.var_department.get(),
                                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                    self.var_rollno.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                    self.var_r1.get(),
                                                                                                                                                                                                    self.var_reg.get()
                        ))

                        
                                                                                                                                                                                                 
                    else:
                      if not Update:
                        return
                    messagebox.showinfo("Success","Student details successfully update completed")
                    conn.commit()
                    fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")


        b2_1=Button(self.root,text="Update data",cursor="hand2",command=update_data,font=("times new roman",45,"bold"),bg="green",fg="white")
        b2_1.place(x=300,y=400,width=930,height=50)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()     