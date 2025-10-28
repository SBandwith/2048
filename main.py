# Name: Saina Bhandari
# Period: 6
# Date Last Edited: 10/22/2025

"""
Abstraction Reference Guide:
    main                - responsible for starting the game and directing control to each function, the tests, or quitting
        board           - a variable within main that contains the current board and is passed to most functions as an argument
    System Functions:
        get_key_press   - returns the user's key_press input as an ascii value
        clear           - clears the screen (should be called before each print_board call)
        pause           - a function used by the GUI to allow for a slight delay that is more visually appealing in placing the new piece
    Board Functions:
        make_board      - creates a new, empty square board of N x N dimension
        print_board     - prints out the state of the argument board
        board_full      - returns True if the board is full and False otherwise
    Logic:
        swipe_right     - simulates a right swipe on the argument board
        swipe_left      - simulates a left swipe on the argument board
        swipe_up        - simulates a upward swipe on the argument board
        swipe_down      - simulates a downward swipe on the argument board
        swap            - occurs when the spacebar is pressed and randomly switches two different numbers on the board
        swap_possible   - a helper function that returns True if a swap is possible and False otherwise
    Useful Helper Functions:
        get_piece       - gets the piece from the given board at the given (x,y) coordinates or returns None if the position is invalid
        place_piece     - places the given piece on the given board at the given (x,y) coordinates and returns True or returns False if the position is invalid
        place_random    - user implemented function which places a random 2 OR 4 OR 8 in an empty part of the board
        have_lost       - responsible for determining if the game has been lost yet (no moves remain)
        move_possible   - responsible for determining if a move is possible from a single position
        move            - responsible for moving a piece, at the given (x,y) coordinates in the given direction on the given board
"""

def main():
    #Initialize a new leaderboard
    leaderboard = {}

    #Creating a new board
    board = initBoard()

    #Runs the game loop until the user quits or the game is lost
    while True:

        #Gets the key pressed and stores it in the key variable
        #Hint: look at the available functions in the "Abstraction Reference Guide"
        #starting on line 2. You'll use those functions throughout the
        #project.
        key = get_key_press()
        #Quit case ('q')
        if key == 113:
            print("Bye bye!")
            quit()

        #Up arrow
        elif key == 72:
            swipe_up(board)

        #Down arrow
        elif key == 80:
            swipe_down(board)

        #Right arrow
        elif key == 77:
            swipe_right(board)

        #Left arrow
        elif key == 75:
            swipe_left(board)

        #Space bar (swap)
        elif key == 32:
            if swap_possible(board):
                swap(board)
            else:
                print("You can't swap")

        #Check to see if I've lost at the end of the game or not
        if have_lost(board):

            # This will be zero until you complete the final steps of the project
            score = compute_score(board)
            input1 = input('Game over! Your score is ' + str(score) + '. Press enter to continue..')
            process_leaderboard(leaderboard, score)
            print_leaderboard(leaderboard)

            print("Would you like to play again? (y/n) ")

            if (input().lower() == 'y'):
                board = initBoard()
            else:
                quit()

def initBoard():
    #Creating my new 4x4 board
    board = make_board(4)

    #Getting the game started with a single piece on the board
    place_random(board)
    print_board(board)

    return board

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def get_piece(x, y, board):
    """
    Utility function that gets the piece at a given (x,y) coordinate on the given board
    Returns the piece if the request was valid and None if the request was not valid
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to get the piece from
    """
    
    #Ensure that x and y are both integers (use assert)
    assert type(x) == int and type(y) == int, "Values must be integers"

    #What does this do?
    N = len(board)

    #Checking that the (x,y) coordinates given are valid for the N x N board
    if (x >= len(board) or x < 0) or (y >= len(board) or y < 0):
        return None

    #Getting the piece on the board
    return board[y][x]


def place_piece(piece, x, y, board):
    """
    Utility function that places the piece at a given (x,y) coordinate on the given board if possible
    Will overwrite the current value at (x,y), no matter what that piece is
    Returns True if the piece is placed successfully and False otherwise
    Arg piece: string - represents a piece on the board ('*' is an empty piece, '2' '8' etc. represent filled spots)
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to place the piece on
    """
    
    #Ensure that x and y are both integers (use assert)
    assert type (x) == int and type(y) == int, "Values must be strings"

    #What are the dimensions of the board?
    N = len(board)

    #Checking that the (x,y) coordinates given are valid for the board
    if (x >= len(board) or x < 0) or (y >= len(board) or y < 0):
        return False

    #Placing the piece on the board
    #Note how it's y (row), then x (column)
    board[y][x] = piece
    return True

