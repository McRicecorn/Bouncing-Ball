import pygame
import sys

# Pygame starten
pygame.init()

# Fenster
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Ball
x, y = 250, 200
dx, dy = 3, 2
radius = 20
color = (255, 0, 0)

x1, y1 = 300, 150
dx1, dy1 = 3, 2
radius = 20
color1 = (170, 20, 100)

# Spiel-Loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ball bewegen
    x += dx
    y += dy

    x1 += dx1
    y1 += dy1
    # Zweiten Ball bewegen
    if x1 - radius <= 0 or x1 + radius >= WIDTH:
        dx1 = -dx1
    if y1 - radius <= 0 or y1 + radius >= HEIGHT:
        dy1 = -dy1
    

    # Wände prüfen
    if x - radius <= 0 or x + radius >= WIDTH:
        dx = -dx
    if y - radius <= 0 or y + radius >= HEIGHT:
        dy = -dy

    # Zeichnen
    screen.fill((255, 255, 255))  # Hintergrund
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.draw.circle(screen, color1, (x1, y1), radius)
    pygame.display.flip()

    clock.tick(60)
