import random
import time
import pygame
import sys

# 设置游戏参数
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 设置游戏对象
class Snake:
    def __init__(self):
        self.body = [(100, 100), (120, 100), (140, 100)]
        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            self.body.insert(0, (self.body[0][0] + BLOCK_SIZE, self.body[0][1]))
            self.body.pop()
        elif self.direction == 'left':
            self.body.insert(0, (self.body[0][0] - BLOCK_SIZE, self.body[0][1]))
            self.body.pop()
        elif self.direction == 'up':
            self.body.insert(0, (self.body[0][0], self.body[0][1] - BLOCK_SIZE))
            self.body.pop()
        elif self.direction == 'down':
            self.body.insert(0, (self.body[0][0], self.body[0][1] + BLOCK_SIZE))
            self.body.pop()

    def check_collision(self):
        if self.body[0][0] < 0 or self.body[0][0] >= SCREEN_WIDTH or self.body[0][1] < 0 or self.body[0][1] >= SCREEN_HEIGHT:
            return True
        for i in range(1, len(self.body)):
            if self.body[0] == self.body[i]:
                return True
        return False

    def check_eat(self, food):
        if self.body[0] == food:
            return True
        return False

class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

    def generate(self):
        self.position = (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('贪吃蛇')
clock = pygame.time.Clock()

snake = Snake()
food = Food()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
            elif event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'

    snake.move()

    screen.fill(BLACK)
    for pos in snake.body:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))

    if snake.check_collision():
        print('Game Over!')
        pygame.quit()
        sys.exit()
    elif snake.check_eat(food):
        food.generate()

    pygame.display.flip()
    clock.tick(SPEED)