#End of Step 1 #############################################################################################


#Start of Step 2 ###########################################################################################

def place_random(board):
    """
    Helper function which is necessary for the game to continue playing
    Returns True if a piece is placed and False if the board is full
    Places a 2 (60%) or 4 (37%) or 8 (3%) randomly on the board in an empty space
    Arg board: board - the board you wish to place the piece on
    """
    
    #Check if the board is full and return False if it is
    count = 0

    for row in board:
        for space in row:
            if not "*" in row:
                count+=1
    if count == len(space)*len(space):
        return False

    N = len(board)
    #random.random() generates a random decimal between [0, 1) ... Multiplying by 100 generates a number between [0, 100)
    generated = random.random() * 100

    #Assign to_place according to my generated random number

    if generated < 61:                              #YOUR CODE HERE (replace -1) <<<<<
        to_place = "2"

    elif generated < 96 and generated >= 61:        #YOUR CODE HERE (replace -1) <<<<<
        to_place = "4"

    else:
        #What should to_place be if it's not a 2 or 4?
        to_place = "8"


    #Variable keeps track of whether a randomly generated empty spot has been found yet
    found = False
    N = len(board)

    while not found:
        #Generate a random (x,y) coordinate that we can try to put our new value in at
        #How did we "generate" a random number earlier? (hint: x and y should be between [0, N) )
        random_y = random.randint(0, N)
        random_x = random.randint(0, N)


        #If the randomly generated coordinates are empty, we have found a spot to place our random piece
        found = get_piece(random_x, random_y, board) == '*'
        if found:
            #Place the piece at the randomly generated (x,y) coordinate
            place_piece(to_place, random_x, random_y, board)


    return True

#End of Step 2 #############################################################################################


#Start of Step 3 ###########################################################################################

def have_lost(board):
    """
    Helper function which checks at the end of each turn if the game has been lost
    Returns True if the board is full and no possible turns exist and False otherwise
    Arg board: board - the board you wish to check for a losing state
    """


    N = len(board)

    #Check every (x,y) position on the board to see if a move is possible
    for y in range(N):
        for x in range(N):
            if board_full(board) == True and move_possible(x, y, board) == False:
                return True
    return False

#End of Step 3 #############################################################################################


#Start of Step 4 ###########################################################################################

def end_move(board):
    """
    Prints the board after a swipe, pauses for .2 seconds, places a new random piece and prints the new state of the board
    Arg board: board - the board you're finishing a move on
    """
    
    #Print the board
    clear()
    print_board(board)

    #Pause for .2 seconds
    pause(0.2)

    #Place a random piece on the board at a random (x,y) position
    place_random(board)

    #Print the board again
    clear()
    print_board(board)

#End of Step 4 #############################################################################################



#Start of Step 5 ###########################################################################################

def swipe_left(board):
    """
    YOUR COMMENT HERE (WHAT DOES THIS FUNCTION DO?)
    Arg board: board - (WHAT IS A BOARD ARGUMENT?)
    """
    
    #Action_taken is a variable that stores a boolean value which represents if the player has done a move
    action_taken = False

    #This is storing the dimensions of the square board in the variable N
    N = len(board)

    #Checks if the move is valid
    for y in range(N):
        for x in range(N):
            #Calls the function get_piece and assigns it at piece_at_xy, and calls it again to assign it to left_adjacent to check the places and see if it valid to swipe left
            piece_at_xy = get_piece(x, y, board)
            left_adjacent = get_piece(x-1, y, board)

            #Checks if the piece is empty, stop the iteration of the loop if it is
            if piece_at_xy == '*':
                continue

            #Checks if the function is invalid at the that point
            if left_adjacent == None:
                continue

            #If both of the previous statements are true, then the action_taken variable will be true since the player will be able to swipe right
            action_taken = move(x, y, "left", board) or action_taken


    #If the player has finished their move, then the program will execute the code to end the move
    if action_taken:
        end_move(board)

