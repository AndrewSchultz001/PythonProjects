import random as rnd

def roll():
    return rnd.randint(1, 6)

while True:
    num_of_players = input("Enter the number of players (1-4): ")

    if num_of_players.isdigit() and int(num_of_players) >= 1 and int(num_of_players) <= 4:
        break
    else:
        print("Invalid Input. Try Again")
        continue

num_of_players = int(num_of_players)
max_score = 20
player_scores = [0 for _ in range(num_of_players)]

while max(player_scores) < max_score:
    for i in range(num_of_players):
        print("Player " + str(i + 1) + "\'s turn has started")
        print("Your total score is: " + str(player_scores[i]) + '\n')
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ").lower()

            if should_roll != 'y':
                break

            roll_val = roll()

            if roll_val == 1:
                print("You rolled a 1! Your turn is done")
                current_score = 0
                break
            else:
                current_score += roll_val
                print("You rolled a " + str(roll_val))

        player_scores[i] += current_score
        print("Your total score is: " + str(player_scores[i]) + '\n')

max_score = max(player_scores)
winning_index = player_scores.index(max_score) + 1
print("Player " + str(winning_index) + ' won with a total score of ' + str(max_score))
