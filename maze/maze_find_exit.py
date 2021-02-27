grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['#', '#', '.', '.', '.', '.', '.', '.', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#']
]
grid[1][0] = '*'


def is_start(x, y):
    return grid[x][y] == '*'


def is_visited(x, y):
    return grid[x][y] == 'v'


def mark_visited(x, y):
    grid[x][y] = 'v'


def is_cell_on_edge(x, y):
    edge = (x == len(grid) - 1 or y == len(grid[x]) - 1 or x == 0 or y == 0)
    print(f"is cell {x, y} on edge {edge}")
    return edge


def has_path(x, y):
    return grid[x][y] == '.'


def search(x, y):  # Check correct ranges for x, y
    # Also check is it was visited
    # try:

    if is_start(x, y):
        mark_visited(x, y)

    elif is_visited(x, y):
        return False
    # except IndexError:
    #     return False

    elif not has_path(x, y):
        mark_visited(x, y)
        return False

    elif is_cell_on_edge(x, y) and has_path(x, y):
        print(f"!!!Found exit at {x, y}!!! ")
        return True

    mark_visited(x, y)  # explore neighbors clockwise starting by the one on the right

    if (search(x + 1, y)
            or search(x, y - 1)
            or search(x - 1, y)
            or search(x, y + 1)):
        grid[x][y] = '7'
        print(f"Dig from {x, y}")
        return True

    return False

search(1, 0)

for line in grid:
    print(line)

