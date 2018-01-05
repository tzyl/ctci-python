def zero_column_row(matrix):
    """If an elmement in an MxN matrix is 0, its entire row and column are set
    to 0."""
    M = len(matrix)
    N = len(matrix[0])
    zeros = []
    for i in xrange(M):
        for j in xrange(N):
            if matrix[i][j] == 0:
                zeros.append((i, j))
    for i, j in zeros:
        for x in xrange(M):
            matrix[x][j] = 0
        for y in xrange(N):
            matrix[i][y] = 0
    return matrix

test = [[4, 1, 3], [1, 0, 1], [1, 2, 4]]
print "\n".join(str(row) for row in zero_column_row(test))
