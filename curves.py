import pygame
from positions import Position
def LinearCurve(positions, t, screen, color, trigger=True):
    P0_x = (1 - t) * positions[0].x
    P0_y = (1 - t) * positions[0].y

    P1_x = t * positions[1].x
    P1_y = t * positions[1].y

    curve = (P0_x + P1_x, P0_y + P1_y)
    
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, color, (positions[0].x, positions[0].y),(int(curve[0]), int(curve[1])), 5)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    elif trigger == False:
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
        return (int(curve[0]), int(curve[1]))

def QuadraticCurve(positions, t, screen, color, curve_list, green, trigger= True):

    P0_x = pow((1-t), 2) * positions[0].x
    P0_y = pow((1-t), 2) * positions[0].y

    P1_x = 2 * (1-t) * t * positions[1].x
    P1_y = 2 * (1-t) * t * positions[1].y

    P2_x = t ** 2 * positions[2].x
    P2_y = t ** 2 * positions[2].y

    curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
        first_line = [positions[0], positions[1]]
        second_line = [positions[1], positions[2]]

        a = LinearCurve(first_line, t,  screen, green, False)
        b = LinearCurve(second_line, t,  screen, green, False)

        pygame.draw.line(screen, green, a, b, 2)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))

def CubicCurve(positions, t, screen, color, curve_list, green, blue, quad_curve, quad_curve1, quad_curve2):
    P0_x = pow((1 - t), 3) * positions[0].x
    P0_y = pow((1 - t), 3) * positions[0].y

    P1_x = 3 * pow((1-t), 2) * t * positions[1].x
    P1_y = 3 * pow((1-t), 2) * t * positions[1].y

    P2_x = 3 * (1-t) * pow(t, 2) * positions[2].x
    P2_y = 3 * (1-t) * pow(t, 2) * positions[2].y

    P3_x = pow(t, 3) * positions[3].x
    P3_y = pow(t, 3) * positions[3].y

    curve = (P0_x + P1_x + P2_x + P3_x, P0_y + P1_y + P2_y + P3_y)

    pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
    pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
    pygame.draw.line(screen, (0, 0, 0), (positions[2].x, positions[2].y), (positions[3].x, positions[3].y), 1)

    first_line = [positions[0], positions[1]]
    second_line = [positions[1], positions[2]]
    third_line = [positions[2], positions[3]]
    fourth_line = [positions[0], positions[1], positions[2]]
    fifth_line = [positions[1], positions[2], positions[3]]
    sixth_line = [positions[0], positions[2], positions[3]]

    a = LinearCurve(first_line, t,  screen, green, False)
    b = LinearCurve(second_line, t,  screen, green, False)
    c = LinearCurve(third_line, t,  screen, green, False)

    pygame.draw.line(screen, green, a, b, 2)
    pygame.draw.line(screen, green, b, c, 2)

    QuadraticCurve(fourth_line, t, screen, (100, 100, 0), quad_curve, green)
    QuadraticCurve(fifth_line, t, screen, (100, 100, 0), quad_curve1, green)
    QuadraticCurve(sixth_line, t, screen, (100, 100, 0), quad_curve2, green, False)

    position_1 = Position(a[0], a[1])
    position_2 = Position(b[0], b[1])
    position_3 = Position(c[0], c[1])

    line1 = [position_1, position_2]
    line2 = [position_2, position_3]

    start = LinearCurve(line1, t, screen, blue, False)
    end = LinearCurve(line2, t, screen, blue, False)

    pygame.draw.line(screen, blue, start, end, 2)

    pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))
