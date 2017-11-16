import connectfour
import functions_for_both

#handle command
def handle_commands(game_state: connectfour.ConnectFourGameState)->connectfour.ConnectFourGameState:
    '''Display game board, accept and process commands.
    '''
    print('Welcome to the ConnectFour game !\n')
    functions_for_both.print_screen(game_state)
    while True:
        functions_for_both.print_turn(game_state)
        try:
            command=functions_for_both.collect_player_command()
            column_number=eval(command[-1])-1
            game_state=functions_for_both.game_each_move(command[0],column_number,game_state)
        except NameError:
            print('Invalid input! Please try again')
            continue
        functions_for_both.print_screen(game_state)
        winner=connectfour.winning_player(game_state)
        if functions_for_both.check_for_winner(winner):
            break
        
    print('Game Over')
    return

def user_interface()-> None:
    '''Main program
    '''
    GameBoard=connectfour.new_game_state()
    handle_commands(GameBoard)
    return

if __name__ == '__main__':
    user_interface()
