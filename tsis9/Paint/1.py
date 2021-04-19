import pygame

Screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Q-ChangeColor || W-Eraser || Arrows Up and Down for size || 1,2,3 to change Shape")

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Screen.fill(WHITE)
Colors = [BLACK, BLUE, GRAY, GREEN, RED]

DefColor = Colors[0]
done = False
draw = False
radius = 2
iterator = 0
CurrentTool = 0
mouse = pygame.mouse.get_pos()
Height = 150
Width = 50

def drawCircle(srf, color, mouse, radius):
    pygame.draw.circle(srf, color, mouse, radius)

def drawRect(srf, color, mouse, Height, Width):
    pygame.draw.rect(Screen,DefColor,(mouse[0]-50,mouse[1]-25,Height,Width))


def drawLine(srf, color, start, end, radius=1):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)


while not done:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                iterator += 1
                if iterator > 4:
                    iterator = 0
                    DefColor = Colors[iterator]
                else:
                    DefColor = Colors[iterator]
            if event.key == pygame.K_w:
                DefColor = WHITE
            if event.key == pygame.K_DOWN:
                if Height > 11 and Width > 11:
                    Width-=10
                    Height-=10
                if radius > 1:
                    radius -= 1
            if event.key == pygame.K_UP:
                radius += 1
                Width+=10
                Height+=10
            if event.key == pygame.K_1:
                CurrentTool = 0
                radius = 3
            if event.key == pygame.K_2:
                CurrentTool = 1
                radius = 50
            if event.key == pygame.K_3:
                CurrentTool = 2

        print(mouse)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if CurrentTool == 1:
                drawCircle(Screen,DefColor,mouse,radius)

            if CurrentTool == 2:
                drawRect(Screen,DefColor,mouse,Height,Width)
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if event.type == pygame.MOUSEMOTION:
            if CurrentTool == 0:
                if draw:
                    pygame.draw.circle(Screen, DefColor, event.pos, radius)
                    drawLine(Screen, DefColor, event.pos, last_pos, radius)
                last_pos = event.pos

            pygame.display.update()
