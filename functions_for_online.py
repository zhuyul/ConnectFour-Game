import functions_for_both
import connectfour
import socket

def connect(host: str, port: int,username_to_send:str)->None:
    '''
    Connects to a server running on the given host and listening
    on the given port
    '''
    connectfour_socket = socket.socket()
    try:
        print('Connecting to echo server...')
        connectfour_socket.connect((host, port))
        print('Connected successfully!')
        send_message(connectfour_socket,username_to_send)
        print(receive_message(connectfour_socket))
        _start_game(connectfour_socket)
        GameBoard=connectfour.new_game_state()
        Game_command(GameBoard,connectfour_socket)
    except ConnectionRefusedError:
        connect(host,port)
    finally:
        print('Closing connection')
        connectfour_socket.close()

    print('Goodbye!')

def Game_command(game_state: connectfour.ConnectFourGameState,connectfour_socket:socket.socket)->connectfour.ConnectFourGameState:
    '''Display game board, accept and process commands.
    '''
    functions_for_both.print_screen(game_state)
    while True:
        functions_for_both.print_turn(game_state)
        
        if game_state.turn==connectfour.RED:
            command=functions_for_both.collect_player_command()
                # try
            send_message(connectfour_socket,command)
            print(receive_message(connectfour_socket))
        elif game_state.turn==connectfour.YELLOW:
            command=receive_message(connectfour_socket)
            print(command)

        column_number=eval(command.split()[1])-1
        game_state=functions_for_both.game_each_move(command[0],column_number,game_state)
        
        functions_for_both.print_screen(game_state)
        winner=connectfour.winning_player(game_state)
        if functions_for_both.check_for_winner(winner):
            break
          
    print('Game Over')
    return

# message transmission through socket
def send_message(connectfour_socket:socket.socket,message:str)->None:
    '''take a meesage and socket to the server'''
    message_send =(message+'\r\n').encode(encoding='utf-8')
    connectfour_socket.send(message_send)
    return

def receive_message(connectfour_socket:socket.socket)->str:
    '''take a message and decoded'''
    reply_message_bytes = connectfour_socket.recv(4096)
    reply_message = reply_message_bytes.decode(encoding='utf-8').rstrip()
    return reply_message


def _start_game(connectfour_socket:socket.socket):
    '''enter 'AI_GAME' to start the game
    '''
    while True:
        message_to_start=input('enter "AI_GAME" to start the game: ').strip()
        if message_to_start=='AI_GAME':
            send_message(connectfour_socket,message_to_start)
            print('Game Start')
            print(receive_message(connectfour_socket))
            return True
        else:
            print('Invalid input. Please try again.')
    return
