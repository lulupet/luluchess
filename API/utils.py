ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def next_column(column):
    return COLUMNS[COLUMNS.index(column) + 1]

def previous_column(column):
    return COLUMNS[COLUMNS.index(column) - 1]

def next_row(row):
    return ROWS[ROWS.index(row) + 1]

def previous_row(row):
    return ROWS[ROWS.index(row) - 1]

def diagonals(column, row):
    diag = []
    i = column
    j = row
    while i != 'H' and j != '8':
        i = next_column(i)
        j = next_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'H' and j != '1':
        i = next_column(i)
        j = previous_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'A' and j != '8':
        i = previous_column(i)
        j = next_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'A' and j != '1':
        i = previous_column(i)
        j = previous_row(j)
        diag.append(i + j)
    return diag
