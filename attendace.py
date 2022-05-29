from cProfile import label
from msilib.schema import Font
from optparse import Values
from tkinter import*
from tkinter import ttk
#from tkinter import _XYScrollCommand
from turtle import title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Attendance portal")




         # # first img
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\depositphotos_68789187-stock-photo-students.jpg")
        img=img.resize((500,150),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #top second img
        imgt2=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\education-horizontal-typography-banner-set-with-learning-knowledge-symbols-flat-illustration_1284-29493.jpg")
        imgt2=imgt2.resize((550,150),Image.LANCZOS)
        self.photoimgt2=ImageTk.PhotoImage(imgt2)
        f_lbl=Label(self.root,image=self.photoimgt2)
        f_lbl.place(x=500,y=0,width=550,height=150)

         #top third img
        imgt3=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\depositphotos_12658125-stock-photo-smiling-teenager-students.jpg")
        imgt3=imgt3.resize((500,150),Image.LANCZOS)
        self.photoimgt3=ImageTk.PhotoImage(imgt3)
        f_lbl=Label(self.root,image=self.photoimgt3)
        f_lbl.place(x=1050,y=0,width=500,height=150)

        #bg img
        bgimg=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\abstract_smooth_wave_background_vector_grapihic_art_569579.jpg")
        bgimg=bgimg.resize((1530,640),Image.LANCZOS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)
        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=150,width=1530,height=640)

        title_lbl=Label(self.root,text="ATTENDANCE     PORTAL",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=150,width=1530,height=45)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=5,y=200,width=1525,height=590)

        #left label frame
        l_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance details",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_frame.place(x=10,y=10,width=750,height=550)

        #Student Id
        id=Label(l_frame,text="Attendance Id",font=("times new roman",15,"bold"))
        id.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(l_frame,width=18,font=("times new roman",15,"bold"))
        id_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        name_=Label(l_frame,text="Student Name",font=("times new roman",15,"bold"))
        name_.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(l_frame,width=18,font=("times new roman",15,"bold"))
        name_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Roll no.
        roll=Label(l_frame,text="Roll",font=("times new roman",15,"bold"))
        roll.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(l_frame,width=18,font=("times new roman",15,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
        department=Label(l_frame,text="Department",font=("times new roman",15,"bold"))
        department.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(l_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer science","Information Technology","Electronics","Electrical","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #Date
        date_=Label(l_frame,text="Date",font=("times new roman",15,"bold"))
        date_.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(l_frame,width=18,font=("times new roman",15,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Time
        time_=Label(l_frame,text="Time",font=("times new roman",15,"bold"))
        time_.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(l_frame,width=18,font=("times new roman",15,"bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance status
        attendace_status=Label(l_frame,text="Attendance status",font=("times new roman",15,"bold"))
        attendace_status.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendace_status_combo=ttk.Combobox(l_frame,font=("times new roman",15,"bold"),width=17,state="read only")
        attendace_status_combo["values"]=("Status","Present","Absent")
        attendace_status_combo.current(0)
        attendace_status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #button frame
        btn_frame=Frame(l_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=455,width=750,height=35)

        save_btn=Button(btn_frame,text="Import csv",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)









        #Right label frame
        r_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance",font=("times new roman",15,"bold"),bg="white",fg="black")
        r_frame.place(x=760,y=10,width=750,height=570)

        table_frame=LabelFrame(r_frame,bd=2,relief=RIDGE,text="Attendace table",font=("times new roman",15,"bold"),bg="white",fg="black")
        table_frame.place(x=10,y=10,width=730,height=530)

        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AtteendanceReportTable=ttk.Treeview(table_frame,column=("Department","Attendance Id","Name","Roll no","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AtteendanceReportTable.xview)
        scroll_y.config(command=self.AtteendanceReportTable.yview)

        self.AtteendanceReportTable.heading("Department",text="Department")
        self.AtteendanceReportTable.heading("Attendance Id",text="Attendace Id")
        self.AtteendanceReportTable.heading("Name",text="Name")
        self.AtteendanceReportTable.heading("Roll no",text="Roll no")
        self.AtteendanceReportTable.heading("Time",text="Time")
        self.AtteendanceReportTable.heading("Date",text="Date")
        self.AtteendanceReportTable.heading("Status",text="Status")

        self.AtteendanceReportTable["show"]="headings"
        self.AtteendanceReportTable.column("Department",width=100)
        self.AtteendanceReportTable.column("Attendance Id",width=100)
        self.AtteendanceReportTable.column("Name",width=100)
        self.AtteendanceReportTable.column("Roll no",width=100)
        self.AtteendanceReportTable.column("Time",width=100)
        self.AtteendanceReportTable.column("Date",width=100)
        self.AtteendanceReportTable.column("Status",width=100)
        

        self.AtteendanceReportTable.pack(fill=BOTH,expand=1)


if __name__=="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()    