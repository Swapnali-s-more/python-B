import tkinter as tk
import random

SIZE = 4

COLORS = {
    "empty": "#ecf0f1",
    "player": "#3498db",
    "danger": "#e74c3c",
    "gold": "#f1c40f",
    "hint": "#bdc3c7"
}

root = tk.Tk()
root.title("Wumpus World")

grid = []
player_pos = [0, 0]
score = 0
game_over = False
buttons = []

# Setup game
def setup_game():
    global grid, player_pos, score, game_over

    grid = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    player_pos = [0, 0]
    score = 0
    game_over = False

    place_item("W")
    place_item("P")
    place_item("G")

    status_label.config(text="Find the Gold!")
    score_label.config(text="Score: 0")
    update_grid()

# Place items
def place_item(symbol):
    while True:
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)

        if grid[x][y] == "" and [x, y] != [0, 0]:
            grid[x][y] = symbol
            break

# Hints
def get_hint(x, y):
    hints = []

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if grid[nx][ny] == "W":
                hints.append("💨")
            if grid[nx][ny] == "P":
                hints.append("🌫")

    return " ".join(hints)

# Update UI
def update_grid():
    for i in range(SIZE):
        for j in range(SIZE):
            btn = buttons[i][j]

            if [i, j] == player_pos:
                btn.config(text="🤖", bg=COLORS["player"])

            elif grid[i][j] == "W":
                btn.config(text="🐉", bg=COLORS["danger"])

            elif grid[i][j] == "P":
                btn.config(text="🕳", bg=COLORS["danger"])

            elif grid[i][j] == "G":
                btn.config(text="🪙", bg=COLORS["gold"])

            else:
                hint = get_hint(i, j)
                btn.config(text=hint, bg=COLORS["hint"])

# Move
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
        status_label.config(text="Invalid Move!")
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
        status_label.config(text="Wumpus got you!")
        game_over = True

    elif grid[x][y] == "P":
        status_label.config(text="Fell into pit!")
        game_over = True

    elif grid[x][y] == "G":
        status_label.config(text="You found GOLD!")
        score += 50
        game_over = True

# Auto move
def auto_move():
    if game_over:
        return
    move(random.choice(["up", "down", "left", "right"]))

# UI Grid
frame = tk.Frame(root)
frame.pack()

for i in range(SIZE):
    row = []
    for j in range(SIZE):
        btn = tk.Label(frame, width=10, height=4, relief="ridge", font=("Arial", 12))
        btn.grid(row=i, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Controls
controls = tk.Frame(root)
controls.pack()

tk.Button(controls, text="Up", command=lambda: move("up")).grid(row=0, column=1)
tk.Button(controls, text="Left", command=lambda: move("left")).grid(row=1, column=0)
tk.Button(controls, text="Down", command=lambda: move("down")).grid(row=1, column=1)
tk.Button(controls, text="Right", command=lambda: move("right")).grid(row=1, column=2)

tk.Button(controls, text="Auto Move", command=auto_move).grid(row=2, column=0, columnspan=3)
tk.Button(controls, text="Restart", command=setup_game).grid(row=3, column=0, columnspan=3)

# Labels
status_label = tk.Label(root, text="Welcome!")
status_label.pack()

score_label = tk.Label(root, text="Score: 0")
score_label.pack()

# Start
setup_game()
root.mainloop()