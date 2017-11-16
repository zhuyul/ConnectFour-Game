import functions_for_online

HOST = 'woodhouse.ics.uci.edu'
PORT = 4444


def client_user_interface():
    print('Welcome to the Connectfour Online Game')
    username_to_send=_ask_for_username()
    functions_for_online.connect(HOST,PORT,username_to_send)
    return

def _ask_for_username()->str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that is expected    '''
    while True:
        username_to_send = 'I32CFSP_HELLO '+input('''Please input your username: ''').strip()
        List_username=username_to_send.split()
        if _is_useranme_expected(List_username,'I32CFSP_HELLO'):
            return username_to_send
        else:
            print('The username is invalid. Please input again.')

def _is_useranme_expected(List_username:list,expected_username:str)->bool:
    '''Returns True if the input username is expected text,
    False otherwise.
    '''
    result=False
    if List_username[0]==expected_username and len(List_username)==2 and len(List_username[-1])>1:
        result= True
    return result




if __name__ == '__main__':
    client_user_interface()
