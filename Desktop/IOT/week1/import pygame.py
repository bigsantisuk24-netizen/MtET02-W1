pip install pygameimport pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 30)


def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def random_food():
    return (
        random.randrange(0, WIDTH, GRID_SIZE),
        random.randrange(0, HEIGHT, GRID_SIZE)
    )


snake = [(100, 100)]
direction = (GRID_SIZE, 0)

food = random_food()

score = 0

running = True

while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and direction != (0, GRID_SIZE):
        direction = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -GRID_SIZE):
        direction = (0, GRID_SIZE)
    if keys[pygame.K_LEFT] and direction != (GRID_SIZE, 0):
        direction = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-GRID_SIZE, 0):
        direction = (GRID_SIZE, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # Collision with wall
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT
    ):
        break

    # Collision with itself
    if new_head in snake:
        break

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        while True:
            food = random_food()
            if food not in snake:
                break
    else:
        snake.pop()

    # Draw
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0], segment[1], GRID_SIZE, GRID_SIZE)
        )

    draw_text(f"Score: {score}", WHITE, 10, 10)

    pygame.display.flip()

# Game Over
screen.fill(BLACK)
draw_text("Game Over!", RED, WIDTH // 2 - 70, HEIGHT // 2 - 20)
draw_text(f"Score: {score}", WHITE, WIDTH // 2 - 50, HEIGHT // 2 + 20)
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()