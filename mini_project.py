import tkinter as tk
import random

SIZE = 4
CELL_SIZE = 80

# Colors
COLORS = {
    "empty": "#ecf0f1",
    "player": "#3498db",
    "danger": "#e74c3c",
    "gold": "#f1c40f",
    "hint": "#95a5a6"
}

# Main window
root = tk.Tk()
root.title("🧠 Smart Wumpus World")

# Game variables
grid = [["" for _ in range(SIZE)] for _ in range(SIZE)]
player_pos = [0, 0]
score = 0
game_over = False

# Place items
def place_item(symbol):
    while True:
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)
        if grid[x][y] == "" and [x, y] != [0, 0]:
            grid[x][y] = symbol
            break

def setup_game():
    global grid, player_pos, score, game_over
    grid = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    player_pos = [0, 0]
    score = 0
    game_over = False

    place_item("W")
    place_item("G")
    place_item("P")

    status_label.config(text="Game Started! Explore safely 🧭")
    update_grid()

# Get hints
def get_hint(x, y):
    hints = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if grid[nx][ny] == "W":
                hints.append("💨 Stench")
            if grid[nx][ny] == "P":
                hints.append("🌫 Breeze")
    return " | ".join(hints)

# UI Grid
buttons = []
def update_grid():
    for i in range(SIZE):
        for j in range(SIZE):
            btn = buttons[i][j]

            if [i, j] == player_pos:
                btn.config(text="🤖", bg=COLORS["player"])
            else:
                hint = get_hint(i, j)
                btn.config(text=hint, bg=COLORS["empty"])

# Move player
def move(direction):
    global score, game_over
    if game_over:
        return

    x, y = player_pos

    if direction == "up" and x > 0:
        player_pos[0] -= 1
    elif direction == "down" and x < SIZE-1:
        player_pos[0] += 1
    elif direction == "left" and y > 0:
        player_pos[1] -= 1
    elif direction == "right" and y < SIZE-1:
        player_pos[1] += 1
    else:
        status_label.config(text="❌ Invalid Move!")
        return

    score -= 1
    check_status()
    update_grid()
    score_label.config(text=f"Score: {score}")

# Check status
def check_status():
    global game_over, score
    x, y = player_pos

    if grid[x][y] == "W":
        status_label.config(text="😱 Wumpus got you!")
        game_over = True
    elif grid[x][y] == "P":
        status_label.config(text="😵 Fell into Pit!")
        game_over = True
    elif grid[x][y] == "G":
        status_label.config(text="🎉 You found GOLD!")
        score += 50
        game_over = True

# Simple AI Agent (random safe move)
def auto_move():
    if game_over:
        return

    directions = ["up", "down", "left", "right"]
    move(random.choice(directions))

# UI Layout
frame = tk.Frame(root)
frame.pack()

for i in range(SIZE):
    row = []
    for j in range(SIZE):
        btn = tk.Label(frame, text="", width=10, height=4,
                       bg=COLORS["empty"], relief="ridge", font=("Arial", 10))
        btn.grid(row=i, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Controls
controls = tk.Frame(root)
controls.pack(pady=10)

tk.Button(controls, text="⬆", command=lambda: move("up")).grid(row=0, column=1)
tk.Button(controls, text="⬅", command=lambda: move("left")).grid(row=1, column=0)
tk.Button(controls, text="⬇", command=lambda: move("down")).grid(row=1, column=1)
tk.Button(controls, text="➡", command=lambda: move("right")).grid(row=1, column=2)

tk.Button(controls, text="🤖 Auto Move", command=auto_move).grid(row=2, column=0, columnspan=3, pady=5)
tk.Button(controls, text="🔄 Restart", command=setup_game).grid(row=3, column=0, columnspan=3)

# Status + Score
status_label = tk.Label(root, text="Welcome!", font=("Arial", 12), fg="blue")
status_label.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()

# Start game
setup_game()

root.mainloop()