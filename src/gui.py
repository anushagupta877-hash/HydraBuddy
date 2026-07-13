import tkinter as tk
from PIL import Image, ImageTk
import os

from tracker import drink_water


def show_reminder():

    root = tk.Tk()
    root.title("HydraBuddy 💧")

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="#EAF8FF")
    root.resizable(False, False)

    # ---------------- Window Position ---------------- #

    window_width = 320
    window_height = 420

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width - window_width - 20
    y = screen_height - window_height - 60

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # ---------------- Title ---------------- #

    tk.Label(
        root,
        text="HydraBuddy 💧",
        font=("Segoe UI", 22, "bold"),
        bg="#EAF8FF",
        fg="#0077B6"
    ).pack(pady=(15, 5))

    tk.Label(
        root,
        text="Time to drink water!",
        font=("Segoe UI", 13),
        bg="#EAF8FF",
        fg="#555555"
    ).pack()

    # ---------------- Cat Image ---------------- #

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((100, 100))

    cat_image = ImageTk.PhotoImage(image)

    cat_label = tk.Label(root, image=cat_image, bg="#EAF8FF")

    start_x = -120
    end_x = 105
    y_pos = 75

    cat_label.place(x=start_x, y=y_pos)

    x_pos = start_x

    def animate():
        nonlocal x_pos

        if x_pos < end_x:
            x_pos += 5
            cat_label.place(x=x_pos, y=y_pos)
            root.after(15, animate)

    animate()

    # ---------------- Message ---------------- #

    message = tk.Label(
        root,
        text="💧 Drink one glass of water!",
        font=("Segoe UI", 13, "bold"),
        bg="#EAF8FF",
        fg="#333333"
    )

    message.pack(pady=(130, 15))

    # ---------------- Button Functions ---------------- #

    def drank():
        drink_water()
        message.config(text="🎉 Great job! Stay hydrated.")
        root.after(1000, root.destroy)

    def later():
        message.config(text="😊 I'll remind you later.")
        root.after(1000, root.destroy)

    # ---------------- Buttons ---------------- #

    tk.Button(
        root,
        text="💧 I Drank Water",
        command=drank,
        bg="#4CAF50",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=6
    ).pack(pady=5)

    tk.Button(
        root,
        text="⏰ Remind Me Later",
        command=later,
        bg="#FFB703",
        fg="black",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=6
    ).pack()

    # ---------------- Footer ---------------- #

    tk.Label(
        root,
        text="Made with ❤️ by Anusha & Aanya",
        font=("Segoe UI", 9),
        bg="#EAF8FF",
        fg="gray"
    ).pack(side="bottom", pady=8)

    # Auto close after 15 seconds

    root.after(15000, root.destroy)

    root.mainloop()


if __name__ == "__main__":
    show_reminder()