import tkinter as tk
from PIL import Image, ImageTk
import os

from tracker import drink_water


def show_reminder():

    root = tk.Tk()
    root.title("HydraBuddy 💧")
    root.geometry("600x500")
    root.configure(bg="#EAF8FF")
    root.resizable(False, False)

    # ---------- Title ----------

    tk.Label(
        root,
        text="HydraBuddy 💧",
        font=("Segoe UI", 24, "bold"),
        bg="#EAF8FF",
        fg="#0077B6"
    ).pack(pady=15)

    tk.Label(
        root,
        text="Time to drink water!",
        font=("Segoe UI", 14),
        bg="#EAF8FF",
        fg="#555555"
    ).pack()

    # ---------- Load Image ----------

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "..", "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((180, 180))

    cat_image = ImageTk.PhotoImage(image)

    cat_label = tk.Label(root, image=cat_image, bg="#EAF8FF")

    # Start outside the window
    x = -200
    y = 90

    cat_label.place(x=x, y=y)

    # ---------- Animation ----------

    def animate():

        nonlocal x

        if x < 210:
            x += 5
            cat_label.place(x=x, y=y)
            root.after(20, animate)

    animate()

    # ---------- Message ----------

    message = tk.Label(
        root,
        text="💧 Drink one glass of water!",
        font=("Segoe UI", 15, "bold"),
        bg="#EAF8FF",
        fg="#333333"
    )

    message.pack(pady=(210, 20))

    # ---------- Button Functions ----------

    def drank():

        drink_water()

        message.config(text="🎉 Great job! Stay hydrated.")

        root.after(1200, root.destroy)

    def later():

        message.config(text="😊 Okay! I'll remind you later.")

        root.after(1200, root.destroy)

    # ---------- Buttons ----------

    drink_btn = tk.Button(
        root,
        text="💧 I Drank Water",
        command=drank,
        bg="#4CAF50",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        padx=20,
        pady=10
    )

    drink_btn.pack(pady=8)

    later_btn = tk.Button(
        root,
        text="⏰ Remind Me Later",
        command=later,
        bg="#FFB703",
        fg="black",
        font=("Segoe UI", 12, "bold"),
        padx=20,
        pady=10
    )

    later_btn.pack()

    tk.Label(
        root,
        text="Made with ❤️ by Anusha & Aanya",
        font=("Segoe UI", 10),
        bg="#EAF8FF",
        fg="gray"
    ).pack(side="bottom", pady=15)

    root.mainloop()


# For testing only
if __name__ == "__main__":
    show_reminder()