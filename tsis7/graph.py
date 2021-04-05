import pygame
from math import pi, sin, cos


pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


bg = pygame.display.set_mode((800, 600))

text = pygame.font.SysFont("Times New Roman",20,False,True)
text2 = pygame.font.SysFont("Times New Roman",15,False,True)

horizontal_string = ("-3П","-2,5П","-2П","-1.5П","-П","-0.5П","0","0.5П","П","1.5П","2П","2.5П","3П")
vertical_string = ("1.00","0.75","0.50","0.25","0.00","-0.25","-0.50","-0.75","-1.00")




text_x = "X"
text_x_render = text.render(text_x,True,BLACK)


test = "TEST"
testrender = text.render(test,True,BLACK)



x_coor = 100

text_sin = "SinX"
text_cos = "CosX"

textsinren = text.render(text_sin,True,BLACK)
textcosren = text.render(text_cos,True,BLACK)





done = False





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    bg.fill(WHITE)
    iterator = 0
    iterator2 = 0
    pygame.display.set_caption("Sin&Cos Graph")
    pygame.draw.rect(bg, BLACK, (70, 10, 660, 540), 2)  
    pygame.draw.line(bg, BLACK, (70, 280), (730, 280), 3)  
    pygame.draw.line(bg, BLACK, (400, 10), (400, 550), 3)  

    pygame.draw.line(bg, BLACK, (70, 40), (730, 40))  
    pygame.draw.line(bg, BLACK, (70, 520), (730, 520))  
    pygame.draw.line(bg, BLACK, (100, 10), (100, 550))  
    pygame.draw.line(bg, BLACK, (700, 10), (700, 550))  

    for x in range(100, 701, 100):
        pygame.draw.line(bg, BLACK, (x, 10), (x, 550))

    for x in range(100, 701, 50):
        pygame.draw.line(bg, BLACK, (x, 10), (x, 30))
        pygame.draw.line(bg, BLACK, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(bg, BLACK, (x, 10), (x, 20))
        pygame.draw.line(bg, BLACK, (x, 550), (x, 540))

    for y in range(40, 521, 60):
        pygame.draw.line(bg, BLACK, (70, y), (730, y))
    for y in range(40, 521, 30):
        pygame.draw.line(bg, BLACK, (70, y), (90, y))
        pygame.draw.line(bg, BLACK, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(bg, BLACK, (70, y), (80, y))
        pygame.draw.line(bg, BLACK, (720, y), (730, y))

    for x in range(100, 700):
        sin_y1 = 240 * sin((x - 100) / 100 * pi)
        sin_y2 = 240 * sin((x - 99) / 100 * pi)
        pygame.draw.aalines(bg, RED, True, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])

    for x in range(100, 700, 2):
        cos_y1 = 240 * cos((x - 100) / 100 * pi)
        cos_y2 = 240 * cos((x - 99) / 100 * pi)
        pygame.draw.aalines(bg, BLUE, True, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])


    for x in range(100, 701, 50):
        if iterator <14:
            fontforhor = pygame.font.SysFont("Arial",15,True,False)
            horrender = fontforhor.render(horizontal_string[iterator],True,BLACK)
            iterator = iterator + 1

            bg.blit(horrender,(x-5,550))
        else:
            break

    for y in range(40, 521, 60):
        if iterator <14:
            fontforver = pygame.font.SysFont("Arial",15,True,False)
            verrender = fontforver.render(vertical_string[iterator2],True,BLACK)
            iterator2 = iterator2 + 1

            bg.blit(verrender,(35,y-10))
        else:
            break
    

    pygame.draw.line(bg, BLUE, (150, 70), (160, 70), 1)
    pygame.draw.line(bg, BLUE, (163, 70), (175, 70), 1)
    pygame.draw.line(bg, BLUE, (179, 70), (190, 70), 1)
    pygame.draw.line(bg, BLUE, (193, 70), (200, 70), 1)
    pygame.draw.line(bg, RED, (150, 50), (200, 50), 1)

    bg.blit(textsinren,(100,40))
    bg.blit(textcosren,(100,60))       
    bg.blit(text_x_render,(396,570))

    pygame.display.update()
    
pygame.quit()




