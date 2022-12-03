def print_board(board):
    for row in board:
        tmp = ' '
        for place in row:
            tmp += place + ' '
            tmp += '| '
        print(tmp[:-2])
        if row is not board[2]:
            print('-----------')

def place_mark(board, mark):
    x = int(input("Podaj wiersz z zakresu (0-2):"))
    y = int(input("Podaj kolumne z zakresu (0-2):"))
    if board[x][y] == ' ':
        board[x][y] = mark
    else:
        print("To pole jest juz zajete. Wybierz inne!")
        place_mark(board, mark)
    return board

def isWin(board, mark):
    isWin = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            isWin = True
        elif board[0][i] == board[1][i] == board[2][i] == mark:
            isWin = True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        isWin = True
    elif board[0][2] == board[1][1] == board[2][0] == mark:
        isWin = True
    return isWin

def print_end_message(active_player, round_count):
    if round_count == 9:
        print("Remis!")
    else:
        print("Gracz " + active_player + " wygrywa!")


def change_active_player(active_player):
    if active_player == 'x':
        active_player = 'o'
    else:
        active_player = 'x'
    return active_player

def game_loop():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    isEnd = False
    round_counter = 0
    activePlayer = 'o'

    print_board(board)
    while not isEnd:
        round_counter += 1
        activePlayer = change_active_player(activePlayer)
        place_mark(board, activePlayer)
        print_board(board)
        isEnd = isWin(board, activePlayer) or round_counter == 9

    return activePlayer, round_counter

def main():
    winner, round_counter = game_loop()
    print_end_message(winner, round_counter)

main()
