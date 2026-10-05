import random
import pygame

CELL = 30
COLS = 20
ROWS = 20
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS

BACKGROUND = (20, 20, 30)
SNAKE_COLOR = (60, 200, 90)
HEAD_COLOR = (120, 255, 150)
FOOD_COLOR = (230, 60, 60)
TEXT_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)


def new_food(snake):
    free = [(x, y) for x in range(COLS) for y in range(ROWS)
            if (x, y) not in snake]
    if not free:
        return None
    return random.choice(free)


def new_game():
    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)
    return snake, direction, new_food(snake), 0


def draw_text(text, text_font, y):
    image = text_font.render(text, True, TEXT_COLOR)
    rect = image.get_rect(center=(WIDTH // 2, y))
    screen.blit(image, rect)


snake, direction, food, score = new_game()
next_direction = direction
game_over = False
message = ""
running = True

while running:
    # 1. LISTEN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score = new_game()
                    next_direction = direction
                    game_over = False
                elif event.key == pygame.K_q:
                    running = False
            else:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    next_direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    next_direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    next_direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    next_direction = (1, 0)

    # 2. MOVE
    if not game_over:
        direction = next_direction
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        hit_wall = not (0 <= head[0] < COLS and 0 <= head[1] < ROWS)
        if hit_wall or head in snake:
            game_over = True
            message = "Game over!"
        else:
            snake.insert(0, head)
            if head == food:
                score += 1
                food = new_food(snake)
                if food is None:
                    game_over = True
                    message = "You win!"
            else:
                snake.pop()

    # 3. DRAW
    screen.fill(BACKGROUND)
    if food is not None:
        pygame.draw.rect(screen, FOOD_COLOR,
                         (food[0] * CELL, food[1] * CELL, CELL, CELL))
    for i, (x, y) in enumerate(snake):
        color = HEAD_COLOR if i == 0 else SNAKE_COLOR
        pygame.draw.rect(screen, color,
                         (x * CELL + 1, y * CELL + 1, CELL - 2, CELL - 2))
    score_image = font.render("Score: " + str(score), True, TEXT_COLOR)
    screen.blit(score_image, (10, 10))

    if game_over:
        draw_text(message, big_font, HEIGHT // 2 - 30)
        draw_text("Press R to play again, Q to quit", font, HEIGHT // 2 + 30)

    pygame.display.flip()
    clock.tick(min(8 + score // 3, 20))

pygame.quit()