from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageDraw
import webbrowser


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer - Face Recognition System")

        # ========== Title ==========
        title_lbl = Label(
            self.root,
            text="Meet the Developer",
            font=("Verdana", 35, "bold"),
            bg="#f0f0f0",
            fg="#db1d1d"
        )
        title_lbl.pack(fill=X)

        # ========== Load and Darken Background ==========
        bg_image = Image.open("college_images/dev.jpg").convert("RGBA")
        overlay = Image.new("RGBA", bg_image.size, (0, 0, 0, 120))  # Black with 120 alpha (~47%)
        bg_image = Image.alpha_composite(bg_image, overlay)
        bg_image = bg_image.resize((1530, 710), Image.Resampling.LANCZOS)

        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=70, width=1530, height=720)

        # ========== Developer Card ==========
        card = Frame(bg_label, bg="white", bd=4, relief="ridge")
        card.place(x=540, y=140, width=470, height=510)

        # ========== Developer Image ==========
        dev_img = Image.open("college_images/kiran.jpg").resize((150, 150), Image.Resampling.LANCZOS)
        self.dev_photo = ImageTk.PhotoImage(dev_img)
        img_label = Label(card, image=self.dev_photo, bd=2, relief="solid")
        img_label.place(x=160, y=20, width=150, height=150)

        # ========== Developer Info ==========
        name_lbl = Label(card, text="Aayush Bhavesh Shah", font=("Segoe UI", 20, "bold"), bg="white", fg="#003366")
        name_lbl.place(x=50, y=190)

        role_lbl = Label(card, text="Data Analytics | Python Developer", font=("Segoe UI", 13), bg="white", fg="#444")
        role_lbl.place(x=80, y=225)

        # ========== Contact Info ==========
        contact_info = [
            ("Email:", "shahaayush604@gmail.com"),
            ("Phone:", "+91-7208356103"),
            ("GitHub:", "github.com/aayushshah"),
        ]

        y_start = 270
        for label, value in contact_info:
            Label(card, text=label, font=("Segoe UI", 12, "bold"), bg="white", fg="#222").place(x=60, y=y_start)
            Label(card, text=value, font=("Segoe UI", 12), bg="white", fg="#666").place(x=150, y=y_start)
            y_start += 30

        # ========== Mission Statement ==========
        quote = Label(
            card,
            text="\"Passionate about building smart tech to simplify real-world challenges.\"",
            font=("Segoe UI", 11, "italic"),
            bg="white",
            fg="#006666",
            wraplength=380,
            justify="center"
        )
        quote.place(x=30, y=380)

        # ========== Portfolio Button ==========
        Button(
            card,
            text="Visit Portfolio",
            font=("Segoe UI", 12, "bold"),
            bg="#003366",
            fg="white",
            activebackground="#0059b3",
            cursor="hand2",
            relief="flat",
            command=self.open_portfolio
        ).place(x=160, y=430, width=150, height=35)

    def open_portfolio(self):
        webbrowser.open("https://github.com/aayushshah")  # Update if needed


if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
