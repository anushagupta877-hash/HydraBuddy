import tkinter as tk
from PIL import Image, ImageTk
import os

from tracker import drink_water, get_water_count


def show_reminder():

    root = tk.Tk()
    root.title("HydraBuddy 💧")
    root.geometry("430x540")
    root.configure(bg="#EAF8FF")
    root.resizable(False, False)

    goal = 8
    current = get_water_count()
    progress = min(current / goal, 1)

    # ---------------- TITLE ---------------- #

    tk.Label(
        root,
        text="HydraBuddy 💧",
        font=("Segoe UI", 24, "bold"),
        bg="#EAF8FF",
        fg="#0077B6"
    ).pack(pady=(20, 5))

    tk.Label(
        root,
        text="Stay Hydrated 💙",
        font=("Segoe UI", 13),
        bg="#EAF8FF",
        fg="#666666"
    ).pack()

    # ---------------- PROGRESS ---------------- #

    tk.Label(
        root,
        text=f"Today's Progress: {current}/{goal} glasses",
        font=("Segoe UI", 11, "bold"),
        bg="#EAF8FF",
        fg="#0077B6"
    ).pack(pady=(18, 5))

    canvas = tk.Canvas(
        root,
        width=260,
        height=18,
        bg="#EAF8FF",
        highlightthickness=0
    )

    canvas.pack()

    canvas.create_rectangle(
        0,
        0,
        260,
        18,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_rectangle(
        0,
        0,
        260 * progress,
        18,
        fill="#4CAF50",
        outline=""
    )

    # ---------------- CAT IMAGE ---------------- #

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "..", "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((150, 150))

    cat_image = ImageTk.PhotoImage(image)

    cat_label = tk.Label(
        root,
        image=cat_image,
        bg="#EAF8FF"
    )

    cat_label.pack(pady=18)

    # ---------------- MESSAGE ---------------- #

    message = tk.Label(
        root,
        text="💧 It's time for your next glass of water!",
        font=("Segoe UI", 13, "bold"),
        bg="#EAF8FF",
        fg="#333333",
        wraplength=330,
        justify="center"
    )

    message.pack(pady=10)

    # ---------------- BUTTON FUNCTIONS ---------------- #

    def drank():

        drink_water()

        new_count = get_water_count()

        message.config(
            text=f"🎉 Great Job!\nYou've completed {new_count}/{goal} glasses today."
        )

        root.after(1500, root.destroy)

    def later():

        message.config(
            text="⏰ No worries!\nI'll remind you again later."
        )

        root.after(1500, root.destroy)

    # ---------------- BUTTONS ---------------- #

    drink_btn = tk.Button(
        root,
        text="💧 I Drank Water",
        command=drank,
        bg="#4CAF50",
        fg="white",
        activebackground="#43A047",
        activeforeground="white",
        font=("Segoe UI", 11, "bold"),
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    )

    drink_btn.pack(pady=(15, 8))

    later_btn = tk.Button(
        root,
        text="⏰ Remind Me Later",
        command=later,
        bg="#FFB703",
        fg="black",
        activebackground="#F4A300",
        font=("Segoe UI", 11, "bold"),
        width=22,
        height=2,
        relief="flat",
        cursor="hand2"
    )

    later_btn.pack()

    # ---------------- FOOTER ---------------- #

    tk.Label(
        root,
        text="Made with ❤️ by Team HydraBuddy\nAnusha & Aanya",
        font=("Segoe UI", 9),
        bg="#EAF8FF",
        fg="gray"
    ).pack(side="bottom", pady=15)

    root.mainloop()


if __name__ == "__main__":
    show_reminder()