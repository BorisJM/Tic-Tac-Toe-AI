from game import board, evaluateBoard, get_available_moves

# 9. Funkcja minimax, żeby AI dokonało najlepszej decyzji.
def minimax(alpha, beta, is_maximizing, isAiChoice=False):
    score = evaluateBoard()

    # Gra skończona
    if score is not None:
        return score

    # Ruch AI (maksymalizacja)
    if is_maximizing:
        best_score = -float('inf')
        best_move = None

        for element in get_available_moves():
            board[element] = "O"

            score = minimax(alpha, beta, False)

            # Cofnięcie ruchu
            board[element] = " "

            if score > best_score:
                best_score = score
                best_move = element

            # Alpha update
            alpha = max(alpha, score)

            # Alpha-Beta pruning
            if alpha >= beta:
                break

        if isAiChoice:
            return best_move
        return best_score

    # Ruch użytkownika (minimalizacja)
    else:
        best_score = float('inf')

        for element in get_available_moves():
            board[element] = "X"

            score = minimax(alpha, beta, True)

            # Cofnięcie ruchu
            board[element] = " "

            best_score = min(best_score, score)

            # Beta update
            beta = min(beta, score)

            # Alpha-Beta pruning
            if alpha >= beta:
                break

        return best_score