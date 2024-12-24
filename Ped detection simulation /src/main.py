import pygame
import sys
import math

from person import Person
from car import Car

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 1200, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scrolling Background with Character")

# Load and scale the road image
road_image = pygame.image.load("road_sprites/road.png")
road_image = pygame.transform.scale(road_image, (screen_width, screen_height))

road_image_width = road_image.get_width()

# Define game variables
scroll_speed = 0
tiles = math.ceil(screen_width / road_image_width) + 1


# Create a character instance
hero = Person(800, screen_height - 80,0, rotate_enabled=True)  # Rotates
driver = Car(10, screen_height - 180)  # Rotates

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60  # Set FPS for smooth animation
scroll_speed = 0
background_scroll = 0
# Main game loop
while True:
        # Get key states
    keys = pygame.key.get_pressed()

    background_scroll -= driver.set_speed(keys)
    scroll_speed = driver.set_speed(keys)
    driver.update_animation()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # scroll_speed the road background
 
    if abs(background_scroll) > road_image_width:
        background_scroll = 0

    # Handle input and move the character
    hero.move(-scroll_speed)
    hero.check_boundary( screen_width, screen_height)
    

# Check for collision
    if hero.get_rect().colliderect(driver.get_rect()):
        hero.reset_position()  # Reset the person if they collide with the car

    # Draw the scrolling background
    for i in range(0, tiles):
        screen.blit(road_image, (i * road_image_width + background_scroll, 0))


    # Draw the character
    hero.draw(screen)
    driver.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
