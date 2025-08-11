from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
import mysql.connector
from main import FaceRecognitionSystem
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # ===== Top Strip with Faces =====
        # You can replace these image paths with your own
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

        # ===== Title =====
        title_lbl = Label(self.root, text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=100, width=1550, height=50)

        # ===== Background Image =====
        bg_img = Image.open(r"college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
        bg_img = bg_img.resize((1550, 650), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=150, width=1550, height=650)

        # ===== Login Frame =====
        frame = Frame(self.root, bg="black")
        frame.place(x=580, y=200, width=400, height=450)

        # User Icon
        img_icon = Image.open(r"college_images\LoginIconAppl.png")
        img_icon = img_icon.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg_icon = ImageTk.PhotoImage(img_icon)
        lbl_icon = Label(frame, image=self.photoimg_icon, bg="black", borderwidth=0)
        lbl_icon.place(x=150, y=20)

        # Heading
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"),
                        fg="white", bg="black")
        get_str.place(x=130, y=130)

        # Username
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"),
                             fg="white", bg="black")
        username_lbl.place(x=50, y=180)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=50, y=210, width=300)

        # Password
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"),
                             fg="white", bg="black")
        password_lbl.place(x=50, y=250)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=50, y=280, width=300)

        # Login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"),
                           bd=3, relief=RIDGE, fg="white", bg="red",
                           activeforeground="white", activebackground="red",
                           command=self.login)
        login_btn.place(x=50, y=330, width=300, height=40)

        # Register Button
        register_btn = Button(frame, text="New User Register", font=("times new roman", 13, "bold"),
                              borderwidth=0, fg="white", bg="black", activeforeground="white",
                              command=self.register)
        register_btn.place(x=50, y=380, width=150)

        # Forgot Password Button
        forgot_btn = Button(frame, text="Forgot Password?", font=("times new roman", 13, "bold"),
                            borderwidth=0, fg="white", bg="black", activeforeground="white",
                            command=self.forgot_password)
        forgot_btn.place(x=200, y=380, width=150)

        # Bottom Note
        note_lbl = Label(self.root, text="Note: First input valid username and valid password",
                         font=("times new roman", 15, "bold"), fg="blue", bg="white")
        note_lbl.place(x=0, y=790, width=1550, height=20)
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username == "admin" and password == "12345":
            messagebox.showinfo("Success", "Welcome!")
        else:
            conn = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="HA032908@",
                 database="face_recogniser"
             )
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT * FROM register WHERE email=%s AND password=%s",
            (username, password)
        )

        row = my_cursor.fetchone()
        if row is None:
            messagebox.showerror("Error", "Invalid Username and Password")
        else:
            open_main = messagebox.askyesno("Access", "Access only admin")
            if open_main:
                self.new_window = Toplevel(self.root)
                self.app = FaceRecognitionSystem(self.new_window)
            else:
                return

        conn.commit()
        conn.close()

                    

        conn.commit()
        conn.close()

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Window(self.new_window)
        #messagebox.showinfo("Register", "Redirecting to registration page...")

    def forgot_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your email address to reset your password")
        else:
            conn = mysql.connector.connect(
             host="localhost",
             user="root",
             password="HA032908@",
             database="face_recogniser"
           )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            values = (self.txtuser.get(),)
            my_cursor.execute(query, values)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter valid username")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.config(bg="black")

                l = Label(self.root2, text="Forgot Password", font=("times new roman", 12, "bold"), fg="white", bg="red")
                l.place(x=0, y=10, relwidth=1)

                self.var_securityQ = StringVar()
                self.var_securityA = StringVar()
                self.var_new_password = StringVar()

                securityQ_lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), fg="red", bg="black")
                securityQ_lbl.place(x=50, y=60)

                securityQ_combo = ttk.Combobox(self.root2, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
                securityQ_combo["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
                securityQ_combo.current(0)
                securityQ_combo.place(x=50, y=90, width=250)

                securityA_lbl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="red", bg="black")
                securityA_lbl.place(x=50, y=130)

                securityA_entry = ttk.Entry(self.root2, textvariable=self.var_securityA, font=("times new roman", 15))
                securityA_entry.place(x=50, y=160, width=250)

                new_password_lbl = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="red", bg="black")
                new_password_lbl.place(x=50, y=200)

                new_password_entry = ttk.Entry(self.root2, textvariable=self.var_new_password, font=("times new roman", 15), show="*")
                new_password_entry.place(x=50, y=230, width=250)

                submit_btn = Button(self.root2, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), bg="red", fg="white")
                submit_btn.place(x=100, y=280)

    def reset_password(self):
        if self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "Please select a security question")
        elif self.var_securityA.get() == "":
            messagebox.showerror("Error", "Please enter the security answer")
        elif self.var_new_password.get() == "":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="HA032908@",
                database="face_recogniser"
            )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityQ=%s and securityA=%s"
            values = (self.txtuser.get(), self.var_securityQ.get(), self.var_securityA.get())
            my_cursor.execute(query, values)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Security question and answer do not match")
            else:
                update_query = "update register set password=%s where email=%s"
                update_values = (self.var_new_password.get(), self.txtuser.get())
                my_cursor.execute(update_query, update_values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password reset successful!")
                self.root2.destroy()

class Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background
        bg_img = Image.open(r"college_images/2-AI-invades-automobile-industry-in-2019.jpeg")
        bg_img = bg_img.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=100, width=750, height=600)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 25, "bold"), fg="red", bg="black")
        register_lbl.place(x=250, y=20)

        # Labels and Entries
        fname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="red", bg="black")
        fname_lbl.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=130, width=250)

        lname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="red", bg="black")
        lname_lbl.place(x=370, y=100)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        lname_entry.place(x=370, y=130, width=250)

        contact_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), fg="red", bg="black")
        contact_lbl.place(x=50, y=180)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        contact_entry.place(x=50, y=210, width=250)

        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="red", bg="black")
        email_lbl.place(x=370, y=180)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        email_entry.place(x=370, y=210, width=250)

        # Security Question
        securityQ_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="red", bg="black")
        securityQ_lbl.place(x=50, y=260)
        securityQ_combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        securityQ_combo["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
        securityQ_combo.current(0)
        securityQ_combo.place(x=50, y=290, width=250)

        securityA_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="red", bg="black")
        securityA_lbl.place(x=370, y=260)
        securityA_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        securityA_entry.place(x=370, y=290, width=250)

        # Password
        pass_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="red", bg="black")
        pass_lbl.place(x=50, y=340)
        pass_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        pass_entry.place(x=50, y=370, width=250)

        confpass_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="red", bg="black")
        confpass_lbl.place(x=370, y=340)
        confpass_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        confpass_entry.place(x=370, y=370, width=250)

        # Register Button
        register_btn = Button(frame, text="Register", font=("times new roman", 15, "bold"), bg="red", fg="white", command=self.register_data)
        register_btn.place(x=300, y=450, width=150, height=40)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",        # your MySQL username
                    password="HA032908@",        # your MySQL password
                    database="face_recogniser"
                )
                my_cursor = conn.cursor()

                # Create table if not exists
                my_cursor.execute("""
                CREATE TABLE IF NOT EXISTS register (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fname VARCHAR(50),
                    lname VARCHAR(50),
                    contact VARCHAR(15),
                    email VARCHAR(100) UNIQUE,
                    securityQ VARCHAR(100),
                    securityA VARCHAR(100),
                    password VARCHAR(50)
                )
                """)

                # Check if email exists
                my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
                row = my_cursor.fetchone()
                if row:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    # Insert data
                    my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Registration Successful!")

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



if __name__ == "__main__":
    main()