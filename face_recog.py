from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.processed_students = set()
        self.var_period=StringVar()
        
        # Set up database connection for re-use
        self.conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Saksham1234",
            database="recognizationface"
        )
        self.my_cursor = self.conn.cursor()
        
        title_lbl = Label(self.root, text="FACE RECOGNIZATION", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        
        # Load image
        try:
            img_top = Image.open(r"C:\Users\Sg201\ATTENDX\images\new.jpg")
            img_top = img_top.resize((1530, 730))
            self.photoimg_top = ImageTk.PhotoImage(img_top)
        except FileNotFoundError:
            print("Image not found!")
            return

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=45, width=1530, height=730)
        
        # Button for face recognition
        b1_1 = Button(self.root, text="Face Recognization", command=self.face_re, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)
        
        period_label = Label(self.root, text="LECTURE:", font=("times new roman", 12, "bold"), bg="white")
        period_label.place(x=350, y=300, width=100, height=40)

        style = ttk.Style()
        style.configure("TEntry", fieldbackground="white", background="white")

        period_entry = ttk.Entry(self.root, textvariable=self.var_period, width=20, font=("times new roman", 12, "bold"), style="TEntry")
        period_entry.place(x=440, y=300, width=100, height=40)
        
    def mark_attendence(self, i, d, n, r):
        if i not in self.processed_students:
            with open("AttendX.csv", "a+", newline="\n") as f:  # Open file in append mode
                myDataList = f.readlines()
                name_list = [line.split(",")[0] for line in myDataList]
                
                if i not in name_list:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.write(f"\n{i},{d},{r},{n},{dtString},{d1},{self.var_period.get()},Present")
                    self.processed_students.add(i)
    
    def draw_boundary(self, img, classifier, scalefactor, minneighbour, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scalefactor, minneighbour)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))
            print(id)
            # Query database for student details
            self.my_cursor.execute("SELECT Name FROM student WHERE student_id = %s", (id,))
            n = self.my_cursor.fetchone()
            n = n[0] if n else "Unknown"

            self.my_cursor.execute("SELECT Roll FROM student WHERE student_id = %s", (id,))
            r = self.my_cursor.fetchone()
            r = r[0] if r else "Unknown"

            self.my_cursor.execute("SELECT Dep FROM student WHERE student_id = %s", (id,))
            d = self.my_cursor.fetchone()
            d = d[0] if d else "Unknown"

            self.my_cursor.execute("SELECT student_id FROM student WHERE student_id = %s", (id,))
            i = self.my_cursor.fetchone()
            
            if i:  # Check if i is not None
                i = i[0]
            else:
                i = "Unknown"
            print(f"Confidence: {confidence}")


            if confidence > 77:
                cv2.putText(img, f"Dep: {d}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll: {r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendence(i, d, n, r)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        return img

    
    def recognize(self, img, clf, faceCascade):
        img = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "face", clf)
        return img

    def face_re(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
