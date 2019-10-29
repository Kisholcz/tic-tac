game_time = None

def is_winner(playerChar):
        if board[0][0] == playerChar and board[0][1] == playerChar and board[0][2] == playerChar:
                return True
        elif board[0][1] == playerChar and board[1][1] == playerChar and board[2][1] == playerChar:
                return True        
        elif board[1][0] == playerChar and board[1][1] == playerChar and board[1][2] == playerChar:
                return True
        elif board[2][0] == playerChar and board[2][1] == playerChar and board[2][2] == playerChar:
                return True
        elif board[0][0] == playerChar and board[1][0] == playerChar and board[2][0] == playerChar:
                return True
        elif board[1][0] == playerChar and board[1][1] == playerChar and board[1][2] == playerChar:
                return True
        elif board[2][0] == playerChar and board[2][1] == playerChar and board[2][2] == playerChar:
                return True
        elif board[0][0] == playerChar and board[1][1] == playerChar and board[2][2] == playerChar:
                return True
        elif board[0][2] == playerChar and board[1][1] == playerChar and board[2][0] == playerChar:
                return True
        else:
                return False

# def is_winnero():
#         if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
#                 return True
#         elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
#                 return True        
#         elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
#                 return True
#         elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
#                 return True
#         elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
#                 return True
#         elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
#                 return True
#         elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
#                 return True
#         elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
#                 return True
#         elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
#                 return True
#         else:
#                 return False
# def is_winnerx():
        # if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        #         return True
        # elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        #         return True
        # elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        #         return True
        # elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        #         return True
        # elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        #         return True
        # elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        #         return True
        # elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        #         return True
        # elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        #         return True
        # elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        #         return True
        # else:
        #         return False
            #kimaradt egy sor középső oszlop nem nyer
def main_menu():
        global board
        global game_time
        game_time = None
        print("Welcome to the game!\nType START to begin the game!\nType QUIT to exit!")
        menu_input = str(input("what's your choice?"))
        if menu_input == "START" or menu_input == "start":
                import os
                os.system('clear')
                # global game_time
                board = [["." , "." , "."] , ["." , "." , "."] , ["." , "." , "."]]
                game_time = 1
                print_board()
                return board
        elif menu_input == "QUIT" or menu_input == "quit":
                exit()
def input_player1():
        import time
        col =5
        row =5
        while col == 5 or row  ==5:
                while col == 5 :
                        user_input_col1 = str(input("Player 1, enter your column: "))
                        if user_input_col1 == '1':
                                col = 0
                        elif user_input_col1 == '2':
                                col = 1
                        elif user_input_col1 == '3':
                                col = 2
                        elif user_input_col1 == "quit":
                                exit()
                        else:
                                print("Please enter a valid column.")
                while row == 5 :
                        user_input_row1 = input("Player 1, enter your row: ")
                        if user_input_row1 == "a":
                                row = 0
                        elif user_input_row1 == "b":
                                row = 1
                        elif user_input_row1 == "c":
                                row = 2
                        elif user_input_row1 == "quit":
                                exit()        

                        else:
                                print("Please enter a valid row.")
                if board[row][col] != ".":
                        print("Don't try to cheat...")
                        time.sleep(2)
                        row = 5
                        col = 5 
        board[row][col]="x"
        import os
        os.system('clear')
        print_board()
        if is_winner('x'):
                print("The winner player is X. ")
                global game_time
                exitx = input("press e to quit:\npress n to menu:")
                if exitx == "e":
                        exit()
                elif exitx == "n":
                        game_time = 0
                        main_menu()
                else:
                        print("quit anyway")
                        exit()
def input_player2():
        import time
        col = 5
        row = 5
        while col == 5 or row == 5:
                while col == 5 :
                        user_input_col2 = str(input("Player 2, enter your column: "))

                        if user_input_col2 == '1':
                                col = 0
                        elif user_input_col2 == '2':
                                col = 1
                        elif user_input_col2 == '3':
                                col = 2
                        elif user_input_col2 == "quit":
                                exit()        
                        else:
                                print("Please enter a valid column.")

                while row ==5 :
                        user_input_row2 = input("Player 2, enter your row: ")
                        if user_input_row2 == "a":
                                row = 0
                        elif user_input_row2 == "b":
                                row = 1
                        elif user_input_row2 == "c":
                                row = 2
                        elif user_input_row2 == "quit":
                                exit()
                        else:
                                print("Please enter a valid row.")
                if board[row][col] !=".":
                        print("Don't try to cheat...")
                        row = 5
                        col = 5    
        board[row][col]="o"
        import os
        os.system('clear')
        print_board()
        if is_winner('o'):
                global game_time
                print("The winner player is O. ")
                exito = input("press e to quit\npress n to menu:")
                if exito == "e":
                        exit()
                elif exito == "n":
                        game_time = 0
                        main_menu()     
                else:
                        print("quit anyway")
                        exit()
def print_board():
    # os.system('clear')
    print("     1 " + "- 2" + " - 3  ")
    print("A--| " + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " | ")
    print("   |---+---+---|")
    print("B--| " + str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " | ")
    print("   |---+---+---|")
    print("C--| " + str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " | ")
def is_full():
        if "." in board[0]:
                global game_time
                game_time = 1
        elif "." in board[1]:
                game_time = 1
        elif "." in board[2]:
                game_time = 1
        else:
                game_time = 0
                import os
                os.system('clear')
                print("TIE!!!!!!  U BOTH SUCKS")
                return False

print("  _____ _         _____             _____          ")
print(" |_   _(_) ___   |_   _|_ _  ___   |_   _|__   ___ ")
print("   | | | |/ __|____| |/ _` |/ __|____| |/ _ \ / _ \ ")
print("   | | | | (_|_____| | (_| | (_|_____| | (_) |  __/ ")
print("   |_| |_|\___|    |_|\__,_|\___|    |_|\___/ \___| ")
board = [["." , "." , "."] , ["." , "." , "."] , ["." , "." , "."]]
main_menu()
while game_time ==1: 
        input_player1()
        if is_full() is False:
                full = input(str("want to play again? y/n"))
                if full == "y":
                        main_menu()
                if full == "n":
                        break
        input_player2()
        if is_full() is False:
                full = input(str("want to play again? y/n"))
                if full == "y":
                        main_menu()
                if full == "n":
                        break