def swipe_right(board):
    #Action_taken is a variable that stores a boolean value which represents if the player has done a move
    action_taken = False

    #This is storing the dimensions of the square board in the variable N
    N = len(board)

    #Checks if the move is valid
    for y in range(N):
        for x in range(N):
            #Adjusting for coordinate perspective
            x = N-1-x

            #Calls the function get_piece and assigns it at piece_at_xy, and calls it again to assign it to left_adjacent to check the places and see if it valid to swipe left
            piece_at_xy = get_piece(x, y, board)
            right_adjacent = get_piece(x+1, y, board)

            #Checks if the piece is empty, stop the iteration of the loop if it is
            if piece_at_xy == '*':
                continue
            
            #Checks if the function is invalid at the that point
            if right_adjacent == None:
                continue
            
            #If both of the previous statements are true, then the action_taken variable will be true since the player will be able to swipe right
            action_taken = move(x, y, "right", board) or action_taken

    #If the player has finished their move, then the program will execute the code to end the move
    if action_taken:
        end_move(board)

def swipe_up(board):
    #Action_taken is a variable that stores a boolean value which represents if the player has done a move
    action_taken = False

    #This is storing the dimensions of the square board in the variable N
    N = len(board)

    #Checks if the move is valid
    for y in range(N):
        for x in range(N):
            #Calls the function get_piece and assigns it at piece_at_xy, and calls it again to assign it to left_adjacent to check the places and see if it valid to swipe left
            piece_at_xy = get_piece(x, y, board)
            up_adjacent = get_piece(x, y-1, board)

            #Checks if the piece is empty, stop the iteration of the loop if it is
            if piece_at_xy == '*':
                continue

            #Checks if the function is invalid at the that point
            if up_adjacent == None:
                continue
            
            #If both of the previous statements are true, then the action_taken variable will be true since the player will be able to swipe right
            action_taken = move(x, y, "up", board) or action_taken

    #If the player has finished their move, then the program will execute the code to end the move
    if action_taken:
        end_move(board)

def swipe_down(board):
    #Action_taken is a variable that stores a boolean value which represents if the player has done a move
    action_taken = False

    #This is storing the dimensions of the square board in the variable N
    N = len(board)

    #Checks if the move is valid
    for y in range(N):
        #Adjusting for coordinate perspective
        y = N-1-y

        for x in range(N):
            #Calls the function get_piece and assigns it at piece_at_xy, and calls it again to assign it to left_adjacent to check the places and see if it valid to swipe left
            piece_at_xy = get_piece(x, y, board)
            down_adjacent = get_piece(x, y+1, board)

            #Checks if the piece is empty, stop the iteration of the loop if it is
            if piece_at_xy == '*':
                continue

            #Checks if the function is invalid at the that point
            if down_adjacent == None:
                continue

            #If both of the previous statements are true, then the action_taken variable will be true since the player will be able to swipe right
            action_taken = move(x, y, "down", board) or action_taken

    #If the player has finished their move, then the program will execute the code to end the move
    if action_taken:
        end_move(board)

#End of Step 5 #############################################################################################


#Start of steps 6 and 7 ####################################################################################   - Section 3 -


def swap(board):
    """
    Note: have_lost does not take into account possible swaps that can "save the day". This is expected behavior.
    """
    N = len(board)

    #Check that a swap can occur on the board -- use the provided function, return False if a swap is not possible
    if swap_possible(board) != True:
        return False

    #Getting the first random piece to swap
    random_x1 = None
    random_x2 = None
    random_y1 = None
    random_y2 = None
    first_random_piece = None
    second_random_piece = None
    found = False
    while not found:

        # Pick a random x and y position within the board boundaires, store them in the
        # appropriate variables
        random_y1 = random.randint(0, N-1)
        random_x1 = random.randint(0, N-1)

        # Get the piece from that position and store it in the appropriate variable
        first_random_piece = get_piece(random_x1, random_y1, board)

        # If that piece is NOT "empty" (an asterisk), set found to True and store it
        if first_random_piece != "*":
            found = True
            break

    # Do it again, with the second random piece
    found = False
    while not found:
        # Pick a random x and y position within the board boundaires, store them in the
        # appropriate variables
        
        random_y2 = random.randint(0, N-1)
        random_x2 = random.randint(0, N-1)

        #Ensuring the two values are not the same
        if random_y2 == random_y1 and random_x2 == random_x1:
            continue

        # Get the piece from that position and store it in the appropriate variable
        second_random_piece = get_piece(random_x2, random_y2, board)

        # If that piece is NOT "empty" (an asterisk), set found to True and store it
        if second_random_piece != "*":
            found = True
            break


    #Swap the first and second pieces using place piece and the random x/y values
    place_piece(first_random_piece, random_x2, random_y2, board)
    place_piece(second_random_piece, random_x1, random_y1, board)
    
    # print the board again
    clear()
    print_board(board)
    
    #An action was taken, so return true
    return True


