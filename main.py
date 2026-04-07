import tkinter as tk
from game import board, evaluateBoard, reset_board
from ai import minimax

# GUI
root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("300x350")
root.configure(bg="#1e1e1e")

buttons = []

# Klik użytkownika
def on_click(index):
    if board[index] != " ":
        return

    board[index] = "X"
    buttons[index].config(text="X")

    if check_end():
        return

    root.after(300, ai_move)


# Ruch AI
def ai_move():
    best_move = minimax(-float('inf'), float('inf'), True, True)
    board[best_move] = "O"
    buttons[best_move].config(text="O")

    check_end()


# Sprawdzenie końca gry
def check_end():
    result = evaluateBoard()

    if result is None:
        return False

    if result == 1:
        label.config(text="AI wygrało")
    elif result == -1:
        label.config(text="Ty wygrałeś")
    else:
        label.config(text="Remis")

    for btn in buttons:
        btn.config(state="disabled")

    return True


# Reset gry
def reset():
    reset_board()

    for btn in buttons:
        btn.config(text=" ", state="normal")

    label.config(text="")


# Tworzenie planszy
for i in range(9):
    btn = tk.Button(
        root,
        text=" ",
        font=("Arial", 20),
        width=5,
        height=2,
        bg="#2e2e2e",
        fg="white",
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Label wynik
label = tk.Label(root, text="", bg="#1e1e1e", fg="white")
label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=4, column=0, columnspan=3)

root.mainloop()