from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os
from tracker import drink_water, get_count, get_goal, reset_today

def show_reminder():
    root = tk.Tk()
    root.title("HydraBuddy 💧")
    root.geometry("400x610")
    root.configure(bg="#EAF8FF")
    root.resizable(False, False)

    tk.Label(root,text="HydraBuddy 💧",font=("Segoe UI",24,"bold"),
             bg="#EAF8FF",fg="#0077B6").pack(pady=(15,5))

    tk.Label(root,text="Time to drink water!",
             font=("Segoe UI",13),
             bg="#EAF8FF",fg="#555555").pack()

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir,"assets","cat.png")

    image = Image.open(image_path).resize((100,100))
    cat = ImageTk.PhotoImage(image)

    img = tk.Label(root,image=cat,bg="#EAF8FF")
    img.image = cat
    img.pack(pady=8)

    message = tk.Label(root,
        text="💧 Drink one glass of water!",
        font=("Segoe UI",14,"bold"),
        bg="#EAF8FF",
        fg="#333333")
    message.pack(pady=5)

    count_label = tk.Label(
        root,
        text=f"Today's Progress: {get_count()} / {get_goal()} glasses",
        font=("Segoe UI",12,"bold"),
        bg="#EAF8FF",
        fg="#0077B6")
    count_label.pack(pady=5)
    progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=250,
    mode="determinate"
)

    progress["maximum"] = get_goal()
    progress["value"] = get_count()
 
    progress.pack(pady=8)

    def drank():
        if get_count() < get_goal():
          drink_water()
        count_label.config(
            text=f"Today's Progress: {get_count()} / {get_goal()} glasses")
        progress["value"] = get_count()
        if get_count() >= get_goal():
         message.config(text="🏆 Daily Goal Completed!")
        else:
          message.config(text="🎉 Great Job! Stay Hydrated.")
        root.after(1500, root.destroy)

    def later():
        message.config(text="😊 I'll remind you again later.")
        root.after(1500, root.destroy)

    tk.Button(root,text="💧 I Drank Water",command=drank,
              bg="#4CAF50",fg="white",
              font=("Segoe UI",11,"bold"),
              width=24,height=2).pack(pady=8)

    tk.Button(root,text="⏰ Remind Me Later",command=later,
              bg="#FFB703",fg="black",
              font=("Segoe UI",11,"bold"),
              width=20,height=1).pack(pady=8)

    tk.Button(
    root,
    text="🔄 Reset Today",
    command=lambda: (
        reset_today(),
        count_label.config(
            text=f"Today's Progress: {get_count()} / {get_goal()} glasses"
        ),
        progress.configure(value=get_count())
    ),
    bg="#F44336",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20,
    height=1
).pack(pady=5)

    tk.Label(root,
             text="Made with ❤️ by Anusha & Aanya",
             font=("Segoe UI",10),
             bg="#EAF8FF",
             fg="gray").pack(side="bottom",pady=15)

    root.mainloop()



def show_cat():

    root = tk.Tk()
    

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "assets", "cat.png")

    image = Image.open(image_path)
    image = image.resize((100, 100))

    cat = ImageTk.PhotoImage(image)

    label = tk.Label(
    root,
    bg="white",
    borderwidth=0
)

    label.configure(image=cat)
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


if __name__ == "__main__":
    show_cat()