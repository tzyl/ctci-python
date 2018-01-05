def highest_stack(heights, widths, depths):
    """Returns the height of the highest stack of boxes possible with a set of
    boxes represented with the index into heights, widhts and depths.

    A box can only placed on the top of a stack if the box is strictly
    larger in height width and depth than every box currently in the stack.
    """
    boxes = zip(heights, widths, depths)
    return highest_substack(None, boxes)


def highest_substack(prev_box, boxes):
    best_height = 0
    best_stack = []
    for box in boxes:
        if is_larger(box, prev_box):
            new_stack = highest_substack(box, boxes)
            new_height = get_height(new_stack)
            if new_height > best_height:
                best_height = new_height
                best_stack = new_stack
    if prev_box is not None:
        best_stack.append(prev_box)
    return best_stack


def is_larger(box1, box2):
    if box2 is None:
        return True
    return box1[0] > box2[0] and box1[1] > box2[1] and box1[2] > box2[2]


def get_height(stack):
    return sum(box[0] for box in stack)

if __name__ == '__main__':
    heights, widths, depths = range(1, 11), range(1, 11), range(1, 11)
    # heights[0] = 54
    stack = highest_stack(heights, widths, depths)
    print stack
    print get_height(stack)
