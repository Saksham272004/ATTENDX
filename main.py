from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
import os
from face_recog import FaceRecognitionSystem
from attendence import attend
from developer import display # Assuming DeveloperWindow is created to handle team display

class Face_Recognization_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and place top images
        self.add_top_images()
        
        # Set background image
        img3 = Image.open(r"C:\Users\Sg201\ATTENDX\images\5.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        # Title label on the background
        title_lbl = Label(
            bg_img, 
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"), 
            bg="white", fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Define buttons with images and actions
        self.add_buttons(bg_img)

    def add_top_images(self):
        # Define top images
        images = [
            (r"C:\Users\Sg201\ATTENDX\images\1.jpg", 500, 130, 0),
            (r"C:\Users\Sg201\ATTENDX\images\2.jpg", 500, 130, 500),
            (r"C:\Users\Sg201\ATTENDX\images\3.jpg", 550, 130, 1000)
        ]
        
        for img_path, width, height, x in images:
            img = Image.open(img_path).resize((width, height))
            photo_img = ImageTk.PhotoImage(img)
            Label(self.root, image=photo_img).place(x=x, y=0, width=width, height=height)
            # Keep reference to prevent garbage collection
            setattr(self, f"photoimg_top_{x}", photo_img)

    def add_buttons(self, parent):
        # Button configurations with command functions and positions
        button_config = [
            (r"C:\Users\Sg201\ATTENDX\images\10.jpg", "Student Details", self.student_details, 350, 100),
            (r"C:\Users\Sg201\ATTENDX\images\11.jpg", "Face Detector", self.face_data, 650, 100),
            (r"C:\Users\Sg201\ATTENDX\images\12.jpg", "Attendance", self.attend_data, 950, 100),
            (r"C:\Users\Sg201\ATTENDX\images\14.jpg", "Train Data", self.train_data, 200, 380),
            (r"C:\Users\Sg201\ATTENDX\images\15.jpg", "Photos", self.open_images, 500, 380),
            (r"C:\Users\Sg201\ATTENDX\images\16.jpg", "Developer", self.dev_data, 800, 380),
            (r"C:\Users\Sg201\ATTENDX\images\17.jpg", "Exit", self.exit_app, 1100, 380)
        ]
        
        # Create buttons on the interface
        for img_path, text, cmd, x, y in button_config:
            img = Image.open(img_path).resize((220, 220))
            photo_img = ImageTk.PhotoImage(img)
            Button(parent, image=photo_img, cursor="hand2", command=cmd).place(x=x, y=y, width=220, height=220)
            Button(
                parent, text=text, cursor="hand2", command=cmd,
                font=("times new roman", 15, "bold"), bg="darkblue", fg="white"
            ).place(x=x, y=y + 200, width=220, height=40)
            # Keep reference to prevent garbage collection
            setattr(self, f"photoimg_button_{x}_{y}", photo_img)

    # Function to open student details window
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    # Function to open training data window
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    # Function to open face data window
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognitionSystem(self.new_window)
        
    # Function to open attendance data window
    def attend_data(self):
        self.new_window = Toplevel(self.root)
        self.app = attend(self.new_window)
    
    # Function to open developer info window
    def dev_data(self):
        self.new_window = Toplevel(self.root)
        self.app = display(self.new_window)  # Use DeveloperWindow to display all team members

    # Function to open images directory
    def open_images(self):
        os.startfile(r"C:\Users\Sg201\ATTENDX\data")  # Set to the correct images folder path
    
    # Exit application
    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__": 
    root = Tk()
    obj = Face_Recognization_System(root)
    root.mainloop()
