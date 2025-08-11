from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import csv
import os

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ========== Variables ==========
        self.var_att_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()

        self.mydata = []  # For storing CSV data

        # ======= Top images =======
        img1 = Image.open("college_images/smart-attendance.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=800, height=200)

        img2 = Image.open("college_images/clg.jpg").resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=800, y=0, width=800, height=200)

        img3 = Image.open("college_images/bg2.jpg").resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Times New Roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================== Main Frame ==================
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # ================= Left Frame =================
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=740, height=580)

        img_left = Image.open("college_images/student.jpeg").resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        lbl_img_left = Label(Left_frame, image=self.photoimg_left)
        lbl_img_left.place(x=5, y=0, width=720, height=130)

        linside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        linside_frame.place(x=0, y=135, width=720, height=300)

        # ======= Labels and Entries =======
        Label(linside_frame, text="Attendance-ID", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_att_id, width=20, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Student-Name", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Department", font=("times new roman", 13, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_dep, width=20, font=("times new roman", 13, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Roll-No", font=("times new roman", 13, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Date", font=("times new roman", 13, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_date, width=20, font=("times new roman", 13, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Time", font=("times new roman", 13, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(linside_frame, textvariable=self.var_time, width=20, font=("times new roman", 13, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(linside_frame, text="Status", font=("times new roman", 13, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.status_combo = ttk.Combobox(linside_frame, textvariable=self.var_status, font=("times new roman", 13, "bold"), state="readonly", width=18)
        self.status_combo["values"] = ("Status", "Present", "Absent")
        self.status_combo.current(0)
        self.status_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ========== Buttons ==========
        btn_frame = Frame(linside_frame, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.import_csv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Export CSV", command=self.export_csv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2, padx=5)
        Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3, padx=5)

        # ============== Right Frame =============
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=740, height=580)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=10, width=720, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,
            columns=("id", "name", "roll", "dep", "time", "date", "status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Attendance ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll", text="Roll")
        self.attendance_table.heading("dep", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"

        for col in ("id", "name", "roll", "dep", "time", "date", "status"):
            self.attendance_table.column(col, width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # ========== Functions ==========

    def import_csv(self):
        self.mydata.clear()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")))
        if file_path:
            with open(file_path) as file:
                csv_read = csv.reader(file)
                for row in csv_read:
                    self.mydata.append(row)
                self.fetch_data(self.mydata)

    def export_csv(self):
        try:
            if not self.mydata:
                messagebox.showerror("No Data", "No data found to export!", parent=self.root)
                return
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File", "*.csv")])
            if file_path:
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    for row in self.mydata:
                        writer.writerow(row)
                messagebox.showinfo("Export Successful", f"Data exported to {file_path}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting file: {str(e)}", parent=self.root)

    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for row in rows:
            self.attendance_table.insert("", END, values=row)

    def get_cursor(self, event=""):
        cursor_focus = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_att_id.set(data[0])
            self.var_name.set(data[1])
            self.var_roll.set(data[2])
            self.var_dep.set(data[3])
            self.var_time.set(data[4])
            self.var_date.set(data[5])
            self.var_status.set(data[6])

    def reset_data(self):
        self.var_att_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_status.set("Status")

    def update_data(self):
        selected = self.attendance_table.focus()
        if selected:
            self.attendance_table.item(selected, values=(
                self.var_att_id.get(),
                self.var_name.get(),
                self.var_roll.get(),
                self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_status.get()
            ))
            messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)
        else:
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
