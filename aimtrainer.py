import pygame
import math
import random as rnd
import time
pygame.init()

WIDTH, HEIGHT = 800, 600
BAR_HEIGHT = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30
LIVES = 3

LABEL_FONT = pygame.font.SysFont('comicsans', 24)
TIME_LABEL_POS = (5, 5)
SPEED_LABEL_POS = (200, 5)
HITS_LABEL_POS = (450, 5)
LIVES_LABEL_POS = (550, 5)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
    
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, scrn):
        pygame.draw.circle(scrn, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(scrn, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(scrn, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(scrn, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.size

def draw(scrn, targets):
    scrn.fill("black")

    for target in targets:
        target.draw(scrn)

def format_time(elapsed_time):
    milli = math.floor(int(elapsed_time * 1000 % 1000) / 100)
    seconds = int(round(elapsed_time % 60, 1))
    mins = int(elapsed_time // 60)

    return f"{mins:02d}:{seconds:02d}.{milli}"

def draw_top_bar(scrn, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(scrn, "grey", (0, 0, WIDTH, BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"speed: {speed} t/s", 1, "black")

    hits_label = LABEL_FONT.render(f"hits: {targets_pressed}", 1, "black")

    lives_label = LABEL_FONT.render(f"lives remaining: {LIVES - misses}", 1, "black")

    scrn.blit(time_label, TIME_LABEL_POS)
    scrn.blit(speed_label, SPEED_LABEL_POS)
    scrn.blit(hits_label, HITS_LABEL_POS)
    scrn.blit(lives_label, LIVES_LABEL_POS)

def end_screen(scrn, elapsed_time, targets_pressed, clicks):
    scrn.fill("white")
    time_label = LABEL_FONT.render(f"time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"speed: {speed} t/s", 1, "black")

    hits_label = LABEL_FONT.render(f"hits: {targets_pressed}", 1, "black")

    acc = round(targets_pressed / clicks * 100, 1)
    acc_label = LABEL_FONT.render(f"accuracy: {acc}%", 1, "black")

    time_label_pos = (get_middle(time_label), 100)
    speed_label_pos = (get_middle(speed_label), 200)
    hits_label_pos = (get_middle(hits_label), 300)
    acc_label_pos = (get_middle(acc_label), 400)

    scrn.blit(time_label, time_label_pos)
    scrn.blit(speed_label, speed_label_pos)
    scrn.blit(hits_label, hits_label_pos)
    scrn.blit(acc_label, acc_label_pos)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2

def main():
    run_bool = True

    targets = []
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    clock = pygame.time.Clock()

    targets_pressed = clicks = misses = 0
    start_time = time.time()

    while run_bool:
        clock.tick(60)
        click = False

        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_bool = False
                break
            
            if event.type == TARGET_EVENT:
                x_pos = rnd.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y_pos = rnd.randint(TARGET_PADDING + BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x_pos, y_pos)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
                mouse_pos = pygame.mouse.get_pos()

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1
            
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                targets_pressed += 1

        if misses >= LIVES:
            end_screen(screen, elapsed_time, targets_pressed, clicks)

        draw(screen, targets)

        draw_top_bar(screen, elapsed_time, targets_pressed, misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()