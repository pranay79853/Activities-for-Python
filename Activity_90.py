# 1) Import the `pygame` library to create a window and draw shapes.
import pygame
# 2) Initialize pygame modules using `pygame.init()`.
pygame.init()
# 3) Create a display window (screen) of size 400x300 using `pygame.display.set_mode(...)`
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
# and store it in `screen`.

# 4) Create a variable `done = False` to control the main loop.

# 5) Start the main loop using `while not done`:

# (This keeps the window running until the user quits.)

# 6) Inside the loop, handle events using `pygame.event.get()`:

# a) If the event type is `pygame.QUIT` (user clicks the close button),

# set `done = True` to stop the loop.

# 7) Draw a rectangle on the screen using `pygame.draw.rect()`:

# a) Draw it on `screen`.

# b) Use the color `(0, 125, 255)` (RGB).

# c) Use `pygame.Rect(30, 30, 60, 60)` to set the rectangle position and size:

# - x = 30, y = 30

# - width = 60, height = 60

# 8) Update the display using `pygame.display.flip()` to show the rectangle

# and any changes on the window.