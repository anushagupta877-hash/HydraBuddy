import tkinter as tk
from PIL import Image, ImageTk
import os

from tracker import drink_water


def show_reminder():

    root = tk.Tk()
    root.title("HydraBuddy 💧")
    root.geometry("380x450")
    root.configure(bg="#EAF8FF")
    root.resizable(False, False)

    tk.Label(
        root,
        text="HydraBuddy 💧",
        font=("Segoe UI", 24, "bold"),
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

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((130, 130))

    cat = ImageTk.PhotoImage(image)

    tk.Label(
        root,
        image=cat,
        bg="#EAF8FF"
    ).pack(pady=15)

    message = tk.Label(
        root,
        text="💧 Drink one glass of water!",
        font=("Segoe UI", 14, "bold"),
        bg="#EAF8FF",
        fg="#333333"
    )

    message.pack(pady=10)

    def drank():
        drink_water()
        message.config(text="🎉 Great Job! Stay Hydrated.")
        root.after(1500, root.destroy)

    def later():
        message.config(text="😊 I'll remind you again later.")
        root.after(1500, root.destroy)

    tk.Button(
        root,
        text="💧 I Drank Water",
        command=drank,
        bg="#4CAF50",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=22,
        height=2
    ).pack(pady=8)

    tk.Button(
        root,
        text="⏰ Remind Me Later",
        command=later,
        bg="#FFB703",
        fg="black",
        font=("Segoe UI", 11, "bold"),
        width=22,
        height=2
    ).pack()

    tk.Label(
        root,
        text="Made with ❤️ by Anusha & Aanya",
        font=("Segoe UI", 10),
        bg="#EAF8FF",
        fg="gray"
    ).pack(side="bottom", pady=15)

    root.mainloop()


def show_cat():

    root = tk.Tk()
    

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((120, 120))

    cat = ImageTk.PhotoImage(image)

    label = tk.Label(
        root,
        image=cat,
        bg="white",
        borderwidth=0
    )

    label.image = cat
    label.pack()
    

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    y = screen_h - 180
    x = -120

    root.geometry(f"120x120+{x}+{y}")

    def bounce():

        direction = -1
        current_y = y

        def animate():
            nonlocal direction, current_y

            current_y += direction

            if current_y <= y - 10:
                direction = 1
            elif current_y >= y:
                direction = -1

            root.geometry(f"120x120+{screen_w - 150}+{current_y}")
            root.after(40, animate)

        animate()


    def run_away():

        nonlocal x

        def animate():

            nonlocal x

            x += 12

            if x < screen_w + 150:
                root.geometry(f"120x120+{x}+{y}")
                root.after(15, animate)
            else:
                root.destroy()

        animate()


    def move():

        nonlocal x

        x += 8

        if x < screen_w - 150:
            root.geometry(f"120x120+{x}+{y}")
            root.after(15, move)
        else:
            bounce()


    move()

    root.after(20000, run_away)


    def open_popup(event=None):

        if root.winfo_exists():
            root.destroy()

        show_reminder()


    label.bind("<Button-1>", open_popup)

    root.mainloop()