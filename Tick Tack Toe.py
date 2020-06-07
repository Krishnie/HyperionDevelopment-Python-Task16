# importing os module
import os
os.system("clear")
class XO_Board():
    ''' This class represents boards'''
    def __init__(self):
        self.position = [" "," "," "," "," "," "," "," "," "]

    def display(self):
        ''' This method prints an  3 by 3 board '''
        print (" %s | %s | %s" %(self.position[0],self.position[1],self.position[2]))
        print ("-----------")
        print (" %s | %s | %s" %(self.position[3],self.position[4],self.position[5]))
        print ("-----------")
        print (" %s | %s | %s" %(self.position[6],self.position[7],self.position[8]))
       
        print("")
        
    def update_position(self,position_no, player):
        ''' This method passes the  postion no entered and the player as the parameters and places the player on the position.'''  
        if self.position[position_no] == " ":
            self.position[position_no] = player

    def is_winner (self, player):
        ''' This method passes the player as the parameters and  returns True for every possible winning combination for that player'''

        if self.position[0] == player and self.position[1] == player and self.position[2] == player:
            return True
        if self.position[3] == player and self.position[4] == player and self.position[5] == player:
            return True
        if self.position[6] == player and self.position[7] == player and self.position[8] == player:
            return True
        if self.position[0] == player and self.position[3] == player and self.position[6] == player:
            return True
        if self.position[1] == player and self.position[4] == player and self.position[7] == player:
            return True
        if self.position[2] == player and self.position[5] == player and self.position[8] == player:
            return True
        if self.position[0] == player and self.position[4] == player and self.position[8] == player:
            return True
        if self.position[2] == player and self.position[4] == player and self.position[6] == player:
            return True
        return False
    
    def draw_game(self):
        ''' this method return true if all the positions are filled and false if it is not filled.'''

        is_filled = 0
        for position in self.position:
              if position != " ":
                  is_filled +=1
        if  is_filled == 9:
             return True
        else:
           return False
         
    def reset (self):
        ''' This method reset the positions all to empty.'''
        self.position = [" "," "," "," "," "," "," "," "," "]
board = XO_Board()

        
def print_welcome():
    ''' This method prints a message to the user.'''
    print(" Welcome to Tic-Tac-Toe ")

def refresh_board():
    ''' This method updates the board.'''
    os.system("clear")
    print_welcome()
    board.display()


while True:
    refresh_board()
    # X Player1
    x_choice = int(input(" PlayerX \n Please choose a position  1 - 9 where 1 starts at the top left corner going from left to right: ")) 
    assert( x_choice <= 9), "This code takes only the natural number 1-9."
    x_choice -=1
    board.update_position(x_choice, "X")
    refresh_board()
    if board.is_winner("X") == True:
        print("Congratulations, X wins !")
        play_again = input("Would you like to play again?(Yes/No)").title()
        if play_again == "Yes":
            board.reset()
            continue
        else:
            break
    if board.draw_game() == True:
        print(" Game is drawn ")
        play_again = input("Would you like to play again?(Yes/No)").title()
        if play_again == "Yes":
            board.reset()
            continue
        else:
            break
    # O Player
    o_choice = int(input(" PlayerO \n Please choose a position  1 - 9 where 1 starts at the top left corner going from left to right: "))
    assert(o_choice <= 9), "This code takes only the natural number." 
    o_choice -=1
    board.update_position(o_choice, "O")
    refresh_board()
    if board.is_winner("O") == True:
        print("Congratulations,O wins !")
        play_again = input("Would you like to play again?(Yes/No)").title()
        if play_again == "Yes":
            board.reset()
            continue
        else:
            break
    if board.draw_game() == True:
        print(" Game is drawn ")
        play_again = input("Would you like to play again?(Yes/No").title()
        if play_again == "Yes":
            board.reset()
            continue
        else:
            break
