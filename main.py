import pygame
from positions import Position
from curves import *

width, height = 1920, 1080
size = (width, height)

pygame.init()
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
speed = 0.002
linear_positions = [Position(100, 800, "P0"), Position(300, 200, "P1")]
Quadratic_positions = [Position(660, 800, "P0"), Position(880, 450, "P1"), Position(720, 200, "P2")]
cubic_positions = [Position(1050, 800, "P0"), Position(1280, 200, "P1"), Position(1420, 800, "P2"), Position(1800, 200, "P3")]

quadratic_curve = []
cubic_curve = []
curve1 = []
curve2 = []
curve3 = []

run = True
while run:
    screen.fill(white)
    clock.tick(fps)
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Bezier Curve - FPS : {}".format(frameRate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    # Gui Text
    text = font.render(" T = " + str(t)[:5], True, black)
    textRect = text.get_rect()
    textRect.center = (960, 100)
    screen.blit(text, textRect)
    linear = font.render("Linear " , True, black)
    
    textRect = linear.get_rect()
    textRect.center = (240, 120)
    screen.blit(linear, textRect)
    Quadratic = font.render("Quadratic", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (620, 120)
    screen.blit(Quadratic, textRect)

    cubic = font.render("Cubic", True, black)
    textRect = cubic.get_rect()
    textRect.center = (1400, 120)
    screen.blit(cubic, textRect)

    #separator ---- | ----- | ------
    pygame.draw.line(screen, purple, (480, 850), (480, 150), 1)
    pygame.draw.line(screen, purple, (950, 850), (950, 150), 1)

    LinearCurve(linear_positions, t, screen, red)
    QuadraticCurve(Quadratic_positions, t, screen, red, quadratic_curve, green)
    CubicCurve(cubic_positions, t, screen, red, cubic_curve, green, blue, curve1, curve2, curve3)

    if len(cubic_curve) > 2:
        pygame.draw.lines(screen, (179, 179, 179),False,  curve1, 3)
        pygame.draw.lines(screen, (179, 179, 179),False,  curve3, 3)
        pygame.draw.lines(screen, (179, 179, 179),False,  curve2, 3)
        pygame.draw.lines(screen, red,False,  cubic_curve, 5)

    if len(quadratic_curve) > 2:
        pygame.draw.lines(screen, red,False,  quadratic_curve, 5)

    if t >= 1:
        t = 0
        quadratic_curve.clear()
        cubic_curve.clear()
        curve1.clear()
        curve2.clear()
        curve3.clear()

    # draw points
    for point in linear_positions:
        point.display(screen, black)
    for point in Quadratic_positions:
        point.display(screen, black)
    for point in cubic_positions:
        point.display(screen, black)

    t += speed
    pygame.display.update()

pygame.quit()
