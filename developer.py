from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk

class display:
    def __init__(self, root):
        self.root = root
        self.root.title("AttendX Team Members")
        self.root.geometry("1530x790")  # Set the window size

        # Configure grid layout to divide the screen into 2x2
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Define team members
        self.team_members = [
            {
                "name": "Nalin Trivedi",
                "role": "Frontend Developer",
                "contribution": "Nalin designed the Tkinter GUI interface for AttendX, ensuring it is visually appealing and intuitive.",
                "image_path": r"C:\Users\Sg201\ATTENDX\images\69.jpg",
                "position": (0, 1)  # Top-left corner
            },
            {
                "name": "Saksham Gupta",
                "role": "OpenCV Specialist",
                "contribution": "Saksham integrated OpenCV for facial recognition, optimizing for real-time tracking and robust recognition.",
                "image_path": r"C:\Users\Sg201\ATTENDX\images\32066.jpg",
                "position": (1, 1)  # Top-right corner
            },
            {
                "name": "Rahul Singh",
                "role": "Backend Developer",
                "contribution": "Rahul developed the backend for secure data storage, integrating it with the Tkinter GUI.",
                "image_path": r"C:\Users\Sg201\ATTENDX\images\2212329.jpg",
                "position": (0, 0)  # Bottom-left corner
            },
            {
                "name": "Shambhavi Tiwari",
                "role": "Algorithm and Data Training Specialist",
                "contribution": "Shambhavi trained models for high-accuracy recognition in diverse conditions.",
                "image_path": r"C:\Users\Sg201\ATTENDX\images\32066.jpg",
                "position": (1, 0)  # Bottom-right corner
            }
        ]

        # Display team member information
        self.display_team_info()

    def display_team_info(self):
        # Loop through each team member and create their display frames
        for member in self.team_members:
            self.create_member_frame(
                name=member["name"],
                role=member["role"],
                contribution=member["contribution"],
                image_path=member["image_path"],
                position=member["position"]
            )

    def create_member_frame(self, name, role, contribution, image_path, position):
        # Load and display image with a smaller size
        img = Image.open(image_path)
        img = img.resize((150, 150))  # Smaller image size for more space
        photo = ImageTk.PhotoImage(img)
        
        # Frame for each member's info
        member_frame = tk.Frame(self.root, padx=20, pady=20)
        member_frame.grid(row=position[0], column=position[1], sticky="nsew", padx=20, pady=20)

        # Add image to the top center of the frame
        label_image = tk.Label(member_frame, image=photo)
        label_image.image = photo  # Keep reference to prevent garbage collection
        label_image.pack()

        # Display name (role) and contribution text below the image
        label_role = tk.Label(member_frame, text=f"Role: {role}", font=("Arial", 14, "bold"))
        label_role.pack(anchor="n", pady=(10, 0))  # Padding to create space between image and role
        
        # Display contribution with a much larger wraplength
        label_contribution = tk.Label(
            member_frame,
            text=f"Contribution:\n{contribution}",
            font=("Arial", 12),
            wraplength=450,  # Increased wraplength to allow more text on each line
            justify="left"
        )
        label_contribution.pack(anchor="w", pady=(5, 0))  # Padding to separate from role text


if __name__ == "__main__":
    root = Tk()
    app = display(root)
    root.mainloop()
