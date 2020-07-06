# CMPT 310
# Assignment 3
# Author: Injun Son
# Date: July 3, 2020
# a3.py
import random
import copy
# get idea of implementing game structure from https://github.com/kaustubh990/Python-Tic-Tac-Toe/blob/master/Tic-Tac-Toe.py

#board
board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-",]

#game is going
game_going = True
real_going = True
#winner
winner = None
#player
# "X" is a human and "O" is a computer
current_player = "X"

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_validity(position):
    pos = int(position)
    if pos<=0 or pos>9:
        return False

    if board[pos-1] != "-":
        return False

    return True


def handle_turn(current_player):
    if current_player=="X": #human player can select position
        position =(input("Choose a position to from 1-9: "))

        validity = check_validity(position)
        while validity == False:
            position = input("Invalid input! Choose another")
            validity = check_validity(position)

        board[int(position)-1] = current_player
        print_board()

    else:   #computer should select position based on random playouts.
        position = best_move()
        board[position] = current_player
        print_board()

def get_emptypositions():
    lst = []
    for i in range(9):
        if board[i] == "-":
            lst.append(i)

    return lst

def best_move():
    possible_positions = get_emptypositions()
    results = [None]*len(possible_positions)
    for i in range(len(possible_positions)):
        results[i] = random_playouts(possible_positions[i])

    print("Simulation result that might loose")
    for i in range(len(results)):
        print(possible_positions[i]+1,":",results[i], end="   ")
    print()

    return possible_positions[results.index(min(results))]

def rand_turn(current_player):
    possible_positions = get_emptypositions()
    next_pos = random.choice(possible_positions)
    board[next_pos] = current_player

#return how many time lose when play 50 games
#simulating game
def random_playouts(possible_position):
    global game_going
    global board
    global winner
    global current_player

    backup_board = copy.deepcopy(board)
    backup_gamegoing = game_going
    backup_winner = winner
    backup_current_player = current_player

    lose = 0
    win = 0
    count=0
    #simulate 3000 times and calculate which positions might be best
    for i in range(3000):
        #print("i:", i)
        count +=1
        board = copy.deepcopy(backup_board)
        board[possible_position] = "O"
        while game_going:
            #print("check")
            rand_turn(current_player)
            check_gameover()
            flip_player()

            if winner =="X":
                lose +=1
                break
            if winner == "O":
                win +=1
                break

        game_going = True


    board = copy.deepcopy(backup_board)
    game_going = backup_gamegoing
    winner = None
    current_player = backup_current_player
    #print("lose", lose, " win", win)
    return lose


def check_gameover():
    check_win()
    check_tie()


def check_win():
    global winner

    #check rows
    row_winner = check_row()
    #check column
    column_winner = check_column()
    #check diagonnals
    diagonal_winner = check_diagonal()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner= column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner = None

    return

def check_row():
    global game_going
    row1 = board[0] == board[1] == board[2] !="-"
    row2 = board[3] == board[4] == board[5] !="-"
    row3 = board[6] == board[7] == board[8] !="-"

    if row1 or row2 or row3:
        game_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_column():

    global game_going
    column1 = board[0] == board[3] == board[6] !="-"
    column2 = board[1] == board[4] == board[7] !="-"
    column3 = board[2] == board[5] == board[8] !="-"

    if column1 or column2 or column3:
        game_going = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def check_diagonal():
    global game_going
    diagonal1 = board[0] == board[4] == board[8] !="-"
    diagonal2 = board[2] == board[4] == board[6] !="-"

    if diagonal1 or diagonal2 :
        game_going = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return


def check_tie():
    global game_going

    if "-" not in board:
        game_going= False
    return


def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def play_a_new_game():
    print_board()

    while game_going:
        print()
        print(current_player+"Turns")
        print()
        handle_turn(current_player)
        check_gameover()
        flip_player()

    if winner=="X" or winner=="O":
        print(winner+"Won")
    elif winner==None:
        print("TIE!!")

if __name__ == '__main__':
  play_a_new_game()
