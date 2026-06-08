import pygame
# Initialize Pygame and screen dimensions
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400,500))

# Create a loop to run till the game is quit by the user
done = False

while not done:
  # event of game 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      # quits
      pygame.quit()
  #  Make the changes visible
  pygame.display.flip()