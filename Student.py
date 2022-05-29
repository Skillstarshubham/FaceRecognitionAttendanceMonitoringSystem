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



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Enrollment Section")

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

        # Fetch data
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

        # Get cursor
        def get_cursor(event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data="-" * len(content)
            data=content["values"]

            self.var_batch.set(data[0]),
            self.var_department.set(data[1]),
            self.var_section.set(data[2]),
            self.var_reg.set(data[3]),
            self.var_name.set(data[4]),
            self.var_rollno.set(data[5]),
            self.var_gender.set(data[6]),
            self.var_dob.set(data[7]),
            self.var_email.set(data[8]),
            self.var_phone.set(data[9]),
            self.var_address.set(data[10]),
            self.var_r1.set(data[11])

        #update function
        def update_data():
            if self.var_batch.get()=="Select batch" or self.var_name.get()=="" or self.var_reg.get()=="":
                messagebox.showerror("Error","All fiels are required")
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this students detail")
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                        my_cursor=conn.cursor()
                        updatedata="UPDATE student SET Name=%s,Department=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Reg=%s WHERE Section=%s"
                        updt=(self.var_name.get(),self.var_department.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_reg.get(),self.var_section.get(),)
                        my_cursor.execute(updatedata,updt)
                        # updatedata="UPDATE student SET Reg. No.=%s,Department=%s,Section=%s,Name=%s,Roll No.=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s WHERE Section=%s"
                        # updt=(self.var_reg.get(),self.var_department.get(),self.var_section.get(),self.var_name.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_r1.get(),self.var_section.get(),)
                        # my_cursor.execute(updatedata,updt)
                        # my_cursor.execute(("UPDATE student SET Batch=%s,Department=%s,Section=%s,Name=%s,Roll No.=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo=%s WHERE Reg. No.=%s"),(                                                                                                                                                                                                     self.var_batch.get(),
                        #                                                                                                                                                                             self.var_batch.get(),
                        #                                                                                                                                                                             self.var_department.get(),
                        #                                                                                                                                                                             self.var_section.get(),
                        #                                                                                                                                                                             self.var_name.get(),
                        #                                                                                                                                                                             self.var_rollno.get(),
                        #                                                                                                                                                                             self.var_gender.get(),
                        #                                                                                                                                                                             self.var_dob.get(),
                        #                                                                                                                                                                             self.var_email.get(),
                        #                                                                                                                                                                             self.var_phone.get(),
                        #                                                                                                                                                                             self.var_address.get(),
                        #                                                                                                                                                                             self.var_r1.get(),
                        #                                                                                                                                                                             self.var_reg.get()

                        # )) 

                        
                                                                                                                                                                                                 
                    else:
                      if not Update:
                        return
                    messagebox.showinfo("Success","Student details successfully update completed")
                    conn.commit()
                    fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")
        
        #delete function
        def delete_data():
            if self.var_reg.get=="":
                messagebox.showerror("Error","Student id must be required")
            else:
                try:
                  delete=messagebox.askyesno("Student Delete page","Do you want to delete this student details")
                  if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM student where Name=%s"
                    val=(self.var_name.get(),)
                    my_cursor.execute(sql,val)
                  else:
                    if not delete:
                        return
                  conn.commit()
                  fetch_data()
                  conn.close()
                  messagebox.showinfo("Delete","Successfully deleted student details")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")

        def reset_data():
            self.var_batch.set("Select Batch")
            self.var_department.set("Select department")
            self.var_section.set("Select Section")
            self.var_reg.set("")
            self.var_name.set("")
            self.var_rollno.set("")
            self.var_gender.set("")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_r1.set("")

        #generate data set or take photo sample
        def generate_dataset():
            if self.var_batch.get()=="Select batch" or self.var_name.get()=="" or self.var_reg.get()=="":
                messagebox.showerror("Error","All fiels are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                         id+=1
                    updatedata="UPDATE student SET Name=%s,Department=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s WHERE Reg=%s"
                    updt=(self.var_name.get(),self.var_department.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_reg.get()==id,)
                    my_cursor.execute(updatedata,updt) 
                    id=self.var_reg.get()                                                                                                                                                      
                    conn.commit()
                    fetch_data()
                    reset_data()
                    conn.close()

                    # load predifined data on face frontals from opencv
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        rat,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                        face=face_cropped(my_frame)
                        face=cv2.resize(face,(450,450),interpolation=cv2.INTER_AREA)
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                        if cv2.waitKey(1)== ord('q') or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set completed")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")




                    





        


        


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

        title_lbl=Label(self.root,text="ENROLLMENT  SECTION",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=150,width=1530,height=45)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=5,y=200,width=1525,height=590)

        #left label frame
        l_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_frame.place(x=10,y=10,width=750,height=550)

        l_img=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\FACE-RECOGNITION_blog_800x400@1x.png")
        l_img=img.resize((730,150),Image.LANCZOS)
        self.photolimg=ImageTk.PhotoImage(l_img)
        f_lbl=Label(l_frame,image=self.photolimg)
        f_lbl.place(x=10,y=10,width=730,height=130)

        #current cource
        c_c_frame=LabelFrame(l_frame,bd=2,relief=RIDGE,text="Current course",font=("times new roman",15,"bold"),bg="white",fg="black")
        c_c_frame.place(x=10,y=130,width=730,height=115)

        #Batch
        batch=Label(c_c_frame,text="Batch",font=("times new roman",15,"bold"))
        batch.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        batch_combo=ttk.Combobox(c_c_frame,textvariable=self.var_batch,font=("times new roman",15,"bold"),width=17,state="read only")
        batch_combo["values"]=("Select Batch","2018-2022","2019-2023","2020-2024","2021-2025")
        batch_combo.current(0)
        batch_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Department
        department=Label(c_c_frame,text="Department",font=("times new roman",15,"bold"))
        department.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(c_c_frame,textvariable=self.var_department,font=("times new roman",15,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer science","Information Technology","Electronics","Electrical","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #Section
        section=Label(c_c_frame,text="Section",font=("times new roman",15,"bold"))
        section.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        sec_combo=ttk.Combobox(c_c_frame,textvariable=self.var_section,font=("times new roman",15,"bold"),width=17,state="read only")
        sec_combo["values"]=("Select Section","A","B","C","D","E","F")
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #Class Student info.
        info_frame=LabelFrame(l_frame,bd=2,relief=RIDGE,text="Student information",font=("times new roman",15,"bold"),bg="white",fg="black")
        info_frame.place(x=10,y=245,width=730,height=210)

        #Student Id
        id=Label(info_frame,text="Reg",font=("times new roman",15,"bold"))
        id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(info_frame,textvariable=self.var_reg,width=18,font=("times new roman",15,"bold"))
        id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Name
        name_=Label(info_frame,text="Student Name",font=("times new roman",15,"bold"))
        name_.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(info_frame,textvariable=self.var_name,width=18,font=("times new roman",15,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Roll no.
        roll=Label(info_frame,text="Roll",font=("times new roman",15,"bold"))
        roll.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(info_frame,textvariable=self.var_rollno,width=18,font=("times new roman",15,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Gender
        gender_=Label(info_frame,text="Gender",font=("times new roman",15,"bold"))
        gender_.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(info_frame,textvariable=self.var_gender,width=18,font=("times new roman",15,"bold"))
        gender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #DOB
        dob_=Label(info_frame,text="DOB",font=("times new roman",15,"bold"))
        dob_.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(info_frame,textvariable=self.var_dob,width=18,font=("times new roman",15,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Email
        mail_=Label(info_frame,text="Email ID",font=("times new roman",15,"bold"))
        mail_.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(info_frame,textvariable=self.var_email,width=18,font=("times new roman",15,"bold"))
        mail_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #phone no.
        phone_=Label(info_frame,text="Phone No.",font=("times new roman",15,"bold"))
        phone_.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(info_frame,textvariable=self.var_phone,width=18,font=("times new roman",15,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #address
        add_=Label(info_frame,text="Address",font=("times new roman",15,"bold"))
        add_.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(info_frame,textvariable=self.var_address,width=18,font=("times new roman",15,"bold"))
        add_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        radiobutton1=Radiobutton(info_frame,variable=self.var_r1,text="Take photo Sample",value="Yes")
        radiobutton1.grid(row=4,column=0)

        radiobutton2=Radiobutton(info_frame,variable=self.var_r1,text="No photo Sample",value="No")
        radiobutton2.grid(row=4,column=1)

        #function declaration
        def add_data():
            if self.var_batch.get()=="Select batch" or self.var_name.get()=="" or self.var_reg.get()=="":
                messagebox.showerror("Error","All fiels are required")
            else:
                 try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_batch.get(),
                                                                                                            self.var_department.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_reg.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_r1.get()
                                                                                                          ))     
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Successful")
                 except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")
                    #  (Batch,Department,Section,Reg. No.,Name,Roll No.,Gender,DOB,Email,Phone,Address,Photo)

        #button frame
        btn_frame=Frame(l_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=455,width=750,height=35)

        save_btn=Button(btn_frame,text="Save",command=add_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=update_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=delete_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=reset_data,width=15,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         #button frame 2
        btn_frame2=Frame(l_frame,bd=2,relief=RIDGE)
        btn_frame2.place(x=0,y=490,width=760,height=35)

        photosample_btn=Button(btn_frame2,text="Take a photo sample",command=generate_dataset,width=30,font=("times new roman",15,"bold"),bg="blue",fg="white")
        photosample_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame2,text="Update photo sample",width=30,font=("times new roman",15,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=1)

        



        #Right label frame
        r_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",15,"bold"),bg="white",fg="black")
        r_frame.place(x=760,y=10,width=750,height=580)

        r_img=Image.open(r"C:\Users\HP\OneDrive\Desktop\image\FACE-RECOGNITION_blog_800x400@1x.png")
        r_img=img.resize((730,150),Image.LANCZOS)
        self.photorimg=ImageTk.PhotoImage(r_img)
        f_lbl=Label(r_frame,image=self.photorimg)
        f_lbl.place(x=10,y=10,width=730,height=130)

        # Search System
        search_frame=LabelFrame(r_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",15,"bold"),bg="white",fg="black")
        search_frame.place(x=10,y=130,width=730,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",15,"bold"),width=10,state="read only")
        search_combo["values"]=("Select","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=11,font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        see_all_btn=Button(search_frame,text="See All",width=11,font=("times new roman",15,"bold"),bg="blue",fg="white")
        see_all_btn.grid(row=0,column=4,padx=5)

        # Table frame
        table_frame=LabelFrame(r_frame,bd=2,relief=RIDGE,text="Table ")
        table_frame.place(x=10,y=200,width=730,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Batch","Department","Section","Reg","Name","Roll","Gender","DOB","Email id","Phone no.","Address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Reg",text="Registration No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll",text="Roll no.")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email id",text="Email id")
        self.student_table.heading("Phone no.",text="Phone no.")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("photo",text="photo")
        
        self.student_table["show"]="headings"
        self.student_table.column("Batch",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Reg",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email id",width=100)
        self.student_table.column("Phone no.",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",get_cursor)
        fetch_data()
        

        # #function declaration
        # def add_data(self):
        #     if self.var_batch.get()=="Select batch" or self.name_.get()=="" or self.id.get()=="":
        #         messagebox.showerror("Error","All fiels are required",parrent=self.root)
        #     else:
        #         messagebox.showinfo("Successful","Done",parrent=self.root)

        # Fetch data
        # def fetch_data(self):
        #     conn=mysql.connector.connect(host="localhost",username="root",password="Kumar2003@",database="facerecognition")
        #     my_cursor=conn.cursor()
        #     my_cursor.execute("select* from student")
        #     data=my_cursor.fetchall()

        #     if len(data)!=0:
        #         self.student_table.delete(*self.student_table.get_children())
        #         for i in data:
        #             self.student_table.insert("",END,Values=i)
        #         conn.commit()
        #     conn.close()
        













if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()       