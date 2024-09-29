import turtle
import time
import random as rnd

WIDTH = HEIGHT = 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
MIN_MOVE, MAX_MOVE = 1, 20

def get_num_of_racers():
    while True:
        num_of_racers = input("Enter the number of racers (2-10): ")

        if num_of_racers.isdigit():
            num_of_racers = int(num_of_racers)
            if 2 <= num_of_racers <= 10:
                break
            else:
                print('Please enter a valid number. Pick between 2-10')
        else:
            print("Please input a number")
    return num_of_racers

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def create_turtles(colors):
    turtles = []
    spacingx =  WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        x_pos = -WIDTH // 2  + (i + 1) * spacingx
        y_pos = -HEIGHT // 2 + 20
        racer.setpos(x_pos, y_pos)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            dist = rnd.randrange(MIN_MOVE, MAX_MOVE)
            racer.forward(dist)
            
            x, y = racer.pos()

            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

racers = get_num_of_racers()
init_turtle()

rnd.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)

print("The winner is the turtle with color: " + winner)
time.sleep(5)