def swap_possible(board):
    """
    Helper function for swap
    Returns True if a swap is possible on the given board and False otherwise
    """
    
    # A set is like a list, but it can't have duplicate values
    container = set()
    N = len(board)
    
    for y in range(N):
        for x in range(N):
            piece_at_xy = get_piece(x, y, board)
            if piece_at_xy == "*":
                continue
            container.add(piece_at_xy)

            #Don't add empty spaces (they obviously can't be swapped...)
            #If the piece_at_xy is not empty... add it to the set using container.add(...)

    unique_pieces = len(container)

    # If there are fewer than 2 unique pieces, print "Can't swap" and return False, otherwise Return True
    if unique_pieces < 2:
        print("Can't Swap")
        return False
    return True


#End of steps 6 and 7 ######################################################################################

#Start of step 8 ###########################################################################################

def compute_score(board):
    N = len(board)
    totalScore = 0
    # Use nested for loops to add up the pieces on the board to calculate the score
    for row in board:
        for space in row:
            if space != "*":
                totalScore+=int(space)        
    return totalScore

def process_leaderboard(leaderboard, current_game_score):
    # First, calculate the total number of scores currently in the leaderboard
    totalLeaderboard = len(leaderboard)

    # Then compare the current_game_score to existing scores to determine
    # if the current_game_score should be stored in the leaderboard.
    min = current_game_score
    inLeaderBoard = False
    removeFromLeaderboard = []
    for key in leaderboard:        
        if len(leaderboard) >= 5 and current_game_score > leaderboard[key]:
            name = input("Please enter your name: ")
            inLeaderBoard = True
        if len(leaderboard) >= 5 and current_game_score > leaderboard[key]:
            if leaderboard[key] < min:
                min = leaderboard[key]
                removeFromLeaderboard.append[key, min]
    if len(leaderboard) >= 5 and current_game_score > leaderboard[key]:
        leaderboard.pop[removeFromLeaderboard[len(removeFromLeaderboard)-3], "Key doesn't exist"]

    if len(leaderboard) < 5:
            name = input("Please enter your name: ")
            leaderboard[name] = current_game_score  
            inLeaderBoard = True
    if name in leaderboard.keys():
        if current_game_score > leaderboard[name]:
            leaderboard[name] = current_game_score
      
    #Add player name, to the function parameter

    # If the current score is a high score, prompt the user for their name
    # with input()
    # # # # If there are already five scores stored in the leaderboard, you
    # # # # will need to determine which score to remove and remove it so that
    # # # # the new current score can fit (max of 5 scores in leaderboard)
    #
    # Finally, add/update the Name in the leaderboard with the current score

    # You do not need to return anything from this function, changes made to leaderboard
    # will reflect elsewhere in the code.

#Update + Print
def print_leaderboard(leaderboard):
    ## Do not change the next two lines of code ####################
    import copy
    copied_leaderboard = copy.deepcopy(leaderboard)
    ## This will be very similar to the Part 2 of A59, where you needed to remove values
    ## from the dictionary in order to figure out the rankings of word frequencies.
    ## Since the leaderboard needs to remain unchanged for the next game, we can make a
    ## COPY of the leaderboard in the variable copied_leaderboard. Do not pop() values from
    ## the main leaderboard variable in this function, only change copied_leaderboard.
    clear()
    keys = []
    leaderboardKeys = sorted(copied_leaderboard.keys())
    sorted_values = sorted(copied_leaderboard.values(), reverse=True)
    for i in range(len(sorted_values)):
        for j in range(len(sorted_values)):
            if sorted_values[i] == copied_leaderboard[leaderboardKeys[j]]:
                keys.append(leaderboardKeys[j])

    print("Leaderboard for 2048")
    for i in range(len(copied_leaderboard)):
        print(str(i+1) + ": " + keys[i] + " - " + str(sorted_values[i]))
    


#End of third section

############################################################################################################
################################## DO NOT CHANGE ANYTHING BELOW THIS LINE ##################################   - Section 4 -
############################################################################################################

from utils import *

import subprocess
import sys

if __name__ == "__main__":
    #Only want to see the game board at the top
    clear()
    
    #Starting the game
    main()
