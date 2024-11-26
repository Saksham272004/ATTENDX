
####======Attendance System Using Facial Recognition
This project implements an Attendance Management System using Facial Recognition for automatic attendance tracking. 
The system captures the faces of students or employees and identifies them using facial recognition algorithms, marking their attendance in a database. The data is stored in a SQL database, and attendance records can be exported to an Excel file. It utilizes the LPHB Algorithm and OpenCV for facial recognition using frontal Haarcascades and classifiers.

Features
  Facial Recognition: Uses OpenCV and Haar Cascade Classifiers for detecting and recognizing faces.
  Automatic Attendance Tracking: Automatically marks attendance based on facial recognition.
  SQL Backend: Uses SQL to store attendance data.
  Excel Export: Allows exporting attendance data to Excel for easy viewing and reporting.
  LPHB Algorithm: Implements the Local Phase Quantization (LPHB) method for facial feature extraction and recognition.
  CSV Attendance Logging: Attendance is also logged in a CSV file (attendx.csv) for simple export and backup.
  File Structure

ATTENDX:-
├── main.py                # Main entry point for the system, where the application starts
├── student.py             # Handles student-related functionalities, like registration and management
├── attendance.py          # Manages attendance records, marking attendance, and storing data in the database
├── data.py                # Manages database operations, interactions, and queries
├── train.py               # Responsible for training the face recognition model with registered images
├── face_recog.py          # Implements the facial recognition algorithm using OpenCV and LPHB
├── developer.py           # Provides developer-specific configurations or helper functions
├── help.py                # Contains helper functions or user assistance commands
├── images/                # Folder containing images for registered students/employees (used for training)
├── attendx.csv            # Stores the marked attendance data in CSV format
└── README.md              # Project documentation
Installation
Prerequisites
To run the system, you'll need the following libraries installed:
    Python 3.x
    OpenCV: pip install opencv-python
    NumPy: pip install numpy
    Pandas: pip install pandas
    tkinter
    sqlconnector
    os
    cv2
    

Clone the repository:
  code:
  git clone https://github.com/Saksham272004/ATTENDX.git
  cd ATTENDX
  Install the required dependencies:
  
  code:
  pip install -r requirements.txt
Set up your SQL Database and configure the connection. You can use SQLite, MySQL, or any other SQL-based database. Create a database and define the Attendance Table where student/employee details and attendance logs will be stored.

Create the images folder and store registered images of each person for the face recognition model to train on. Each image should be labeled with the person's student id.


Attendance Export: The attendance can be exported to an Excel file for easy access and reporting. This can be done from the system's UI or by using the backend script.

View Attendance: The system maintains a record of attendance in the SQL database and logs the attendance to a CSV file (attendx.csv). You can open this file to view attendance records.

Algorithms Used
1. OpenCV Haar Cascade Classifier
The Haar Cascade Classifier is used to detect faces in real-time from webcam input. OpenCV provides pre-trained classifiers that can identify frontal faces efficiently.

2. LPHB Algorithm
The Local Phase Quantization (LPHB) algorithm is used to extract facial features, helping in more accurate facial recognition. This algorithm improves face recognition by handling varying lighting conditions and pose variations.

3. SQL Database Backend
The attendance data is stored in a SQL database, making it easy to manage and retrieve records. The system can store user details, face data, and attendance logs.

4. CSV File Logging
In addition to the SQL database, the system also logs attendance data in a CSV file (attendx.csv). This is useful for quick exports, backups, and easy access to attendance data.

How It Works
Face Detection: When the system is started, it continuously captures frames from the webcam. It uses Haar Cascade Classifiers to detect faces in the image.

Facial Recognition: Once a face is detected, it is compared to the faces stored in the system. If a match is found, the system marks the attendance of that person in the SQL database and logs it in the attendx.csv file.

Attendance Export: Attendance records are automatically logged in the SQL database and the CSV file. The system allows exporting these records into an Excel file for reporting.

Contribution
If you would like to contribute to this project, feel free to submit a pull request or open an issue.
