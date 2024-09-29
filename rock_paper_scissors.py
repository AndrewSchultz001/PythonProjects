import random as rnd

user_score = computer_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        continue

    rand_num = rnd.randint(0, 2)
    opponent_choice = options[rand_num]

    if (user_input == 'rock' and opponent_choice == 'paper') or (user_input == 'paper' and opponent_choice == 'scissors') or (user_input == 'scissors' and opponent_choice == 'rock'):
        print('Loser')
        computer_score += 1
    elif (user_input == 'rock' and opponent_choice == 'scissors') or (user_input == 'paper' and opponent_choice == 'rock') or (user_input == 'scissors' and opponent_choice == 'paper'):
        print('Winner')
        user_score += 1
    else:
        print('Tied')

print("You won " + str(user_score) + " times")
print("The computer won " + str(computer_score) + ' times')