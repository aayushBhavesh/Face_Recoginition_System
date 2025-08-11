from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time

from student import Student
from train import Train
from face_recognition import Face_R
from attendance import Attendance
from developer import Developer
from chatbot import ChatBot


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ========== Top Images ==========
        img1 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\BestFacialRecognition.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\facialrecognition.png")
        img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=500, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\images.jpg")
        img3 = img3.resize((480, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=1050, y=0, width=480, height=130)

        # ========== Background ==========
        img4 = Image.open(r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\bg2.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # ========== Title ==========
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Times New Roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ========== Clock Label ==========
        self.time_lbl = Label(
            bg_img,
            font=("times new roman", 14, "bold"),
            bg="white",
            fg="blue"
        )
        self.time_lbl.place(x=1350, y=10, width=170, height=30)
        self.update_time()

        # ========== Helper Function ==========
        def create_button(img_path, text, x, y, command=None):
            image = Image.open(img_path).resize((220, 220), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            btn = Button(bg_img, image=photo, cursor="hand2", command=command)
            btn.image = photo  # prevent garbage collection
            btn.place(x=x, y=y, width=220, height=220)

            text_btn = Button(
                bg_img,
                text=text,
                cursor="hand2",
                font=("Times New Roman", 15, "bold"),
                bg="darkblue",
                fg="white",
                command=command
            )
            text_btn.place(x=x, y=y + 220, width=220, height=40)
            return btn, text_btn

        # ========== First Row Buttons ==========
        x_start = 200
        x_gap = 300
        y_top = 100

        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\student1.jpg",
            "Student Details",
            x_start,
            y_top,
            command=self.student_details
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\face_detector1.jpg",
            "Face Detector",
            x_start + x_gap,
            y_top,
            command=self.face_data
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\attendance.jpg",
            "Attendance",
            x_start + 2 * x_gap,
            y_top,
            command=self.atten_data
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\chat1.jpg",
            "Chatbot",
            x_start + 3 * x_gap,
            y_top,
            command=self.chat_data
        )

        # ========== Second Row Buttons ==========
        y_bottom = 400

        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\Train.jpg",
            "Train",
            x_start,
            y_bottom,
            command=self.train_data
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\photos.jpg",
            "Photos",
            x_start + x_gap,
            y_bottom,
            command=self.open_img
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\developers.jpg",
            "Developer",
            x_start + 2 * x_gap,
            y_bottom,
            command=self.dev_data
        )
        create_button(
            r"C:\Users\bhave\OneDrive\Desktop\Face recognition system\college_images\exit.jpg",
            "Exit",
            x_start + 3 * x_gap,
            y_bottom,
            command=self.exit_app
        )

    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")  # Format: HH:MM:SS AM/PM
        self.time_lbl.config(text=current_time)
        self.time_lbl.after(1000, self.update_time)  # Update every 1 second

    def open_img(self):
        os.startfile("data")

    # ========== Function Buttons ==========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_R(self.new_window)

    def atten_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def dev_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def chat_data(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()
