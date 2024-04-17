import numpy as np
import random

def notContains(array, num):
    for i in range(len(array)):
        if (array[i] == num):
            return False
    return True

def notContainsBox(array, num): 
    for i in range(len(array)):
        for j in range(len(array[0])):
            if (array[i][j] == num):
                return False
    return True

def generate_board():
    board = np.zeros((9, 9))
    numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def is_valid_move(row, col, num):
        return (notContains(board[row, :], num) and
                notContains(board[:, col], num) and
                notContainsBox(board[(row//3)*3:(row//3)*3+3, (col//3)*3:(col//3)*3+3], num))

    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row, col] == 0:
                    np.random.shuffle(numbers)
                    for num in numbers:
                        if is_valid_move(row, col, num):
                            board[row, col] = num
                            if fill_board(): 
                                return True
                            board[row, col] = 0  
                    return False  
        return True

    fill_board()
    return board

def get_board():
    return generate_board()