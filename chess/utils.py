def get_previous_row(row):
    return str(int(row) - 1)


def get_previous_column(col):
    if col == 'b':
        return 'a'
    elif col == 'c':
        return 'b'
    elif col == 'd':
        return 'c'
    elif col == 'e':
        return 'd'
    elif col == 'f':
        return 'e'
    elif col == 'g':
        return 'f'
    elif col == 'h':
        return 'g'


def get_next_row(row):
    return str(int(row) + 1)


def get_next_column(col):
    if col == 'a':
        return 'b'
    elif col == 'b':
        return 'c'
    elif col == 'c':
        return 'd'
    elif col == 'd':
        return 'e'
    elif col == 'e':
        return 'f'
    elif col == 'f':
        return 'g'
    elif col == 'g':
        return 'h'


def get_available_diagonals(key, board):
    available_diagonals = []
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'h' and j != '8' and not found_obstacle:
        i = get_next_column(i)
        j = get_next_row(j)
        if i + j not in board.keys():
            available_diagonals.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_diagonals.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'h' and j != '1' and not found_obstacle:
        i = get_next_column(i)
        j = get_previous_row(j)
        if i + j not in board.keys():
            available_diagonals.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_diagonals.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'a' and j != '8' and not found_obstacle:
        i = get_previous_column(i)
        j = get_next_row(j)
        if i + j not in board.keys():
            available_diagonals.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_diagonals.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'a' and j != '1' and not found_obstacle:
        i = get_previous_column(i)
        j = get_previous_row(j)
        if i + j not in board.keys():
            available_diagonals.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_diagonals.append(i + j)
            found_obstacle = True
    return available_diagonals


def get_available_lines(key, board):
    available_lines = []
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'a' and not found_obstacle:
        i = get_previous_column(i)
        if i + j not in board.keys():
            available_lines.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_lines.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while i != 'h' and not found_obstacle:
        i = get_next_column(i)
        if i + j not in board.keys():
            available_lines.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_lines.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while j != '1' and not found_obstacle:
        j = get_previous_row(j)
        if i + j not in board.keys():
            available_lines.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_lines.append(i + j)
            found_obstacle = True
    i = key[0]
    j = key[1]
    found_obstacle = False
    while j != '8' and not found_obstacle:
        j = get_next_row(j)
        if i + j not in board.keys():
            available_lines.append(i + j)
        else:
            if board[i + j]['color'] != board[key]['color']:
                available_lines.append(i + j)
            found_obstacle = True
    return available_lines


def get_diagonals(key):
    diagonals = []
    i = key[0]
    j = key[1]
    while i != 'h' and j != '8':
        i = get_next_column(i)
        j = get_next_row(j)
        diagonals.append(i + j)
    i = key[0]
    j = key[1]
    while i != 'h' and j != '1':
        i = get_next_column(i)
        j = get_previous_row(j)
        diagonals.append(i + j)
    i = key[0]
    j = key[1]
    while i != 'a' and j != '8':
        i = get_previous_column(i)
        j = get_next_row(j)
        diagonals.append(i + j)
    i = key[0]
    j = key[1]
    while i != 'a' and j != '1':
        i = get_previous_column(i)
        j = get_previous_row(j)
        diagonals.append(i + j)
    return diagonals


def get_lines(key):
    lines = []
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if i != key[0]:
            lines.append(i + key[1])
    for j in ['1', '2', '3', '4', '5', '6', '7', '8']:
        if j != key[1]:
            lines.append(key[0] + j)
    return lines
