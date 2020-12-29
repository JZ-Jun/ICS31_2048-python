from utilities import place_random, print_board

DEV_MODE = False

def update_board(game_board: [[int, ], ], keyboard_input: "") -> [[int, ], ]:
    tmp_row = []
   
    if keyboard_input == "a":  # sum numbers from left
        for i in range(4):
            # step 1: remove all 0s in list
            tmp_row = [k for k in game_board[i] if k != 0]
            if len(tmp_row) > 1:
                # step 2: sum tmp row's value
                for j in range(1, len(tmp_row)):
                    if (tmp_row[j] != 0) and (tmp_row[j] == tmp_row[j - 1]):
                        tmp_row[j - 1] = tmp_row[j] * 2
                        tmp_row[j] = 0;

            tmp_row = [k for k in tmp_row if k != 0]
            for l in range(4 - len(tmp_row)):
                tmp_row.append(0)
            game_board[i] = tmp_row
            #print(game_board)

    elif keyboard_input == "d":  # sum numbers from left
        for i in range(4):
            # step 1: remove all 0s in list
            tmp_row = [k for k in game_board[i] if k != 0]
            tmp_row.reverse()
            if len(tmp_row) > 1:
                # step 2: sum tmp row's value
                for j in range(1, len(tmp_row)):
                    if (tmp_row[j] != 0) and (tmp_row[j] == tmp_row[j - 1]):
                        tmp_row[j - 1] = tmp_row[j] * 2
                        tmp_row[j] = 0;

            tmp_row = [k for k in tmp_row if k != 0]
            for l in range(4 - len(tmp_row)):
                tmp_row.append(0)
            tmp_row.reverse()
            game_board[i] = tmp_row
            #print(game_board)
            
    elif keyboard_input == 'w':
        game_board
        for i in range(4):
            tmp_col = []
            for n in range(4):
                if (game_board[n][i] != 0):
                    tmp_col.append(game_board[n][i])
                    
            if len(tmp_col) > 1:
                for j in range(1, len(tmp_col)):
                    if (tmp_col[j] != 0) and (tmp_col[j] == tmp_col[j-1]):
                        tmp_col[j-1] = tmp_col[j]*2
                        tmp_col[j] = 0
                        
            tmp_col = [k for k in tmp_col if k != 0]
            for l in range(4 - len(tmp_col)):
                tmp_col.append(0)
            for m in range(4):
                game_board[m][i] = tmp_col[m]
                
    elif keyboard_input == 's':
        for i in range(4):
            tmp_col = []
            for n in range(4):
                if (game_board[n][i] != 0):
                    tmp_col.append(game_board[n][i])
                    
            tmp_col.reverse()
            if len(tmp_col) > 1:
                for j in range(1, len(tmp_col)):
                    if (tmp_col[j] != 0) and (tmp_col[j] == tmp_col[j-1]):
                        tmp_col[j-1] = tmp_col[j]*2
                        tmp_col[j] = 0
                        
            tmp_col = [k for k in tmp_col if k != 0]
            for l in range(4 - len(tmp_col)):
                tmp_col.append(0)
            tmp_col.reverse()
            for m in range(4):
                game_board[m][i] = tmp_col[m]
    
    return game_board

def main(game_board):
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell

    # You are not required to implement develop mode, but it is encouraged to do so.
    # Develop mode allows you to input the location of the next piece that will be
    # placed on the board, rather than attempting to debug your code with random
    # input values.
    if DEV_MODE:
        # This line of code handles the input of the develop mode.
        column, row, value = (int(i) for i in input("column,row,value:").split(','))

        # OPTIONAL: place the piece in the corresponding cell on the game board
    else:
        # TODO: generate a random piece and location using the place_random function
        gen = place_random(game_board)
        row = gen['row']
        column = gen['column']
        value = gen['value']
        
        # TODO: place the piece at the specified location
        game_board[row][column] = value
        pass

    # Initialize game state trackers

    # Game Loop
    while True:
        # break
        # TODO: Reset user input variable
        keyboard_input = ""
        valid_input_list = ["w", "a", "s", "d", "q"]
        while keyboard_input not in valid_input_list:
            #read input
            keyboard_input = input()
        
        # TODO: Take computer's turn
        # place a random piece on the board
        gen = place_random(game_board)
        row = gen['row']
        column = gen['column']
        value = gen['value']
        game_board[row][column] = value
        # check to see if the game is over using the game_over function
       
        # TODO: Show updated board using the print_board function
        print_board(game_board)
        # TODO: Take user's turn
        game_board = update_board(game_board, keyboard_input)
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move
        
        if(keyboard_input == 'q'):
            print('Goodbye')
            print_board(game_board)
            break      

        # Check if the user wins
        if game_pass(game_board):
            break

        if(game_over(game_board)):
            print('Game Over, You Lost')
            print_board(game_board)
            break
           
    return game_board
 

def game_pass(game_board: [[int, ], ]) -> bool:
    if any(2048 in x for x in game_board):
        return True
    else:
        return False

def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    for i in range(4):
        for j in range(4):
            if game_board[i][j] < 2 :
                return False
    for i in range(4):
        for j in range (4):
            if i <= 2:
                #up and down
                if game_board[i][j] == game_board[i+1][j]:
                    return False
            if j <= 2:
                if game_board[i][j] == game_board[i][j+1]:
                    return False
    return True  # TODO: Don't always return false

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])

