import connectfour

# Print Module
# The board should always be shown in a fixed format
# The game should repeatly remind the player of whose turn is next

def print_screen(game_state: connectfour.ConnectFourGameState) -> None:  
    ''' Print the board in a fixed format, '.' represents no piece
    '''
    for i in range(1,connectfour.BOARD_COLUMNS+1):
        print(i,end=' ')
    print()
    for row in range(connectfour.BOARD_ROWS):   
        for col in range(connectfour.BOARD_COLUMNS): 
            if game_state.board[col][row] == connectfour.NONE:
                pixel = '.'
            else:
                pixel = game_state.board[col][row]
            print(pixel,end=' ')
        print() 
    return

def print_turn(game_state: connectfour.ConnectFourGameState) -> None:
    '''The game should repeatly remind the player of whose turn is next
    '''
    
    print("{}'s turn is next".format(game_state.turn))
    return

#input module
def collect_player_command()->str:
    '''return the command of the player
    '''
    while True:
        command=input('''\nEnter how you want to do with the piece ---
Enter examples:
    DROP 1: To drop a piece at the first column 
    POP 5: To pop a piece at the fifth column
Your input is: ''').strip()
        if command.split()[0]=='DROP' and type(eval(command[-1]))==int :
            break
        elif command.split()[0]=='POP' and type(eval(command[-1]))==int:
            break
        print('invalid input! please try again')
        
    return command

# drop or pop
def game_each_move(command:str,column_number:int,game_state:connectfour.ConnectFourGameState)->connectfour.ConnectFourGameState:
    '''each move for the game
    '''
    try:
        if command=='D':
            game_state=connectfour.drop_piece(game_state,column_number)
        elif command=='P':
            game_state=connectfour.pop_piece(game_state,column_number)
    except connectfour.InvalidConnectFourMoveError:
        print('Invalid move! Please try again')
    except ValueError:
        print('column_number must be int between 0 and {}'.format(connectfour.BOARD_COLUMNS))
    return game_state       
  
# winner       
def check_for_winner(winner:str)->bool:
    '''check if the game is over, and return True if the game is over
    '''
    if winner==connectfour.RED:
        print('Red wins!')
        return True
    elif winner==connectfour.YELLOW:
        print('Yellow wins!')
        return True
    return False
