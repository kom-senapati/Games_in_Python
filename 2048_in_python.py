import random
import copy

default_tiles = [2, 4]

Row1 = [0] * 4
Row2 = [0] * 4
Row3 = [0] * 4
Row4 = [0] * 4
Board = [Row1, Row2, Row3, Row4]


def add2or4():

    while True:

        r = random.randint(0, len(Board)-1)
        c = random.randint(0, len(Board)-1)

        if Board[r][c] == 0:
            Board[r][c] = random.choice(default_tiles)

            break


add2or4()
add2or4()


def won():

    for Row in Board:
        if 2048 in Row:

            return True
    return False


def lost():

    tempboard = copy.deepcopy(Board)

    if (tempboard == move_up(tempboard)
        and tempboard == move_down(tempboard)
        and tempboard == move_left(tempboard)
            and tempboard == move_right(tempboard)):

        return True
    return False


def printer():

    tile_size = 0

    for Row in Board:
        for Tile in Row:
            Tile = len(f"{Tile}")
            if Tile > tile_size:
                tile_size = Tile

    for r in Board:
        for Tile in r:
            print(str(Tile).center(tile_size), end=' ')
        print('\n\n')


def Clear_zeroes(arr,):
    return list(filter(lambda x: x != 0, arr))


def transposer(Rows):

    Columns = [[] for _ in range(len(Rows))]

    for i in range(len(Rows)):
        for j in range(len(Rows[i])):
            Columns[j].append(Rows[i][j])

    return Columns


def move_left(Board):

    tempboard = copy.deepcopy(Board)

    for Row in Board:
        row = Clear_zeroes(Row)
        for i in range(len(row)):
            if (i != len(row)-1) and (row[i] == row[i+1]):
                row[i] = row[i]*2
                row[i+1] = 0
        r = Clear_zeroes(row)
        r.extend([0]*(4-len(r)))
        Board[Board.index(Row)] = r

    if tempboard != Board:
        add2or4()
    else:
        print("Sorry, you cant move in that direction.")

    return Board


def move_up(Board):

    tempboard = copy.deepcopy(Board)

    Columns = transposer(Board)

    for Column in Columns:
        column = Clear_zeroes(Column)
        for i in range(len(column)):
            if (i != len(column)-1) and (column[i] == column[i+1]):
                column[i] = column[i]*2
                column[i+1] = 0
        c = Clear_zeroes(column)
        c.extend([0]*(4-len(c)))
        Columns[Columns.index(Column)] = c

    Board = transposer(Columns)

    if tempboard != Board:
        add2or4()
    else:
        print("Sorry, you cant move in that direction.")

    return Board


def move_right(Board):

    tempboard = copy.deepcopy(Board)

    for Row in Board:
        Row = Row[::-1]
        row = Clear_zeroes(Row)
        for i in range(len(row)):
            if (i != len(row)-1) and (row[i] == row[i+1]):
                row[i] = row[i]*2
                row[i+1] = 0
        r = Clear_zeroes(row)
        r.extend([0]*(4-len(r)))
        Board[Board.index(Row[::-1])] = r[::-1]

    if tempboard != Board:
        add2or4()
    else:
        print("Sorry, you cant move in that direction.")

    return Board


def move_down(Board):

    tempboard = copy.deepcopy(Board)
    Columns = transposer(Board)

    for Column in Columns:
        Column = Column[::-1]
        column = Clear_zeroes(Column)
        for i in range(len(column)):
            if (i != len(column)-1) and (column[i] == column[i+1]):
                column[i] = column[i]*2
                column[i+1] = 0
        c = Clear_zeroes(column)
        c.extend([0]*(4-len(c)))
        Columns[Columns.index(Column[::-1])] = c[::-1]

    Board = transposer(Columns)

    if tempboard != Board:
        add2or4()
    else:
        print("Sorry, you cant move in that direction.")

    return Board


def play():

    global Board

    print("Welcome to 2048!")
    print('''
          You will win if you can get a tile with the value 2048.
          You will lose if you cannot move any tiles.(in all directions)''')
    print("Use the ['W','A','S','D'] keys to move the tiles.")
    print("Press 'R' then 'R' to undo the changes.")
    print("Press 'R' then 'r' to reset.")
    print("Press 'Q' to quit.")
    print("The current board is as follows:")
    printer()

    Backup = copy.deepcopy(Board)
    move = ""

    while move != 'Q':

        Temp = copy.deepcopy(Board)
        move = input("Enter your move: ")

        if won():
            print("You won by reaching 2048!")
            break

        elif lost():
            print("You lost as you cannot move any tiles.")
            break

        else:
            if move.lower() in ['w', 'a', 's', 'd']:

                if move.upper() == 'W':
                    Board = move_up(Board)
                    printer()
                elif move.upper() == 'S':
                    Board = move_down(Board)
                    printer()
                elif move.upper() == 'A':
                    Board = move_left(Board)
                    printer()
                elif move.upper() == 'D':
                    Board = move_right(Board)
                    printer()

            elif move.upper() == 'R':

                choice = input("Enter 'R' to undo or 'r' to reset: ")

                if choice == 'R':
                    Board = Temp
                elif choice == 'r':
                    Board = Backup

            else:

                if move != 'Q':
                    print("Invalid input.")


play()
