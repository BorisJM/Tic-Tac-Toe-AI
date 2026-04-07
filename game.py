# Inicjalizacja planszy
board = [" "] * 9

# 7. Funckcja oceny stanu planszy.
def evaluateBoard():
    # Wszystkie kombinacje wygranej:
    winnerCombinations = [
        [0, 1, 2],  # 1.
        [3, 4, 5],  # 2.
        [6, 7, 8],  # 3.
        [0, 3, 6],  # 4.
        [1, 4, 7],  # 5.
        [2, 5, 8],  # 6.
        [0, 4, 8],  # 7.
        [2, 4, 6]   # 8.
    ]

    # Sprawdzamy wszystkie kombinacje wygranej
    for winnerComb in winnerCombinations:
        if all(element != " " for element in [
            board[winnerComb[0]],
            board[winnerComb[1]],
            board[winnerComb[2]]
        ]):
            if board[winnerComb[0]] == board[winnerComb[1]] == board[winnerComb[2]]:
                if board[winnerComb[0]] == 'O':
                    return 1
                if board[winnerComb[0]] == 'X':
                    return -1

    # Remis
    if all(element != " " for element in board):
        return 0

    # Gra trwa
    return None


# 8. Funkcja zwracająca listę wolnych indeksów w tablicy.
def get_available_moves():
    free_indexes = []
    for index, element in enumerate(board):
        if element == " ":
            free_indexes.append(index)
    return free_indexes


# Reset planszy
def reset_board():
    global board
    board = [" "] * 9