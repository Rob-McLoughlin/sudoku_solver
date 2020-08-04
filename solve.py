puzzle = [[5, 1, 0, 0, 7, 9, 0, 0, 0],
          [0, 0, 2, 0, 0, 5, 0, 0, 0],
          [0, 9, 0, 0, 1, 2, 5, 3, 0],
          [3, 6, 4, 0, 5, 0, 2, 0, 7],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [7, 0, 5, 0, 3, 0, 6, 9, 4],
          [0, 7, 3, 5, 2, 0, 0, 4, 0],
          [0, 0, 0, 1, 0, 0, 7, 0, 0],
          [0, 0, 0, 4, 9, 0, 0, 6, 1]]


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
    row = puzzle[y]
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


def get_possibilities(puzzle: list, x: int, y: int) -> list:
    possibilities = [i for i in range(1, 10) if possible(
        puzzle=puzzle, x=x, y=y, n=i)]
    return possibilities


def solve(puzzle):
    finished = True if 0 not in [
        item for row in puzzle for item in row] else False
    if finished:
        print('Finished the puzzle!')
        print(puzzle)
    else:
        # Create a list of possibilities for each cell
        for row in puzzle:
            row_number = puzzle.index(row)
            # print(row_number)
            for i in range(9):
                if row[i] == 0:
                    # Create possibilities)
                    possibilities = get_possibilities(
                        puzzle=puzzle, x=i, y=row_number)
                    if len(possibilities) == 1:
                        puzzle[row_number][i] = possibilities[0]
                        # Go again
                        solve(puzzle)


solve(puzzle=puzzle)
