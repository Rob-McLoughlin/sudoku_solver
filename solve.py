puzzle = [[5, 1, 0, 0, 7, 9, 0, 0, 0],
          [0, 0, 2, 0, 0, 5, 0, 0, 0],
          [0, 9, 0, 0, 1, 2, 5, 3, 0],
          [3, 6, 4, 0, 5, 0, 2, 0, 7],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 5, 0, 3, 0, 6, 9, 4],
          [0, 7, 3, 5, 2, 0, 0, 4, 0],
          [0, 0, 0, 1, 0, 0, 7, 0, 0],
          [0, 0, 0, 4, 9, 0, 0, 6, 1]]


def next_cell(puzzle, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if puzzle[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if puzzle[x][y] == 0:
                return x, y
    return -1, -1


def get_subgrid(puzzle: list, x: int, y: int) -> list:
    """Return a flat list of the subgrid that an x, y sits in the puzzle grid

    Args:
        puzzle (list): A 2x9 matrix representing the puzzle
        x (int): The x position in the matrix, starting from the left at 0
        y (int): The x position in the matrix, starting from the top at 0

    Returns:
        list: A flat list of the subgrid
    """
    subgrid = []
    # Determine what subgrid in a 3x3 grid the x,y is in (index 0)
    subgrid_x_pos = (x // 3) * 3
    subgrid_y_pos = (y // 3) * 3
    for i in range(0, 3):
        # Print all the rows
        row = puzzle[i + subgrid_y_pos]
        for j in range(0, 3):
            subgrid.append(row[j + subgrid_x_pos])
    return subgrid


def possible(puzzle: list, x: int, y: int, n: int) -> bool:
    """Determines whether a number is valid in the puzzle matrix at a given x,y coordinate

    Args:
        puzzle (list): A 2x9 matrix representing the puzzle
        x_pos (int): The x position in the matrix, starting from the left at 0
        y_pos (int): The x position in the matrix, starting from the top at 0
        n (int): The number to check validity of.

    Returns:
        bool: Whether the number is valid or not
    """
    # print('Trying {} at position {} {}'.format(n, x, y))
    # Check the row, check the column
    row = [puzzle[y]]
    column = [number[x] for number in puzzle]
    # If the number is in the column or in the row, return False
    if n in row or n in column:
        # print('{} was already in the row or column'.format(n))
        return False
    # If the number is in the 3x3 subgrid
    subgrid = get_subgrid(puzzle=puzzle, x=x, y=y)
    if n in subgrid:
        # print('{} was already in the subgrid'.format(n))
        return False
    return True


def solve_puzzle(puzzle: list) -> list:
    """Solves the given puzzle

    Args:
        puzzle (list): A 2x9 matrix representing the puzzle

    Returns:
        list: the solved puzzle (with no 0's)
    """
    for y in range(9):
        # print(y)
        for x in range(9):
            if puzzle[y][x] == 0:
                print('Found 0 position at {},{}'.format(x, y))
                for n in range(1, 10):
                    if possible(puzzle=puzzle, x=x, y=y, n=n):
                        print('{} fits at position {}, {}'.format(n, x, y))
                        puzzle[y][x] = n
                        solve_puzzle(puzzle=puzzle)
                        puzzle[y][x] = 0
                return


# print(solve_puzzle(puzzle=puzzle))


def solve(puzzle, i=0, j=0):
    i, j = next_cell(puzzle, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if possible(puzzle=puzzle, x=i, y=j, n=e):
            puzzle[i][j] = e
            if solve(puzzle, i, j):
                return True
            # Undo the current cell for backtracking
            puzzle[i][j] = 0
    print(puzzle)
    return False


solve(puzzle=puzzle)
