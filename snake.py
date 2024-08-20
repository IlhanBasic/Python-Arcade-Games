import random
import os
import time

WIDTH = 20
HEIGHT = 20

def snake_game():
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_length = 1
    direction = 'RIGHT'
    food_x = random.randint(0, WIDTH - 1)
    food_y = random.randint(0, HEIGHT - 1)
    snake_positions = [(snake_x, snake_y)]

    def draw_board():
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in snake_positions:
                    print('O', end=' ')
                elif (x, y) == (food_x, food_y):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(f'Score: {snake_length - 1}')

    def move_snake(direction):
        nonlocal snake_x, snake_y, food_x, food_y, snake_length, snake_positions

        if direction == 'RIGHT':
            snake_x += 1
        elif direction == 'LEFT':
            snake_x -= 1
        elif direction == 'UP':
            snake_y -= 1
        elif direction == 'DOWN':
            snake_y += 1

        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            food_x = random.randint(0, WIDTH - 1)
            food_y = random.randint(0, HEIGHT - 1)

        snake_positions.append((snake_x, snake_y))

        if len(snake_positions) > snake_length:
            snake_positions.pop(0)

    while True:
        draw_board()
        time.sleep(0.2)

        command = input('Unesite komandu (WASD za kretanje, Q za izlaz): ').upper()

        if command == 'W':
            direction = 'UP'
        elif command == 'S':
            direction = 'DOWN'
        elif command == 'A':
            direction = 'LEFT'
        elif command == 'D':
            direction = 'RIGHT'
        elif command == 'Q':
            break

        move_snake(direction)

        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT or (snake_x, snake_y) in snake_positions[:-1]:
            print('Game Over!')
            play_again = input('Želite li igrati ponovo? (Y/N): ').upper()
            if play_again == 'Y':
                snake_x, snake_y = WIDTH // 2, HEIGHT // 2
                snake_positions = [(snake_x, snake_y)]
                snake_length = 1
                direction = 'RIGHT'
                food_x = random.randint(0, WIDTH - 1)
                food_y = random.randint(0, HEIGHT - 1)
            else:
                break
