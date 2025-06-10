import random


def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            maze[i][j] = ' ' if random.random() > 0.3 else '#'
    maze[1][1] = 'P'  # Player's starting position
    maze[rows - 2][cols - 2] = 'E'  # Exit position
    return maze


def print_maze(maze):
    for row in maze:
        print(''.join(row))


def move_player(maze, direction, player_pos):
    x, y = player_pos
    maze[x][y] = ' '  # Clear current position
    if direction == 'w' and maze[x - 1][y] != '#':
        x -= 1
    elif direction == 's' and maze[x + 1][y] != '#':
        x += 1
    elif direction == 'a' and maze[x][y - 1] != '#':
        y -= 1
    elif direction == 'd' and maze[x][y + 1] != '#':
        y += 1
    maze[x][y] = 'P'  # Update new position
    return (x, y)


def play_game():
    rows, cols = 10, 10
    maze = generate_maze(rows, cols)
    player_pos = (1, 1)
    print("Welcome to the Maze Escape Game!")
    print("Use 'w', 'a', 's', 'd' to move up, left, down, and right respectively.")
    print("Reach 'E' to escape the maze!")

    while True:
        print_maze(maze)
        move = input("Your move: ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Invalid move! Use 'w', 'a', 's', 'd'.")
            continue
        player_pos = move_player(maze, move, player_pos)
        if player_pos == (rows - 2, cols - 2):
            print_maze(maze)
            print("Congratulations! You escaped the maze!")
            break


if __name__ == "__main__":
    play_game()
