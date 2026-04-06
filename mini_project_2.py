import tkinter as tk
import random
from collections import deque

# Grid settings
SIZE = 20
CELL = 25

# Game variables
snake = []
direction = (0, 1)
food = ()
running = True
ai_mode = False
score = 0
speed = 200   # 🐢 Initial speed (higher = slower)

# Window
root = tk.Tk()
root.title("🐍 Smart Snake AI Game")

canvas = tk.Canvas(root, width=SIZE*CELL, height=SIZE*CELL, bg="black")
canvas.pack()

# 🔁 Initialize Game
def init_game():
    global snake, direction, food, running, score
    snake = [(10,10), (10,9), (10,8)]
    direction = (0,1)
    food = generate_food()
    running = True
    score = 0
    update_display()

# 🍎 Generate Food
def generate_food():
    while True:
        f = (random.randint(0, SIZE-1), random.randint(0, SIZE-1))
        if f not in snake:
            return f

# 🎨 Draw Everything
def update_display():
    canvas.delete("all")

    # Snake
    for x, y in snake:
        canvas.create_rectangle(y*CELL, x*CELL, (y+1)*CELL, (x+1)*CELL, fill="green")

    # Food
    fx, fy = food
    canvas.create_oval(fy*CELL, fx*CELL, (fy+1)*CELL, (fx+1)*CELL, fill="red")

    # Score
    canvas.create_text(60, 10, text=f"Score: {score}", fill="white")

# 🧠 BFS Algorithm for AI
def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == target:
            return path

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy

            if (0 <= nx < SIZE and 0 <= ny < SIZE and
                (nx, ny) not in snake and (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(dx, dy)]))

    return []

# 🐍 Move Snake
def move():
    global direction, food, running, score

    if not running:
        return

    # AI Mode
    if ai_mode:
        path = bfs(snake[0], food)
        if path:
            direction = path[0]

    # New head
    head = (snake[0][0] + direction[0],
            snake[0][1] + direction[1])

    # Collision check
    if (head in snake or
        not (0 <= head[0] < SIZE and 0 <= head[1] < SIZE)):
        game_over()
        return

    snake.insert(0, head)

    # Food eaten
    if head == food:
        score += 10
        food = generate_food()
    else:
        snake.pop()

    update_display()
    root.after(speed, move)

# 🎮 Controls
def change_direction(new_dir):
    global direction
    direction = new_dir

def toggle_ai():
    global ai_mode
    ai_mode = not ai_mode

def increase_speed():
    global speed
    speed = max(50, speed - 50)

def decrease_speed():
    global speed
    speed += 50

# 💀 Game Over
def game_over():
    global running
    running = False
    canvas.create_text(SIZE*CELL//2, SIZE*CELL//2,
                       text="GAME OVER",
                       fill="red",
                       font=("Arial", 20))

# 🔄 Restart
def restart():
    init_game()
    move()

# 🎮 Buttons UI
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="⬆", command=lambda: change_direction((-1,0))).grid(row=0, column=1)
tk.Button(frame, text="⬅", command=lambda: change_direction((0,-1))).grid(row=1, column=0)
tk.Button(frame, text="⬇", command=lambda: change_direction((1,0))).grid(row=1, column=1)
tk.Button(frame, text="➡", command=lambda: change_direction((0,1))).grid(row=1, column=2)

tk.Button(frame, text="🤖 Toggle AI", command=toggle_ai).grid(row=2, column=0, columnspan=3)

tk.Button(frame, text="⚡ Faster", command=increase_speed).grid(row=3, column=0, columnspan=3)
tk.Button(frame, text="🐢 Slower", command=decrease_speed).grid(row=4, column=0, columnspan=3)

tk.Button(frame, text="🔄 Restart", command=restart).grid(row=5, column=0, columnspan=3)

# Start game
init_game()
move()

root.mainloop()