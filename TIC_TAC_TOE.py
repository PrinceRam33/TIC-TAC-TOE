from IPython.display import clear_output
import random
def display(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_selection():
    choice = ''
    while (choice != 'X' and choice != 'O'):
        choice = input("Player 1 select 'X' or 'O': ").upper()
    if (choice == 'X'):
        return ('X', 'O')
    else:
        return ('O', 'X')


def replace(board, choice, position):
    board[position] = choice


def win_check(board, choice):
    return (board[7] == board[8] == board[9] == choice or
            board[4] == board[5] == board[6] == choice or
            board[1] == board[2] == board[3] == choice or
            board[7] == board[4] == board[1] == choice or
            board[8] == board[5] == board[2] == choice or
            board[9] == board[6] == board[3] == choice or
            board[7] == board[5] == board[3] == choice or
            board[9] == board[5] == board[1] == choice)


def spot_check(board, position):
    return board[position] == ' '


def fullboard_check(board):
    for i in range(1, 10):
        if spot_check(board, i):
            return False  # EMPTY
    return True  # nonEMPTY


def choose_first():
    flip = random.randint(0, 1)
    if (flip == 0):
        return 'Player 1'
    else:
        return 'Player 2'


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not spot_check(board, position):
        position = int(input("choose a position: (1-9) "))
    return position


def replay():
    choice = input("Play again ?? 'Y' or 'N': ")
    return choice == 'Y'


print("Welcome to TIC-TAC-TOE")
while True:
    game_board = [" "]*10
    player1, player2 = player_selection()
    turn = choose_first()
    print(turn + ' will go first ')
    play_game = input("Ready to play? y or n: ").lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display(game_board)
            position = player_choice(game_board)
            replace(game_board, player1, position)
            if win_check(game_board, player1):
                display(game_board)
                print("Player 1 won")
                game_on = False
            else:
                if fullboard_check(game_board):
                    display(game_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display(game_board)
            position = player_choice(game_board)
            replace(game_board, player2, position)
            if win_check(game_board, player2):
                display(game_board)
                print("Player 2 won")
                game_on = False
            else:
                if fullboard_check(game_board):
                    display(game_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
