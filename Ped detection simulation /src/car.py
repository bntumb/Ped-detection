import pygame

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_moving = False
        self.car1_image = pygame.image.load("car_sprites/0.png")
        self.car2_image = pygame.image.load("car_sprites/1.png")
        self.car1_image = pygame.transform.scale(self.car1_image, (180, 180))
        self.car2_image = pygame.transform.scale(self.car2_image, (180, 180))
        self.current_image = self.car1_image  # Default image
        self.animation_counter = 0  # Counter for toggling images

    def draw(self, screen):
        """Draw the car."""
        screen.blit(self.current_image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 255, 0), self.get_rect(), 2)

    def get_rect(self):
        """Return the bounding rectangle of the car."""
        return pygame.Rect(self.x, self.y, 180, 180)  # 200x200 size

    def set_speed(self, key_pressed):
        """Set speed based on key presses."""
        if key_pressed[pygame.K_UP]:
            self.is_moving = True
            return 5
        self.is_moving = False
        return 0

    def update_animation(self):
        """Update the car's image for animation."""
        if self.is_moving:
            self.animation_counter += 1
            # Toggle image every 10 frames
            if self.animation_counter % 20 < 5:
                self.current_image = self.car1_image
            else:
                self.current_image = self.car2_image
        else:
            # Default image when not moving
            self.current_image = self.car1_image
            self.animation_counter = 0
