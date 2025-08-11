from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # ==========variables===============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()




        img1 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\face-recognition.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\smart-attendance.jpg")
        img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=500, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\clg.jpg")
        img3 = img3.resize((480, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=1050, y=0, width=480, height=130)

        img4 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\bg2.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Times New Roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img5 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\student.jpeg")
        img5 = img5.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_img5 = Label(Left_frame, image=self.photoimg5)
        lbl_img5.place(x=5, y=0, width=720, height=130)

        # current course
        current_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_frame.place(x=5,y=135,width=720,height=150)
        
        # dept
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","COMPUTER","IT","AIDS","ELECTRICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student information
        class_student=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=250,width=720,height=300)

        #student-id
        student_id_label=Label(class_student,text="Student-ID",font=("times new roman",13,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_Name_label=Label(class_student,text="Student-Name",font=("times new roman",13,"bold"),bg="white")
        student_Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        student_class_label=Label(class_student,text="Clas-Division",font=("times new roman",13,"bold"),bg="white")
        student_class_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("Select Division","A","B","C","D","E","F")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        student_roll_label=Label(class_student,text="Roll-No",font=("times new roman",13,"bold"),bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentroll_entry=ttk.Entry(class_student,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        student_gender_label=Label(class_student,text="Gender",font=("times new roman",13,"bold"),bg="white")
        student_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        student_dob_label=Label(class_student,text="DOB",font=("times new roman",13,"bold"),bg="white")
        student_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email
        student_email_label=Label(class_student,text="Email-ID",font=("times new roman",13,"bold"),bg="white")
        student_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentemail_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone-no
        student_phone_label=Label(class_student,text="Phone-no",font=("times new roman",13,"bold"),bg="white")
        student_phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentphone_entry=ttk.Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        studentphone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        student_addr_label=Label(class_student,text="Address",font=("times new roman",13,"bold"),bg="white")
        student_addr_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentaddr_entry=ttk.Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        studentaddr_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #class-teacher
        student_teach_label=Label(class_student,text="Class-Teacher",font=("times new roman",12,"bold"),bg="white")
        student_teach_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentteach_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        studentteach_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=720,height=580)

        img6 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\student1.jpg")
        img6 = img6.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lbl_img6 = Label(Right_frame, image=self.photoimg6)
        lbl_img6.place(x=5, y=0, width=720, height=130)

        search_student=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        search_student.place(x=5,y=135,width=710,height=70)

        search_frame=Label(search_student,text="Search ",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_frame.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_student,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Roll-NO","Phone-No","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_student,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_student,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        show_all_btn=Button(search_student,text="Show-all",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=680, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
        table_frame,
        columns=("dept", "course", "year", "sem", "id", "name", "div", "roll-no", "gender", "dob", "email", "phone-no", "address", "teacher", "photo"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Define headings
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student-ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll-no", text="Roll_No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone-no", text="Phone_No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"] = "headings"

        # Define column widths
        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("div", width=100)
        self.student_table.column("roll-no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=120)
        self.student_table.column("email", width=200)
        self.student_table.column("phone-no", width=120)
        self.student_table.column("address", width=200)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #============function declaration============
    def add_data(self):
       if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All Fields are Required",parent=self.root)
       else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HA032908@",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),                
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
        
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # =============fetch-data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="HA032908@",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =====================get cursor======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data1=content["values"]

        self.var_dep.set(data1[0]), 
        self.var_course.set(data1[1]),
        self.var_year.set(data1[2]),
        self.var_semester.set(data1[3]),
        self.var_id.set(data1[4]),
        self.var_name.set(data1[5]),                
        self.var_div.set(data1[6]),
        self.var_roll.set(data1[7]),
        self.var_gender.set(data1[8]),
        self.var_dob.set(data1[9]),
        self.var_email.set(data1[10]),
        self.var_phone.set(data1[11]),
        self.var_address.set(data1[12]),
        self.var_teacher.set(data1[13]),
        self.var_radio1.set(data1[14])
    
    # ===================update-function=====================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do yo want to update??",parent=self.root)
                if Update:
                    conn=mysql.connector.connect(host="localhost",username="root",password="HA032908@",database="face_recogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_Id=%s",(
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_name.get(),                
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_id.get()
        

                                                                                                                                                      
                                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details updated sucessfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #=========DELETE FUNCTION================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student_Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the student record?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="HA032908@",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Students Detail Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    #===========RESET FUNCTION==============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),                
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="HA032908@", database="face_recogniser")
                my_cursor = conn.cursor()
                
                # Update student info
                my_cursor.execute("""
                    UPDATE student SET 
                        Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                        Roll_no=%s, Gender=%s, DOB=%s, Email=%s, Phone_no=%s, Address=%s, 
                        Teacher=%s, Photo_Sample=%s 
                    WHERE Student_Id=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get()  # Corrected here
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load Haar Cascade
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None

                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    messagebox.showerror("Error", "Cannot access webcam.", parent=self.root)
                    return

                img_id = 0
                while True:
                    ret, myframe = cap.read()
                    if not ret:
                        break
                    face = face_crop(myframe)
                    if face is not None:
                        img_id += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(self.var_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crop Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating datasets completed successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    
        


               

if __name__ == "__main__":
  root = Tk()
  app = Student(root)
  root.mainloop()