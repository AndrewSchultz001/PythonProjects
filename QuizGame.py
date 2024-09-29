print("Welcome to my Quiz Game")

correct_count = 0
total_count = 0

playing = input("Do you want to play? ").lower()
if playing != 'yes':
    quit()

answer = input("What does CPU stand for? ").lower()
total_count += 1
if answer == 'central proccessing unit':
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ").lower()
total_count += 1
if answer == 'graphics proccessing unit':
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ").lower()
total_count += 1
if answer == 'random access memory':
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ").lower()
total_count += 1
if answer == 'power supply':
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

percent_val = correct_count/total_count * 100
print("You got a " + str(percent_val) + "%")
