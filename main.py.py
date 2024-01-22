from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
  def build(self):
    return MDLabel(text="wellcome to game developed by sudhakar",halign="center")
if __name__ == '__main__':
  Main_App().run()




import pygame
import random

# Game settings
WIDTH = 600
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Bird parameters
bird_x = 100
bird_y = HEIGHT // 2
bird_vel = 0
bird_img = pygame.image.load("BIRD.png")

# Pipe parameters
pipe_width = 50
pipe_min_gap = 100
pipe_max_gap = 200
pipe_speed = 5
upper_pipe_x = WIDTH
upper_pipe_height = random.randint(0, HEIGHT - pipe_min_gap - pipe_width)
lower_pipe_height = HEIGHT - pipe_min_gap - upper_pipe_height

# Score
score = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_vel = -8  # Jump force

  # Update bird position
  bird_vel += 1  # Gravity
  bird_y += bird_vel
  bird_y = min(bird_y, HEIGHT - bird_img.get_height())  # Prevent falling off screen

  # Update pipe position
  upper_pipe_x -= pipe_speed
  lower_pipe_y = HEIGHT - pipe_min_gap - upper_pipe_height

  # Collision detection
  if (bird_x + bird_img.get_width() >= upper_pipe_x and bird_x <= upper_pipe_x + pipe_width and
      bird_y <= upper_pipe_height) or (
          bird_x + bird_img.get_width() >= upper_pipe_x and bird_x <= upper_pipe_x + pipe_width and
          bird_y >= lower_pipe_y):
    running = False

  # Score keeping
  if upper_pipe_x == bird_x + bird_img.get_width():
    score += 1

  # Draw elements
  screen.fill(WHITE)
  screen.blit(bird_img, (bird_x, bird_y))
  pygame.draw.rect(screen, GREEN, (upper_pipe_x, 0, pipe_width, upper_pipe_height))
  pygame.draw.rect(screen, GREEN, (upper_pipe_x, lower_pipe_y, pipe_width, HEIGHT - lower_pipe_y))

  # Draw score
  font = pygame.font.SysFont("Arial", 32)
  text = font.render(f"Score: {score}", True, BLACK)
  screen.blit(text, (10, 10))

  # Reset pipes if needed
  if upper_pipe_x + pipe_width < 0:
    upper_pipe_x = WIDTH
    upper_pipe_height = random.randint(0, HEIGHT - pipe_min_gap - pipe_width)
    lower_pipe_y = HEIGHT - pipe_min_gap - upper_pipe_height

  # Update display
  pygame.display.flip()
  clock.tick(FPS)

# Quit Pygame
pygame.quit()

print(f"Final score: {score}")
