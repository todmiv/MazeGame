import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Set up the maze
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X...........X......X",
    "X..XXXXX.X.XXXXX..X",
    "X........X........EX",
    "XXXXXXXXXXXXXXXXXXXX"
]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player_size = 20
player_x = 50
player_y = 50

# Set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Check for collision with walls
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "X":
                wall_rect = pygame.Rect(col*player_size, row*player_size, player_size, player_size)
                if wall_rect.collidepoint(player_x, player_y):
                    player_x, player_y = 50, 50

    # Draw the screen
    screen.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "X":
                pygame.draw.rect(screen, BLACK, (col*player_size, row*player_size, player_size, player_size))
            elif maze[row][col] == "E":
                pygame.draw.rect(screen, RED, (col*player_size, row*player_size, player_size, player_size))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))

    # Check for win condition
    if maze[int(player_y/player_size)][int(player_x/player_size)] == "E":
        print("You win!")
        running = False

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
