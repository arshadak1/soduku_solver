def solve(bo):
    cell = _empty_cell(bo)
    if not cell:
        return True
    else:
        row, col = cell

    for i in range(1, 10):
        if _is_valid(bo, i, cell):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('-------------------------------')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print('|', end="  ")
            print(str(bo[i][j]) + "  ", end="")
        print()


def _is_valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    box_pos = (pos[0] // 3, pos[1] // 3)

    for i in range(box_pos[0] * 3, box_pos[0] * 3 + 3):
        for j in range(box_pos[1] * 3, box_pos[1] * 3 + 3):
            if bo[i][j] == num and (j, i) != pos:
                return False
    return True


def _empty_cell(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None
