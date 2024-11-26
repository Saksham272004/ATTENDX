from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog


my_data=[]

class attend:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #========variables=====
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_Dep = StringVar()
        self.var_rollno = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_lec =StringVar()
        self.var_attendance = StringVar()
        
        
        #first imagde
        img=Image.open(r"C:\Users\Sg201\ATTENDX\images\s1.jpg")
        img=img.resize((500,180) )
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=180)
        
        #second image
        img1=Image.open(r"C:\Users\Sg201\ATTENDX\images\s2.jpg")
        img1=img1.resize((500,180))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=180)
        
        #third image
        img2=Image.open(r"C:\Users\Sg201\ATTENDX\images\s3.jpg")
        img2=img2.resize((550,180))
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=550,height=180)
        
        
        title_lbl=Label(self.root,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=180,width=1530,height=45)
        
        main_frame=Frame(self.root,bd=2,bg="Light blue")
        main_frame.place(x=0,y=225,width=1530,height=580)
        
         #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=535)
        title_lbl=Label(left_frame,text="STUDENT DETAILS",font=("times new roman",20,"bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0,width=736,height=45)
        
        inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        inside_frame.place(x=0,y=45,width=738,height=487)
        
        
        # Student ID
        student_id_label = Label(inside_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        student_id_entry = ttk.Entry(inside_frame,textvariable=self.var_student_id, width=20, font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        name_label = Label(inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        name_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Department
        dep_label = Label(inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        dep_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_Dep, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Roll No
        roll_no_label = Label(inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        roll_no_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_rollno, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Date
        date_label = Label(inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        date_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Time
        time_label = Label(inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        time_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)
        
        #===lec==
        roll_no_label = Label(inside_frame, text="Lecture:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
        roll_no_entry = ttk.Entry(inside_frame, width=20,textvariable=self.var_lec, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        # Attendance
        attendance_label = Label(inside_frame, text="Attendance:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)
        
        
        self.atten_status=ttk.Combobox(inside_frame,textvariable=self.var_attendance,font=("times new roman",12,"bold"),state="read only",width=18)
        self.atten_status["values"]=("Status","Absent","Present")
        self.atten_status.current(0)
        self.atten_status.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        
        
        
        
        
        
        
        #======button frame
        table_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=430,width=738,height=50)
        
        # Save Button
        save_btn = Button(table_frame, text="IMPORT CSV",command=self.csv_import,width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        # Update Button
        update_btn = Button(table_frame, text="EXPORT CSV",command=self.csv_export,width=18, font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Delete Button
        delete_btn = Button(table_frame, text="UPDATE", width=18,command=self.update_data, font=("times new roman", 12, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        # Reset Button
        reset_btn = Button(table_frame, text="RESET",command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)
        
        
        
    
        
         #right label,
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        right_frame.place(x=770,y=10,width=740,height=535)
        title_lbl=Label(right_frame,text="ATTENDENCE DETAILS",font=("times new roman",20,"bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0,width=730,height=45)
        
        
        #======button frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=45,width=738,height=280)
        
        #scrollbar========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendencereprt_table=ttk.Treeview(table_frame,column=("student_id","Dep","rollno","name","time","date","lecture","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendencereprt_table.xview)
        scroll_y.config(command=self.attendencereprt_table.yview)
        
        # Assuming 'self.attendencereprt_table' is a Treeview widget

        # Format column headings
        self.attendencereprt_table.heading("student_id", text="StudentID")
        self.attendencereprt_table.heading("name", text="Name")
        self.attendencereprt_table.heading("Dep", text="Department")
        self.attendencereprt_table.heading("rollno", text="Roll No")
        self.attendencereprt_table.heading("date", text="Date")
        self.attendencereprt_table.heading("time", text="Time")
        self.attendencereprt_table.heading("lecture", text="Lecture")
        self.attendencereprt_table.heading("attendence", text="Attendance")

        
        
        # Optionally set column widths and alignment
        self.attendencereprt_table.column("student_id", width=100)
        self.attendencereprt_table.column("name", width=100)
        self.attendencereprt_table.column("Dep", width=100)
        self.attendencereprt_table.column("rollno", width=100)
        self.attendencereprt_table.column("date", width=100)
        self.attendencereprt_table.column("time", width=100)
        self.attendencereprt_table.column("lecture", width=100)
        self.attendencereprt_table.column("attendence", width=100)

        # Set table to show headings
        self.attendencereprt_table["show"] = "headings"
        self.attendencereprt_table.pack(fill=BOTH,expand=1)
        self.attendencereprt_table.bind("<ButtonRelease>",self.get_cursor)
        
        
       
    
        
# ======fetch data=====
    def fetch_data(self,rows):
        self.attendencereprt_table.delete(*self.attendencereprt_table.get_children())
        for i in rows:
            self.attendencereprt_table.insert("",END,values=i)
    def csv_import(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV ",filetypes=(("CSV File","*csv"),("ALL File","**")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)
    def csv_export(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No Data","No Data found to be exported",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV ",filetypes=(("CSV File","*csv"),("ALL File","**")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data had been exported to " +os.path.basename(fln)+" Successfully")       
        
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Due To : {str(e)}", parent=self.root)    
    
    
    #=====get cursor====
    def get_cursor(self,event=""):
        cursor_row=self.attendencereprt_table.focus()
        content=self.attendencereprt_table.item(cursor_row)
        row=content['values']
        self.var_student_id.set(row[0])
        self.var_name.set(row[3])
        self.var_Dep.set(row[1])
        self.var_rollno.set(row[2])
        self.var_date.set(row[5])
        self.var_time.set(row[4])
        self.var_lec.set(row[6])
        self.var_attendance.set(row[7])
    def reset_data(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_Dep.set("")
        self.var_rollno.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_lec.set("")
        self.var_attendance.set("")
        
        

    def update_data(self):
        # Get the selected row
        selected = self.attendencereprt_table.focus()  # This gets the selected item in Treeview
        if not selected:
            messagebox.showwarning("Warning", "No record selected to update", parent=self.root)
            return

        # Retrieve the data from the form fields
        updated_data = (
            self.var_student_id.get(),
            self.var_Dep.get(),
            self.var_rollno.get(),
            self.var_name.get(),
            self.var_time.get(),
            self.var_date.get(),
            self.var_lec.get(),
            self.var_attendance.get()
        )

        # Update the Treeview with the new values
        self.attendencereprt_table.item(selected, values=updated_data)

        # Optionally, you can add code here to update the database or CSV file
        # if you need to persist the changes made in the Treeview.

        # Show success message
        messagebox.showinfo("Update Successful", "Record updated successfully", parent=self.root)

    # Add this function to the button callback
    



        
        
            
        









                
                                             
if __name__=="__main__": 
    root=Tk()
    obj=attend(root)
    root.mainloop()