
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
images = []
images.append(pygame.image.load("/home/jh/Desktop/001.png"))
images.append(pygame.image.load("/home/jh/Desktop/02.png"))
images.append(pygame.image.load("/home/jh/Desktop/03.png"))
images.append(pygame.image.load("/home/jh/Desktop/04.png"))

# Animation settings
num_frames = 4
frame_duration = 100  # milliseconds per frame
clock = pygame.time.Clock()

def main():
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(images[frame % len(images)], (100, 100))
        pygame.display.flip()
        
        frame += 1
        clock.tick(1000 // frame_duration)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
