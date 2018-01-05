def arrange_eight_queens():
    """Gets all the different ways of arranging eight queens on an 8x8 chess
    board such that no two queens share the same column, row or diagonal.
    """
    solutions = []
    fill_row(0, solutions, [], [], [], [])
    return solutions


def fill_row(i, solutions, current, columns, left_diagonal, right_diagonal):
    print "here"
    blocked = [columns, left_diagonal, right_diagonal]
    possible = [x for x in xrange(8) if not any(x in y for y in blocked)]
    if not possible:
        return
    for x in possible:
        new = list(current)
        new.append(x)
        if i == 7:
            solutions.append(new)
            return
        fill_row(i + 1, solutions, new,
                 columns + [x],
                 [y - 1 for y in left_diagonal] + [x - 1],
                 [y + 1 for y in right_diagonal] + [x + 1])


def draw_board():
    board = []
    board.append(list("_________________"))
    for _ in xrange(8):
        board.append(list("| | | | | | | | |"))
        board.append(list("|_|_|_|_|_|_|_|_|"))
    return board

if __name__ == '__main__':
    for solution in arrange_eight_queens():
        board = draw_board()
        for i, j in enumerate(solution):
            board[2*i + 1][2*j + 1] = "X"
        for row in board:
            print "".join(row)
