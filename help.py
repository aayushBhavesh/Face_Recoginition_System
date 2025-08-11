from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class HelpWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help - Face Recognition System")

        # ========== Title ==========
        title_lbl = Label(
            self.root,
            text="Help & Support",
            font=("Verdana", 35, "bold"),
            bg="#f0f0f0",
            fg="#db1d1d"
        )
        title_lbl.pack(fill=X)

        # ========== Load and Darken Background ==========
        bg_image = Image.open("college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg").convert("RGBA")  # Change image accordingly
        overlay = Image.new("RGBA", bg_image.size, (0, 0, 0, 120))  # Black overlay with alpha
        bg_image = Image.alpha_composite(bg_image, overlay)
        bg_image = bg_image.resize((1530, 710), Image.Resampling.LANCZOS)

        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=70, width=1530, height=720)

        # ========== Info Card ==========
        card = Frame(bg_label, bg="white", bd=4, relief="ridge")
        card.place(x=400, y=140, width=630, height=510)

        # ========== Help Text ==========
        help_text = (
            "Welcome to the Face Recognition Attendance System!\n\n"
            "- To add or manage students, click 'Student Details'.\n"
            "- Use 'Face Detector' to detect and recognize faces.\n"
            "- 'Attendance' shows the attendance records.\n"
            "- Use 'Train' to train the face recognition model.\n"
            "- 'Photos' opens the folder with captured photos.\n"
            "- 'Developer' shows developer information.\n\n"
            "For further assistance, please contact:\n"
            "Email: shahaayush604@gmail.com\n"
            "Phone: +91-7208356103"
        )

        help_label = Label(
            card,
            text=help_text,
            font=("Segoe UI", 14),
            bg="white",
            fg="#003366",
            justify=LEFT,
            wraplength=600
        )
        help_label.place(x=15, y=20)

        # ========== Close Button ==========
        Button(
            card,
            text="Close",
            font=("Segoe UI", 12, "bold"),
            bg="#db1d1d",
            fg="white",
            activebackground="#a30000",
            cursor="hand2",
            relief="flat",
            command=self.root.destroy
        ).place(x=270, y=450, width=100, height=40)


if __name__ == "__main__":
    root = Tk()
    app = HelpWindow(root)
    root.mainloop()
