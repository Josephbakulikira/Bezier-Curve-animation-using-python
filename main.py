import pygame
import os

from positions import Position
from curves import *

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
size = (width, height)
pygame.init()
pygame.display.set_caption("Bezier curves")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 32)

#colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)
blue = (2, 146, 242)
purple = (205, 163, 255)

#parameters
t = 0
speed = 0.005
linear_positions = [Position(100, 800, "P0"), Position(300, 200, "P1")]
Quadratic_positions = [Position(660, 800, "P0"), Position(880, 450, "P1"), Position(720, 200, "P2")]
cubic_positions = [Position(1050, 800, "P0"), Position(1280, 200, "P1"), Position(1420, 800, "P2"), Position(1800, 200, "P3")]
quadratic_curve = []
cubic_curve = []

run = True
while run:
    screen.fill(white)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for point in linear_positions:
        point.display(screen, black)


    for point in Quadratic_positions:
        point.display(screen, black)

    for point in cubic_positions:
        point.display(screen, black)

    text = font.render("T = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (960, 120)
    screen.blit(text, textRect)
    #separator
    pygame.draw.line(screen, purple, (480, 850), (480, 150), 1)
    pygame.draw.line(screen, purple, (950, 850), (950, 150), 1)

    LinearCurve(linear_positions, t, screen, red)
    QuadraticCurve(Quadratic_positions, t, screen, red, quadratic_curve, green)
    CubicCurve(cubic_positions, t, screen, red, cubic_curve, green, blue)

    if len(quadratic_curve) > 2:
        pygame.draw.lines(screen, red,False,  quadratic_curve, 5)
    if len(cubic_curve) > 2:
        pygame.draw.lines(screen, red,False,  cubic_curve, 5)

    if t >= 1:
        t = 0
        quadratic_curve.clear()
        cubic_curve.clear()
    t += speed
    pygame.display.update()

pygame.quit()
