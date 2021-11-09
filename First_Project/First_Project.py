
'''
Tic tac toe clone
Written by Canahedo
'''

#Imports
import os #Used for clearConsole()

#Variable creation
debug = 0 #If 1, enables debug/verbose features.

#Board initialization
board = [["_"] * 3 for i in range(3)] #creates 3x3 board

##################################################
#Functions

def clearConsole(): #Clears the screen between turns
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def board_state(): #Prints current board, formatted
    for row in board:
        for cell in row:
            print(cell, end = "  ")
        print("\n")

def turn_counter(current_turn): #Determines whose turn it is and prints to screen
    if current_turn % 2 == 1:
        active_player = "X"
    else:
        active_player = "O"

    print("It is " + active_player + "'s turn.")
    return active_player

def header():#Prints text and draws board
    clearConsole()
    print("Welcome to Tic-Tac-Toe!")
    print("Squares are numbered 1-9, left to right, top to bottom.")
    board_state()
   
def conv_move(move): #Converts move into row and column, starting in square 1
    col = (move % 3) - 1
    if col == -1:col = 2
    row = (move - 1) // 3
    return row, col

def req_move(board): #Requests, accepts input from active player, returns input as row, col
    while True:
        try:
            move = int(input("Choose a square!: ")) #Takes input, converts to int
            row, col = conv_move(move) #Runs input through convert function 
            if move < 1 or move > 9: #Rejects input if too high or low
                print("\nInvalid entry, please choose a number from 1-9.")
                continue
            elif board[row][col] != "_":#Rejects input if that square was already taken
                print("\nPlease choose an empty square.")
                continue
            break
        except: #Rejects input if int conversion fails (if input is string)
            print("\nInvalid entry, please choose a number from 1-9.")
    return(row, col)


######################################################
######################################################
#Start of program


for current_turn in range(1,10):
    header()
    active_player = turn_counter(current_turn)
    row, col = req_move(board)
    board[row][col] = active_player
    

header()    
print("End\n")






    



















