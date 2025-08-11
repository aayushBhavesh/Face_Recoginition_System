from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from fuzzywuzzy import fuzz
import datetime
import os

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("600x650+500+50")
        self.root.config(bg='white')

        # === Colors ===
        self.bg_color = "#E0F7FA"
        self.header_bg = "#0288D1"
        self.header_fg = "white"
        self.text_fg = "#263238"
        self.button_bg = "#01579B"
        self.button_fg = "white"

        # === Main Frame ===
        main_frame = Frame(self.root, bd=4, bg=self.bg_color, relief=RIDGE)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # === Header Frame (Image + New Chat Button) ===
        header_frame = Frame(main_frame, bg=self.header_bg)
        header_frame.pack(fill=X)

        img_chat = Image.open("chatbot.jpg")
        img_chat = img_chat.resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        img_label = Label(
            header_frame,
            image=self.photoimg,
            bg=self.header_bg,
            bd=0,
            anchor='nw',
            text="  Chat With Me 🤖",
            font=("Poppins", 16, "bold"),
            fg=self.header_fg,
            compound=LEFT,
            padx=10
        )
        img_label.pack(side=LEFT, padx=5, pady=5)

        new_chat_btn = Button(
            header_frame,
            text="New Chat",
            font=("Poppins", 10, "bold"),
            bg="white",
            fg=self.header_bg,
            activebackground="#B3E5FC",
            activeforeground=self.header_bg,
            command=self.new_chat,
            relief=RAISED,
            padx=10,
            pady=5
        )
        new_chat_btn.pack(side=RIGHT, padx=10, pady=10)

        # === Chat Display ===
        chat_frame = Frame(main_frame, bd=2, bg="white", relief=SUNKEN)
        chat_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))

        scrollbar = Scrollbar(chat_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.chat_text = Text(
            chat_frame,
            yscrollcommand=scrollbar.set,
            wrap=WORD,
            font=("Poppins", 12),
            bg="white",
            fg=self.text_fg,
            state=DISABLED
        )
        self.chat_text.pack(fill=BOTH, expand=True)
        scrollbar.config(command=self.chat_text.yview)
        # User messages: right-aligned, nice calm blue with bold font
        self.chat_text.tag_configure(
            'right',
            justify='right',
            foreground='#1565C0',  # Strong blue (Darker than plain blue)
            font=("Poppins", 12, "bold"),
            background='#E3F2FD',  # Light blue background for bubble effect
            spacing3=5  # some spacing after paragraph
        )

        # Bot messages: left-aligned, warm grayish-green with normal font
        self.chat_text.tag_configure(
            'left',
            justify='left',
            foreground='#2E7D32',  # Medium green, not too bright
            font=("Poppins", 12),
            background='#E8F5E9',  # Light green background bubble
        spacing3=5
        )


        # === Bottom Input Area ===
        bottom_frame = Frame(main_frame, bg="white")
        bottom_frame.pack(fill=X, padx=10, pady=(0, 10))

        self.entry_text = StringVar()
        self.entry_box = Entry(
            bottom_frame,
            textvariable=self.entry_text,
            font=("Poppins", 12),
            bg="#F5F5F5",
            fg=self.text_fg,
            width=40,
            relief=GROOVE
        )
        self.entry_box.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        self.entry_box.bind("<Return>", self.send_event)  # <-- Bind Enter key

        send_button = Button(
            bottom_frame,
            text="Send",
            font=("Poppins", 12, "bold"),
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground="#0277BD",
            activeforeground="white",
            relief=RAISED,
            command=self.send
        )
        send_button.pack(side=RIGHT)

        # === Keyboard Shortcut ===
        self.root.bind("<Control-n>", lambda event: self.new_chat())

        # === Chat History File Path ===
        self.history_dir = "chat_history"
        os.makedirs(self.history_dir, exist_ok=True)

    # === Save & Clear Chat ===
    def new_chat(self):
        if messagebox.askyesno("New Chat", "Do you want to start a new chat?\nCurrent chat will be saved."):
            chat_content = self.chat_text.get("1.0", END).strip()
            if chat_content:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_path = os.path.join(self.history_dir, f"chat_{timestamp}.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(chat_content)
            self.chat_text.config(state=NORMAL)
            self.chat_text.delete('1.0', END)
            self.entry_text.set("")
            self.chat_text.config(state=DISABLED)

    # === Function Declaration ===
    def send_event(self, event):
        self.send()

    def send(self):
        msg = self.entry_text.get().strip()
        if msg:
            self.chat_text.config(state=NORMAL)
            self.chat_text.insert(END, '\nYou: ' + msg + '\n', 'right')
            self.entry_text.set("")

            msg_lower = msg.lower()

            # Synonym mapping
            synonyms = {
                "who created you": ["who made you", "who developed you", "who is your creator"],
                "what's your name": ["whats your name", "your name", "do you have a name"],
                "hello": ["hi", "hey", "good morning", "good evening", "good afternoon"],
                "bye": ["goodbye", "see you", "exit", "quit"],
                "thanks": ["thank you", "thanks a lot", "thx"],
            }

            responses = {
                "hello": "Hi! How can I help you?",
                "who created you": "I was created by an awesome developer AAYUSH SHAH using Python and Tkinter!",
                "what's your name": "I am your friendly ChatBot.",
                "what is machine learning": "Machine Learning enables computers to learn from data and improve over time.",
                "how does facial recognition work": "It detects, aligns, extracts, and compares facial features with a database.",
                "can you explain step by step facial recognition system working":
                    "1. Detect face\n2. Align\n3. Extract features\n4. Match\n5. Identify/verify",
                "how many countries use facial recognition system":
                    "Many countries use it, including the USA, China, UK, India, and others.",
                "what is chatbot": "A chatbot simulates conversation with users, often to assist or inform.",
                "do you know any other languages": "I understand English, but can be programmed to speak many languages!",
                "what are the applications of machine learning":
                    "Used in recommendation systems, fraud detection, self-driving cars, healthcare, etc.",
                "how secure is facial recognition technology":
                    "Depends on implementation; it can be secure but also raises privacy concerns.",
                "what are the ethical concerns of facial recognition":
                    "Privacy, consent, bias, and surveillance are major concerns.",
                "can you tell me about natural language processing":
                    "NLP helps machines understand and process human language.",
                "how does a chatbot work":
                    "By processing input text, matching patterns, and generating responses.",
                "what programming languages are used for chatbots":
                    "Python, JavaScript, Java, and others.",
                "can you help me learn programming":
                    "Sure! Ask me anything about programming.",
                "what is artificial intelligence":
                    "AI enables machines to mimic human intelligence.",
                "how do I improve my coding skills":
                    "Practice, build projects, and read code from others.",
                "what is the future of chatbots":
                    "They will become more intelligent and helpful in many industries.",
                "can you tell me a joke":
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                "what is the difference between ai and machine learning":
                    "AI is a broad field; machine learning is a part of it focused on data-driven learning.",
                "bye": "Goodbye! Have a great day!",
                "thanks": "You're welcome! 😊"
        }

            # Map synonym to primary question
            for key, alternatives in synonyms.items():
                if msg_lower in alternatives:
                    msg_lower = key
                    break

            # Fuzzy match fallback
            best_match = None
            best_score = 0
            for question in responses:
                score = fuzz.ratio(msg_lower, question)
                if score > best_score:
                    best_score = score
                    best_match = question

            if best_score > 80:
                bot_reply = responses[best_match]
            else:
                bot_reply = "Sorry, I don't understand that. Can you try asking something else?"

            self.chat_text.insert(END, 'Bot: ' + bot_reply + '\n', 'left')
            self.chat_text.see(END)
            self.chat_text.config(state=DISABLED)


if __name__ == "__main__":
    root = Tk()
    app = ChatBot(root)
    root.mainloop()
