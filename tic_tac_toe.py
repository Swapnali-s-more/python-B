import tkinter as tk
import math

root = tk.Tk()
root.title("Smart Tic-Tac-Toe")

board = [" " for _ in range(9)]
buttons = []
game_over = False
player_score = 0
ai_score = 0

# Check winner
def is_winner(player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in state) for state in win_states)

# Check draw
def is_draw():
    return " " not in board

# Minimax
def minimax(is_max):
    if is_winner("O"):
        return 1
    if is_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

# AI move
def ai_move():
    global game_over, ai_score

    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        update_buttons()

    if is_winner("O"):
        status_label.config(text="AI Wins!")
        ai_score += 1
        game_over = True
    elif is_draw():
        status_label.config(text="Draw!")
        game_over = True

    update_score()

# Player move
def on_click(i):
    global game_over, player_score

    if board[i] == " " and not game_over:
        board[i] = "X"
        update_buttons()

        if is_winner("X"):
            status_label.config(text="You Win!")
            player_score += 1
            game_over = True
        elif is_draw():
            status_label.config(text="Draw!")
            game_over = True
        else:
            root.after(300, ai_move)

        update_score()

# Update buttons
def update_buttons():
    for i in range(9):
        buttons[i].config(text=board[i])

# Restart
def restart():
    global board, game_over
    board = [" " for _ in range(9)]
    game_over = False
    status_label.config(text="Your Turn")
    update_buttons()

# Score
def update_score():
    score_label.config(text=f"You: {player_score} | AI: {ai_score}")

# UI
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your Turn")
status_label.pack()

score_label = tk.Label(root, text="You: 0 | AI: 0")
score_label.pack()

tk.Button(root, text="Restart", command=restart).pack()

root.mainloop()
