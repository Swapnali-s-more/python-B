import tkinter as tk

root = tk.Tk()
root.title("🌈 Mood App")
root.geometry("300x300")

def happy():
    root.configure(bg="#FFFACD")  # light yellow
    label.config(text="😊 Stay Happy!")-

def sad():
    root.configure(bg="#ADD8E6")  # light blue
    label.config(text="😢 It's okay to feel sad")

def angry():
    root.configure(bg="#FFB6C1")  # light pink
    label.config(text="😡 Take a deep breath")

def chill():
    root.configure(bg="#E0FFFF")  # light cyan
    label.config(text="😌 Relax & Chill")

label = tk.Label(root, text="Choose your mood 💭",
                 font=("Arial", 12))
label.pack(pady=20)

tk.Button(root, text="😊 Happy", command=happy).pack(pady=5)
tk.Button(root, text="😢 Sad", command=sad).pack(pady=5)
tk.Button(root, text="😡 Angry", command=angry).pack(pady=5)
tk.Button(root, text="😌 Chill", command=chill).pack(pady=5)

root.mainloop()
