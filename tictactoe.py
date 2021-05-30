def initial_values():
    global player
    global row1
    global row2
    global row3
    player = ''
    row1 = [' '] * 3
    row2 = [' '] * 3
    row3 = [' '] * 3


def choose_token():
    global player
    while True:
        choice = input('choose X or O: \n')
        if choice in ['x', 'o']:
            player = choice
            break


def pick():
    while True:
        choice = input('choose a position (1-9): \n')
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1, 10):
                row = get_row(choice)
                position = (choice-1) % 3
                if row[position] == ' ':
                    row[position] = player
                    break
                else:
                    print('choose an empty spot')


def get_row(num):
    if num < 4:
        return row1
    elif num < 7:
        return row2
    else:
        return row3


def display_board():
    print(f'{row1[0]}|{row1[1]}|{row1[2]}')
    print(f'{row2[0]}|{row2[1]}|{row2[2]}')
    print(f'{row3[0]}|{row3[1]}|{row3[2]}')


def switch_player():
    global player
    player = 'x' if player == 'o' else 'o'


def iswinner():
    if player == row1[0] == row1[1] == row1[2] \
            or player == row2[0] == row2[1] == row2[2] \
            or player == row3[0] == row3[1] == row3[2] \
            or player == row1[0] == row2[0] == row3[0]  \
            or player == row1[1] == row2[1] == row3[1]  \
            or player == row1[2] == row2[2] == row3[2] \
            or player == row1[0] == row2[1] == row3[2] \
            or player == row1[2] == row2[1] == row3[0]:
        print(player + ' is the winner')
        another_game()
    elif row1[0] != ' ' and row1[1] != ' ' and row1[2] != ' ' \
            and row2[0] != ' ' and row2[1] != ' ' and row2[2] != ' ' \
            and row3[0] != ' ' and row3[1] != ' ' and row3[2] != ' ':
        print('It is a tie')
        another_game()


def another_game():
    while True:
        res = input('Do you want to play another game (y,n)? \n')
        if res in ['y', 'n']:
            if res == 'y':
                initial_values()
                choose_token()
                break
            else:
                global gameover
                gameover = True
                break


gameover = False
initial_values()
choose_token()
while not gameover:
    pick()
    display_board()
    iswinner()
    switch_player()
