import curses
from curses import wrapper
from collections import deque
import time

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0 :
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors

def reconstruct_path(parent, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path

def find_path(maze, stdscr):
    start, end = "O", "X"
    start_pos = find_start(maze, start)

    q = deque([start_pos])
    visited = set([start_pos])
    parent = {start_pos: None}

    while q:
        current_pos = q.popleft()
        row, col = current_pos

        current_path = reconstruct_path(parent, current_pos)
        stdscr.clear()
        print_maze(maze, stdscr, current_path)
        stdscr.refresh()
        time.sleep(0.5)

        if maze[row][col] == end:
            return reconstruct_path(parent, current_pos)

        neighbors = find_neighbors(maze, row, col)

        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            if neighbor not in visited and maze[neighbor_row][neighbor_col] != "#":
                visited.add(neighbor)
                parent[neighbor] = current_pos
                q.append(neighbor)

    return []

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)