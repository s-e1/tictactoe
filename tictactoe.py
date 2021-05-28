player = ''
gameover = False
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


def display_board():
    print(f'{row1[0]}|{row1[1]}|{row1[2]}')
    print(f'{row2[0]}|{row2[1]}|{row2[2]}')
    print(f'{row3[0]}|{row3[1]}|{row3[2]}')


def new_game():
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


def iswinner():
    global gameover
    if row1[0] == player and row1[1] == player and row1[2] == player \
            or row2[0] == player and row2[1] == player and row2[2] == player \
            or row3[0] == player and row3[1] == player and row3[2] == player\
            or row1[0] == player and row2[0] == player and row3[0] == player \
            or row1[1] == player and row2[1] == player and row3[1] == player \
            or row1[2] == player and row2[2] == player and row3[2] == player\
            or row1[0] == player and row2[1] == player and row3[2] == player\
            or row1[2] == player and row2[1] == player and row3[0] == player:
        gameover = True
        print(player + ' is the winner')


def switch_player():
    global player
    player = 'x' if player == 'o' else 'o'


new_game()
while not gameover:
    pick()
    display_board()
    iswinner()
    switch_player()
