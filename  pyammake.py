
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
base_color = (100, 150, 200)

def random_color():
    r = max(0, min(255, base_color[0] + random.randint(-6, 6)))
    g = max(0, min(255, base_color[1] + random.randint(-6, 6)))
    b = max(0, min(255, base_color[2] + random.randint(-6, 6)))
    return (r, g, b)

def draw_shapes():
    screen.fill((255, 255, 255))
    for _ in range(100):
        color = random_color()
        if random.choice(['circle', 'square']) == 'circle':
            pygame.draw.circle(screen, color, (random.randint(0, screen_width), random.randint(0, screen_height)), 20)
        else:
            rect = pygame.Rect(random.randint(0, screen_width), random.randint(0, screen_height), 40, 40)
            pygame.draw.rect(screen, color, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_shapes()
    pygame.display.flip()

pygame.quit()

