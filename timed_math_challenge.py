import random as rnd
import math
import time

OPERATORS = ['+', '-', '*', '/']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBS = 10


def generate_problem():
    left = rnd.randint(MIN_OPERAND, MAX_OPERAND)
    right = rnd.randint(MIN_OPERAND, MAX_OPERAND)
    operator = rnd.choice(OPERATORS)

    if operator == '/':
        if left % right != 0:
            left = left * right  

    expr = str(left) + " " + operator + " " + str(right)
    answer = math.floor(eval(expr))
    return expr, answer

input('Press Enter to Start')
print('--------------------')

correct_count = 0
start_time = time.time()
for i in range(TOTAL_PROBS):
    expr, answer = generate_problem()
    guess = input("Problem " + str(i+1) + ": " + expr + " = ")

    if guess == str(answer):
        print('Correct!!\n')
        correct_count += 1
    else:
        print('Incorrect!!')

end_time = time.time()
total_time = round(end_time - start_time, 2)
print('--------------------')
percent_val = correct_count / TOTAL_PROBS * 100
print('You got a ' + str(percent_val) + "%")
print('It took you ' + str(total_time) + ' seconds')


