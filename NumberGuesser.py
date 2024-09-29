import random as rnd

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a value larger than zero")
        quit
else:
    print("Please type a number")
    quit()

value = rnd.randint(0, top_of_range)


guess_count = 0
while True:
    user_guess = input("Type a number: ")
    guess_count += 1

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue

    if user_guess == value:
        print("You guessed correctly")
        break
    elif user_guess > value:
        print("Your guess was above the number")
    else:
        print("Your guess was below the number")

print("It took you " + str(guess_count) + " guesses")