import tkinter as tk

root = tk.Tk()
root.title("🌸 Flower Garden")
root.geometry("300x300")
root.configure(bg="#F9CADA")  # pastel pink

count = 0

def grow_flower():
    global count
    count += 1
    label.config(text="Flowers: " + "🌸" * count)

title = tk.Label(root, text="🌼 Grow Your Garden 🌼",
                 font=("Arial", 14), bg="#FFF0F5")
title.pack(pady=10)

btn = tk.Button(root, text="Grow Flower 🌱",
                command=grow_flower,
                bg="#B0E0E6", padx=10)
btn.pack(pady=10)

label = tk.Label(root, text="",
                 font=("Arial", 12),
                 bg="#FFF0F5")
label.pack(pady=20)
  
root.mainloop()
