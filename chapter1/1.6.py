def rotate_image(pixels):
    """Rotates image by 90 degrees represented by an NxN list of lists."""
    N = len(pixels)
    rotated = [[None] * N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            rotated[j][N - 1 - i] = pixels[i][j]
    return rotated


def rotate_image_inplace(pixels):
    N = len(pixels)
    # One quadrant.
    for i in xrange(N / 2):
        for j in xrange((N + 1) / 2):
            pixels[i][j], pixels[j][N - 1 - i], pixels[N - 1 - i][N - 1 - j], pixels[N - 1 - j][i] = pixels[N - 1 - j][i], pixels[i][j], pixels[j][N - 1 - i], pixels[N - 1 - i][N - 1 - j]
    return pixels

n = 4
for row in rotate_image_inplace([range(n * i, n * (i + 1)) for i in xrange(n)]):
    print row
