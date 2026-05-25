BOARD_SIZE = 4

board = [" "] * (BOARD_SIZE * BOARD_SIZE)


def get_winner(current_board):

    winning_combinations = []

    # ROWS
    for row in range(BOARD_SIZE):

        winning_combinations.append([
            row * BOARD_SIZE + col
            for col in range(BOARD_SIZE)
        ])

    # COLUMNS
    for col in range(BOARD_SIZE):

        winning_combinations.append([
            row * BOARD_SIZE + col
            for row in range(BOARD_SIZE)
        ])

    # DIAGONAL LEFT
    winning_combinations.append([
        i * BOARD_SIZE + i
        for i in range(BOARD_SIZE)
    ])

    # DIAGONAL RIGHT
    winning_combinations.append([
        i * BOARD_SIZE + (
            BOARD_SIZE - 1 - i
        )
        for i in range(BOARD_SIZE)
    ])

    for combination in winning_combinations:

        values = [
            current_board[i]
            for i in combination
        ]

        if values.count("X") == BOARD_SIZE:
            return "X"

        if values.count("O") == BOARD_SIZE:
            return "O"

    if " " not in current_board:
        return "DRAW"

    return None


def get_available_moves(current_board):

    return [
        i for i, value
        in enumerate(current_board)
        if value == " "
    ]


def reset_board():

    global board

    for i in range(len(board)):
        board[i] = " "