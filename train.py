from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\Sg201\ATTENDX\images\po.jpg")
        img_top = img_top.resize((1530, 730))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=1530, height=730)

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

    def train_classifier(self):
        data_dir = "data"  # Path to your data directory
        classifier_path = "classifier.xml"
        
        # Check if the classifier file exists and delete it
        if os.path.exists(classifier_path):
            os.remove(classifier_path)
            print(f"Deleted existing {classifier_path}")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                # Open the image and convert to grayscale
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')

                # Extract ID from the filename (Assuming filename format is 'user.ID.number.jpg')
                filename = os.path.split(image)[1]
                parts = filename.split('.')  # Split by '.'
                if len(parts) >= 3:
                    id = int(parts[1])  # Extract ID (e.g., 'user.32066.1.jpg' -> 32066)
                    faces.append(imageNp)
                    ids.append(id)
                    print(f"Training image for ID: {id}")
                else:
                    print(f"Filename format error: {filename}")
                    continue  # Skip file if it doesn't have the expected format

                # Optional: Show images for feedback
                cv2.imshow("Training", imageNp)
                cv2.waitKey(10)

            except (IndexError, ValueError) as e:
                print(f"Skipping file: {image} due to error: {e}")
                continue  # Skip files that don't match the naming pattern

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, np.array(ids))  # Make sure ids is an np.array
        clf.write("classifier.xml")  # Save the trained classifier
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Set Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
