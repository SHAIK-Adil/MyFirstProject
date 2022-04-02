from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-----")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-----")
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ''


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("choose a position:(1-9) "))
    return position


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'


print("WELCOME to TIC TOE")
while True:
    the_board = ['']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game = input('Ready to play? Y or N? ')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 has won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = "PLAYER 2"
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 has won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = "PLAYER 1"

    if not replay():
        break















