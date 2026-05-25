import random
import json
import os

from game import (
    board,
    BOARD_SIZE,
    get_winner,
    get_available_moves
)

Q_TABLE_FILE = "q_table.json"

Q_TABLE = {}

LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.01

# LOAD Q TABLE

def load_q_table():

    global Q_TABLE

    if os.path.exists(Q_TABLE_FILE):

        with open(
            Q_TABLE_FILE,
            "r"
        ) as file:

            Q_TABLE = json.load(file)


def save_q_table():

    with open(
        Q_TABLE_FILE,
        "w"
    ) as file:

        json.dump(Q_TABLE, file)


load_q_table()

# BOARD STATE

def board_to_key(current_board):

    return "".join(current_board)

# GET Q VALUE

def get_q_value(state, move):

    if state not in Q_TABLE:
        Q_TABLE[state] = {}

    if str(move) not in Q_TABLE[state]:
        Q_TABLE[state][str(move)] = 0

    return Q_TABLE[state][str(move)]

# UPDATE Q VALUE

def update_q_value(
    state,
    move,
    reward,
    next_state
):

    old_value = get_q_value(
        state,
        move
    )

    next_moves = []

    if next_state in Q_TABLE:

        next_moves = (
            Q_TABLE[next_state]
            .values()
        )

    max_future_q = (
        max(next_moves)
        if next_moves
        else 0
    )

    new_value = old_value + LEARNING_RATE * (
        reward +
        DISCOUNT_FACTOR * max_future_q -
        old_value
    )

    Q_TABLE[state][str(move)] = (
        new_value
    )

# CHOOSE MOVE

def choose_move(current_board):
    current_board = current_board.copy()
    available_moves = (
        get_available_moves(
            current_board
        )
    )

    # EXPLORATION
    if random.random() < EPSILON:

        return random.choice(
            available_moves
        )

    # EXPLOITATION

    state = board_to_key(
        current_board
    )

    best_move = None
    best_value = -float("inf")

    for move in available_moves:

        q_value = get_q_value(
            state,
            move
        )

        if q_value > best_value:

            best_value = q_value
            best_move = move

    if best_move is None:

        best_move = random.choice(
            available_moves
        )

    return best_move

# TRAIN AI

def train_ai(games=50000):
    global EPSILON
    print("Training started...")

    x_wins = 0
    o_wins = 0
    draws = 0

    for game in range(games):

        training_board = (
            [" "] * (
                BOARD_SIZE *
                BOARD_SIZE
            )
        )

        current_player = "X"

        game_history = []

        while True:

            state = board_to_key(
                training_board
            )

            move = choose_move(
                training_board
            )

            training_board[move] = (
                current_player
            )

            next_state = board_to_key(
                training_board
            )

            game_history.append(
                (
                    state,
                    move,
                    current_player,
                    next_state
                )
            )

            winner = get_winner(
                training_board
            )

            if winner is not None:

                if winner == "X":
                    x_wins += 1

                elif winner == "O":
                    o_wins += 1

                else:
                    draws += 1

                # UPDATE Q VALUES

                for (
                    state,
                    move,
                    player,
                    next_state
                ) in game_history:

                    if winner == "DRAW":

                        reward = 0

                    elif winner == player:

                        reward = 1 + strategic_reward(
                            training_board,
                            player
                        )

                    else:

                        reward = -1

                    update_q_value(
                        state,
                        move,
                        reward,
                        next_state
                    )

                break

            current_player = (
                "O"
                if current_player == "X"
                else "X"
            )

        # SAVE EVERY 1000 GAMES
        if game % 1000 == 0:
            EPSILON *= 0.995
            print(
                f"Game: {game}"
            )

            print(
                f"X wins: {x_wins}"
            )

            print(
                f"O wins: {o_wins}"
            )

            print(
                f"Draws: {draws}"
            )

    save_q_table()

    print("Training finished.")

def strategic_reward(board, player):

    reward = 0

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

    # DIAGONALS
    winning_combinations.append([
        i * BOARD_SIZE + i
        for i in range(BOARD_SIZE)
    ])

    winning_combinations.append([
        i * BOARD_SIZE + (
            BOARD_SIZE - 1 - i
        )
        for i in range(BOARD_SIZE)
    ])

    for combination in winning_combinations:

        values = [
            board[i]
            for i in combination
        ]

        player_count = values.count(player)

        empty_count = values.count(" ")

        # 3 w linii
        if player_count == 3 and empty_count == 1:
            reward += 0.5

        # 2 w linii
        elif player_count == 2 and empty_count == 2:
            reward += 0.2

    return reward