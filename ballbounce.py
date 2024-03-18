import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()

x = 2
y = 3
speed = pygame.Vector2(x,y)

position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0

running = True

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    position += speed * dt

    circle = pygame.draw.circle(screen, "white", position, 30)

    if position[0] == 500:
        speed[0] = -x
    elif position[1] == 500:
        speed[1] = -y
    elif position[0] == 0:
        speed[0] = x
    elif position[1] == 0:
        speed[1] = y

    pygame.display.flip()

    dt = clock.tick(60) 
    