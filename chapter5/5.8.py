def draw_horizontal_line(screen, width, x1, x2, y):
    """Monochrome screen stored as array of bytes allowing eight consecutive
    pixels to be stored in one byte. Width of screen is a multiple of 8.
    Draws a line from (x1, y) to (x2, y).
    """
    # height = len(screen) * 8 / width
    start_byte, start_bit = (y*width + x1) / 8, x1 % 8
    end_byte, end_bit = (y*width + x2) / 8, x2 % 8
    start_mask = 0xFF >> start_bit
    end_mask = ~(0xFF >> end_bit + 1)
    # Fill in start and end bytes.
    if start_byte == end_byte:
        screen[start_byte] |= start_mask & end_mask
    else:
        screen[start_byte] |= start_mask
        screen[end_byte] |= end_mask
    # Fill in full middle bytes.
    for i in xrange(start_byte + 1, end_byte):
        screen[i] = 0xFF
    return screen

if __name__ == '__main__':
    width = 32
    screen = [0] * 20
    screen = draw_horizontal_line(screen, width, 7, 16, 1)
    screen = draw_horizontal_line(screen, width, 1, 9, 3)
    screen = draw_horizontal_line(screen, width, 5, 15, 3)
    for i, byte in enumerate(screen):
        for j in reversed(xrange(8)):
            print 1 if byte & 1 << j else 0,
        if 8 * (i + 1) % width == 0:
            print
