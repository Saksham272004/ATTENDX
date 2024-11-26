
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        
        #variables
        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_div = StringVar()
        
        self.var_rollno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        #first imagde
        img=Image.open(r"C:\Users\Sg201\ATTENDX\images\s1.jpg")
        img=img.resize((500,130) )
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\Sg201\ATTENDX\images\s2.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\Sg201\ATTENDX\images\s3.jpg")
        img2=img2.resize((550,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=550,height=130)
        
         #bg image
        
        img3=Image.open(r"C:\Users\Sg201\ATTENDX\images\5.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=55,width=1500,height=580)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=560)
        
        img_left=Image.open(r"C:\Users\Sg201\ATTENDX\images\22.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=0,y=0,width=720,height=130)
        #current cousre
        CURRENT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        CURRENT_frame.place(x=10,y=100,width=720,height=150)
        #department
        dep_label=Label(CURRENT_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(CURRENT_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","CSE","IT","ECE","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=15,sticky=W)
        #course
        course_label=Label(CURRENT_frame,text="Specialization",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
    
        
        course_combo=ttk.Combobox(CURRENT_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Specialization","None","IOT","DS","AI","AIML","CYS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)
    
        #year
        year_label=Label(CURRENT_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    
        
        year_combo=ttk.Combobox(CURRENT_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #semester
        sem_label=Label(CURRENT_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
    
        
        sem_combo=ttk.Combobox(CURRENT_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only")
        sem_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #CLASS STUDENT INFO
        classstudent_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Infomation",font=("times new roman",12,"bold"))
        classstudent_frame.place(x=10,y=250,width=720,height=320)
        
        #student id
        studentid_label=Label(classstudent_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)
    
        studentid_entry=ttk.Entry(classstudent_frame,textvariable=self.var_student_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #student name
        studentname_label=Label(classstudent_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,sticky=W)
    
        studentname_entry=ttk.Entry(classstudent_frame,textvariable=self.var_student_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #class division
        classdiv_label=Label(classstudent_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classdiv_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
    
        #classdiv_entry=ttk.Entry(classstudent_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        ##classdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #roll no
        roll_label=Label(classstudent_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
    
        roll_entry=ttk.Entry(classstudent_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        

        # Gender
        gender_label = Label(classstudent_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
       
        
        gender_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # Date of Birth
        dob_label = Label(classstudent_frame, text="Date of Birth:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(classstudent_frame, textvariable=self.var_dob,width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(classstudent_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(classstudent_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_label = Label(classstudent_frame, text="Phone Number:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(classstudent_frame, textvariable=self.var_phone,width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Address
        address_label = Label(classstudent_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry =  ttk.Entry(classstudent_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky=W)

        # Coordinator Name
        coordinator_label = Label(classstudent_frame, text="Coordinator Name:", font=("times new roman", 12, "bold"), bg="white")
        coordinator_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        coordinator_entry = ttk.Entry(classstudent_frame, textvariable=self.var_teacher,width=20, font=("times new roman", 12, "bold"))
        coordinator_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(classstudent_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        # "No Photo Sample" radio button
        self.var_radio2=StringVar()
        radiobtn2 = ttk.Radiobutton(classstudent_frame, variable=self.var_radio1,text="No Photo Sample",  value="No")
        radiobtn2.grid(row=6, column=1)
        
        #buttons frame
        btn_frame=Frame(classstudent_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=-1,y=200,width=719,height=98)
        
        # Save Button
        save_btn = Button(btn_frame, text="SAVE", command=self.add_data,width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        # Update Button
        update_btn = Button(btn_frame, text="UPDATE",command=self.update_data,width=18, font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Delete Button
        delete_btn = Button(btn_frame, text="DELETE",command=self.delete_data, width=18, font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="RESET",command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)
        
        btn_frame1=Frame(classstudent_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=719,height=53)
        # Take Photo Button
        take_photo_btn = Button(btn_frame1, text="TAKE PHOTO", command=self.generate_dataset,width=38, font=("times new roman", 12, "bold"), bg="purple", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=5, pady=5)
        # Update Photo Button
        update_photo_btn = Button(btn_frame1, text="UPDATE PHOTO", width=37, font=("times new roman", 12, "bold"), bg="teal", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=5, pady=5)


        
        #right label,
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=740,height=560)
        
        img_right=Image.open(r"C:\Users\Sg201\ATTENDX\images\s34.jpg")
        img_right=img_right.resize((737,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_label=Label(right_frame,image=self.photoimg_right)
        f_label.place(x=0,y=0,width=737,height=130)
        
        #search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=728,height=70)
        
        search_label=Label(search_frame,text="Search Bar:",font=("times new roman",12,"bold"),bg="light blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_combo=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo, font=("arial",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","roll_no","Name","student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame, width=20,textvariable=self.var_search, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        search_btn = Button(search_frame, text="Search", width=14, font=("times new roman", 12, "bold"), command=self.search_data,bg="red", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=5)
        
        showall_btn = Button(search_frame, text="Show ALL", width=13, font=("times new roman", 12, "bold"), command=self.search_data,bg="red", fg="white")
        showall_btn.grid(row=0, column=4, padx=5, pady=5)
        
        
        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=728,height=330)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","speacialization","sem","year","id","name","div","rollno","gender","dob","email","phone","address","co-ordinator","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("speacialization",text="Speacialization")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("rollno",text="RollNo")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("co-ordinator",text="Co-Ordinator")
        self.student_table.heading("photo",text="PhotoSampleStatus")     
        self.student_table["show"]="headings"
        
        
        
        
        
        self.student_table.column("dep", width=100)
        self.student_table.column("speacialization", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        
        self.student_table.column("rollno", width=100)
        
        self.student_table.column("dob", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("co-ordinator", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)   
        self.student_table.bind("<ButtonRelease>",self.get_cursor) 
        self.fetch_data()

    #=============function declaration======
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_student_name.get() == "" or self.var_student_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Saksham1234", database="recognizationface")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    
                    self.var_student_id.get(),
                    self.var_student_name.get(),
                    self.var_div.get(),
                    self.var_rollno.get(),
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
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Due To : {str(e)}", parent=self.root)

    #=======fetch data=====
    def fetch_data(self) :
        conn = mysql.connector.connect(host="localhost", username="root", password="Saksham1234", database="recognizationface")
        my_cursor = conn.cursor()      
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if (len(data))!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                                                                                       
    #get=== cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]      
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
       
        self.var_semester.set(data[2]),
        self.var_year.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
            
    #update function
   
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_student_name.get() == "" or self.var_student_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student details ",parent=self.root)        
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saksham1234", database="recognizationface")
                    my_cursor = conn.cursor() 
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,photosample=%s where student_id=%s",(
                        
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_semester.get(),
                                                
                                                self.var_div.get(),
                                                self.var_rollno.get(),
                                                self.var_gender.get(),
                                                self.var_dob.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_address.get(),
                                                self.var_teacher.get(),
                                                self.var_radio1.get(),
                                                self.var_student_id.get(),
                    ))
                else:
                    if not update:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details successfully update completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"due To:{str(es)}",parent=self.root) 
                   
    #=====delete===
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this  student data",parent=self.root)    
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Saksham1234", database="recognizationface")
                    my_cursor = conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student Credentials ",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"due To:{str(es)}",parent=self.root)                
                    
    #====reset======
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Specialization")
        self.var_semester.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_student_name.set("")
        self.var_student_id.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #======search dat=====
    def search_data(self):
        if self.var_search.get() == "" or self.var_combo.get() == "":
            messagebox.showerror("ERROR", "Please Select Option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Saksham1234", database="recognizationface")
                my_cursor = conn.cursor()

                # Using parameterized queries to prevent SQL injection
                query = f"SELECT * FROM student WHERE {self.var_combo.get()} LIKE %s"
                my_cursor.execute(query, ("%" + self.var_search.get() + "%",))
                
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)  # Corrected to `insert`
                    conn.commit()
                else:
                    messagebox.showinfo("No Results", "No records found matching your search", parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror("ERROR", f"Due to: {str(es)}", parent=self.root)

            
    #=====Face crop=========
    def face_Cropped(self,img,classifier):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=classifier.detectMultiScale(gray,1.3,5)
        #scaling factor
        #minimum neighbour=5
        for (x,y,w,h) in faces:
            face_cropped=img[y:y+h,x:x+w]
            return face_cropped
    
        
   

    def generate_dataset(self):
        # Check if student ID and other fields are filled
        if self.var_dep.get() == "Select Department" or self.var_student_name.get() == "" or self.var_student_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Saksham1234",
                database="recognizationface"
            )
            my_cursor = conn.cursor()

            # Log student ID for debugging
            student_id = self.var_student_id.get()
            print(f"Generating dataset for student ID: {student_id}")

            # Update student info in the database
            my_cursor.execute("""
                UPDATE student 
                SET Dep=%s, course=%s, year=%s, semester=%s, Divison=%s, Roll=%s, Gender=%s, DOB=%s, 
                    Email=%s, Phone=%s, Address=%s, Teacher=%s, photosample=%s 
                WHERE student_id=%s
                """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_rollno.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                student_id,  # Ensure the student ID is bound here
            ))

            # Check if update was successful
            if my_cursor.rowcount == 0:
                messagebox.showerror("Error", "Student ID not found or no data updated", parent=self.root)
                conn.close()
                return

            # Commit changes
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Proceed to capture images if the update is successful
            self.capture_images(student_id)

        except Exception as es:
            messagebox.showerror("ERROR", f"Due to: {str(es)}", parent=self.root)


    def capture_images(self, student_id):
        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, my_frame = cap.read()
            if not ret:
                break

            face = self.face_Cropped(my_frame, self.face_classifier)
            if face is not None:
                img_id += 1
                face_resized = cv2.resize(face, (450, 450))
                face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)

                # Save image using the student ID
                file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                print(f"Saving image at: {file_name_path}")  # Debug print for file path
                cv2.imwrite(file_name_path, face_gray)

                # Display the capture for feedback
                cv2.putText(face_gray, f"ID: {student_id} - {img_id}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face_gray)

            # Stop capturing after 100 images or if 'Enter' is pressed
            if cv2.waitKey(1) == 13 or img_id == 100:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Generating Data sets Completed!")

                        
                        
                    
                 
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                                             
if __name__=="__main__": 
    root=Tk()
    obj=Student(root)
    root.mainloop()