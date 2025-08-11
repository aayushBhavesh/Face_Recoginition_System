from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


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
    root = Tk()
    app = Register_Window(root)
    root.mainloop()
