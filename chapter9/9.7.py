def paint_fill(screen, point, new_color):
    """Given a screen (represented by a 2D array of colors), a point and a new
    color, fills in the surround area of the point with the new color until the
    color changes from the original color."""
    visited = set()
    paint_fill_helper(screen, point, new_color, visited)


def paint_fill_helper(screen, point, new_color, visited):
    visited.add(point)
    for neighbour in get_neighbours(screen, point):
        if neighbour not in visited:
            if get_color(screen, neighbour) == get_color(screen, point):
                paint_fill_helper(screen, neighbour, new_color, visited)
    screen[point[0]][point[1]] = new_color


def get_neighbours(screen, point):
    for i in xrange(max(0, point[0] - 1), min(len(screen), point[0] + 2)):
        for j in xrange(max(0, point[1] - 1), min(len(screen[0]), point[1] + 2)):
            if i == point[0] and j == point[1]:
                continue
            yield i, j


def get_color(screen, point):
    return screen[point[0]][point[1]]

if __name__ == '__main__':
    screen = [[0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0]]
    paint_fill(screen, (2, 2), 2)
    for row in screen:
        print row
