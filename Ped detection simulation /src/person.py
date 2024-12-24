import pygame
import random

class Person:
    def __init__(self, x, y, angle, rotate_enabled=False):
        self.initial_x = x  # Store the initial position
        self.initial_y = y
        self.x = x
        self.y = y
        self.rotate_enabled = rotate_enabled
        self.angle = angle  # Initial rotation angle
        # Load character images
        self.leg1_image = pygame.image.load("person_sprites/0.png")
        self.leg2_image = pygame.image.load("person_sprites/1.png")
        
        # Scale the images (optional, you can adjust size)
        self.leg1_image = pygame.transform.scale(self.leg1_image, (50, 50))
        self.leg2_image = pygame.transform.scale(self.leg2_image, (50, 50))
        
        self.current_image = self.leg1_image  # Initial image
        self.frame_counter = 0  # Keeps track of animation frames

    def reset_position(self):
        """Reset the character to its initial position."""
        self.x = random.randint(300, 900)
        self.y = random.randint(self.initial_y-100, self.initial_y+80)

      


    def move(self, scroll_speed):
        """Move the character."""
        dy =-0.5
        dx = scroll_speed # Fixed horizontal movement for scrolling
        self.x += dx
        self.y += dy    
        # Move the character if there's input
        if dx != 0 or dy != 0:
            self.update_animation()
        
        # Check for boundary collisions and reset if necessary
    def check_boundary(self, screen_width, screen_height):
        if self.x < 0 or self.x + 50 > screen_width or self.y < 0 or self.y + 50 > screen_height:
            self.reset_position()

    def update_animation(self):
        """Update animation every 10 frames."""
        self.frame_counter += 1
        if self.frame_counter % 10 == 0:
            self.current_image = self.leg1_image if self.current_image == self.leg2_image else self.leg2_image

    def draw(self, screen):
        """Draw the character."""
        if self.rotate_enabled:
            rotated_image = pygame.transform.rotate(self.current_image, -self.angle)  # Negative for clockwise
            rotated_rect = rotated_image.get_rect(center=(self.x + 25, self.y + 25))  # Center the rotation
            screen.blit(rotated_image, rotated_rect.topleft)
        else:
            screen.blit(self.current_image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 255, 0), self.get_rect(), 2)

    def get_rect(self):
        """Return the bounding rectangle of the person."""
        return pygame.Rect(self.x, self.y, 50, 50)  # 50x50 size