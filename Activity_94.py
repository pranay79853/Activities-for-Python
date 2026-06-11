# 1) Import required modules:
#    a) Import `pygame` to create the game window, sprites, and handle events.
import pygame
#    b) Import `random` to place sprites at random positions.
import random
# 2) Create constants for easy changes:
#    a) `SCREEN_WIDTH`, `SCREEN_HEIGHT` for window size.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#    b) `MOVEMENT_SPEED` for how fast the sprite moves.
MOVEMENT_SPEED = 5
#    c) `FONT_SIZE` for the win message size.
FONT_SIZE = 36
# 3) Initialize pygame using `pygame.init()`.
pygame.init()
# 4) Load the background image `bg.jpg` and scale it to fit the screen size
#    using `pygame.transform.scale(...)`.
pygame.display.set_caption("Sprite Collision")
background_image = pygame.transform.scale(pygame.image.load("Background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
# 5) Load the font once using `pygame.font.SysFont("Times New Roman", FONT_SIZE)`.
pygame_font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
# 6) Create a class `Sprite` that inherits from `pygame.sprite.Sprite`.
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(
        min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height),0)

# 9) Create the game window using `pygame.display.set_mode(...)`
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
#    and set the title to "Sprite Collision".

# 10) Create a sprite group `all_sprites = pygame.sprite.Group()` to store and draw sprites.
all_sprites = pygame.sprite.Group()
sprite1 = Sprite("Player.png", 50, 50)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite("Enemy.png", 30, 20)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen = pygame.display.get_surface()
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = pygame_font.render("You win!", True, pygame.Color('white'))
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, text_rect)

    pygame.display.flip()
    clock.tick(90)
pygame.quit()
# 15) Handle events:
#     a) If the user closes the window (`pygame.QUIT`), stop the loop.
#     b) If the user presses the 'X' key, stop the loop.

# 16) If the game is not won yet (`if not won`):
#     a) Detect arrow key presses using `pygame.key.get_pressed()`.
#     b) Calculate `x_change` and `y_change` based on key presses and speed.
#     c) Move `sprite1` using `sprite1.move(x_change, y_change)`.

# 17) Check collision between `sprite1` and `sprite2` using `colliderect()`:
#     a) If they collide, remove `sprite2` from the sprite group.
#     b) Set `won = True`.

# 18) Draw everything:
#     a) Draw the background image using `screen.blit(background_image, (0, 0))`.
#     b) Draw all sprites using `all_sprites.draw(screen)`.

# 19) If the player has won:
#     a) Render the text "You win!" using the font.
#     b) Display the text at the center of the screen using `blit`.

# 20) Update the screen using `pygame.display.flip()`.

# 21) Limit the frame rate to 90 FPS using `clock.tick(90)`.

# 22) When the game loop ends, close pygame using `pygame.quit()`.