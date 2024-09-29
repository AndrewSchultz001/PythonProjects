import random as rnd

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = rnd.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True: 
        guess = input("Guess: ").upper()
        guess = list(guess)

        if len(guess) != 4:
            print("You must guess " + str(CODE_LENGTH) + " colors")
            continue

        for color in guess: 
            if color not in COLORS:
                print("Invalid color: " + str(color) + ". Try again")
                break
        else:
            break
    
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_count = incorrect_count = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_count += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0 and guess_color != real_color:
            incorrect_count += 1
            color_counts[guess_color] -= 1

    return correct_count, incorrect_count

def game():
    print("Welcome to mastermind, you have " + str(TRIES) + " to guess the code")
    print("The valid colors are R G Y B O W")
    code = generate_code()
    print(code)

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_count, incorrect_count = check_code(guess, code)

        if guess == code:
            print("You guessed the code in " + str(attempts) + " tries")
            break

        print("Correct Positions: " + str(correct_count) + " Incorrect Poistions: " + str(incorrect_count))
    else:
        print("You ran out of tries, the code was ", *code)

game()

