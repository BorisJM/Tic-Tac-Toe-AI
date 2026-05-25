import tkinter as tk
import threading

from game import (
    board,
    BOARD_SIZE,
    reset_board,
    get_winner
)

from ai import (
    train_ai,
    choose_move
)

# TRAINING

# WINDOW

root = tk.Tk()

root.title(
    "Q-Learning AI vs AI"
)

root.geometry("550x760")

root.configure(
    bg="#1e1e1e"
)

buttons = []

current_player = "X"

running = False

training_running = False

x_wins = 0
o_wins = 0
draws = 0

# UPDATE GUI

def update_gui():

    for i in range(len(board)):

        buttons[i].config(
            text=board[i]
        )


# END GAME

def end_game(winner):

    global running
    global x_wins
    global o_wins
    global draws

    running = False

    if winner == "X":

        x_wins += 1

    elif winner == "O":

        o_wins += 1

    else:

        draws += 1

    status_label.config(
        text=(
            f"X:{x_wins} "
            f"O:{o_wins} "
            f"Draws:{draws}"
        )
    )
    root.after(
        1500,
        start_next_game
    )

# AI TURN

def ai_turn():

    global current_player
    global running

    if not running:
        return

    move = choose_move(board.copy())

    if move is not None:

        board[move] = current_player

        update_gui()

    winner = get_winner(board)

    if winner is not None:

        end_game(winner)

        return

    current_player = (
        "O"
        if current_player == "X"
        else "X"
    )

    root.after(
        300,
        ai_turn
    )

# START GAME

def start_game():

    global current_player
    global running
    running = False
    reset_board()

    update_gui()

    current_player = "X"

    running = True

    ai_turn()

# AUTO PLAY

auto_running = False


def auto_play():

    global auto_running

    auto_running = True

    start_game()


def start_next_game():

    global auto_running

    if auto_running:

        start_game()

def start_training():

    global training_running

    if training_running:
        return

    training_running = True

    def training_task():

        global training_running

        train_ai(10000)

        training_running = False

    threading.Thread(
        target=training_task,
        daemon=True
    ).start()

# GUI

frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

frame.pack(
    pady=20
)

for i in range(
    BOARD_SIZE *
    BOARD_SIZE
):

    button = tk.Button(
        frame,
        text="",
        width=6,
        height=3,
        font=(
            "Arial",
            20,
            "bold"
        ),
        bg="#2d2d2d",
        fg="white"
    )

    button.grid(
        row=i // BOARD_SIZE,
        column=i % BOARD_SIZE,
        padx=5,
        pady=5
    )

    buttons.append(button)


status_label = tk.Label(
    root,
    text="AI vs AI",
    font=("Arial", 16),
    bg="#1e1e1e",
    fg="white"
)

status_label.pack(
    pady=20
)


start_button = tk.Button(
    root,
    text="Start Game",
    command=start_game,
    font=("Arial", 14)
)

start_button.pack(
    pady=10
)


auto_button = tk.Button(
    root,
    text="Auto Play",
    command=auto_play,
    font=("Arial", 14)
)

auto_button.pack(
    pady=10
)

train_button = tk.Button(
    root,
    text="Train AI",
    command=start_training,
    font=("Arial", 14)
)

train_button.pack(pady=10)

root.mainloop()