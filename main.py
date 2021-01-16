import pygame
import math
import random


pygame.init()
WIDTH, HEIGHT, = 800,850
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pi Estimation Visualizer by Jonathan Lin')


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



#figures out the distance from the generated location to the center of the circle
def distance( coordinate):
    xSquared = (coordinate[0] - 400) ** 2
    ySquared = (coordinate[1] - 400)**2
    return math.sqrt(xSquared + ySquared)


drewCircle = False #makes sure the outer circle is only drawn once

def main():

    FPS = 300
    clock = pygame.time.Clock()

    angle = 0
    circle_coordinates = []
    while angle <= 360:
        circle_coordinates.append((400 + 400*math.cos(math.radians(angle)),400 - 400*math.sin(math.radians(angle))))

        angle = angle + 0.1

    coords_in_circle = []
    coords_out_circle = []

    
    run = True
    while run:

        #this controls the FPS
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
        #pygame.draw.rect(win,(0,0,0),[200,200,100,100])
        #pygame.draw.circle(win,(BLUE),(400,400),400)
        #pygame.draw.circle(win,RED,(400,400),2)

        


        #draws the outlining circle once
        if drewCircle == False:
            win.fill(BLACK)
            for coordinate in circle_coordinates:
                x = int(coordinate[0])
                y = int(coordinate[1])
                win.set_at((x,y),WHITE)
            drewCircle == True
        
        #white background for all buttons
        pygame.draw.rect(win,WHITE,[0,800,250,50])

        font = pygame.font.Font(None, 32)

        #create blue text for all buttons
        text = font.render('x1', True, BLUE)
        win.blit(text, (12,813))
        text = font.render('x2', True, BLUE)
        win.blit(text, (62,813))
        text = font.render('x5', True, BLUE)
        win.blit(text, (112,813))
        text = font.render('x10', True, BLUE)
        win.blit(text, (158,813))
        text = font.render('x25', True, BLUE)
        win.blit(text, (206,813))


        #draw selected button for speed with text on
        if FPS == 30:
            pygame.draw.rect(win,(BLUE),[0,800,50,50])
            text = font.render('x1', True, WHITE) #turn text to white if button selected cuz of the blue background of button that's selected
            win.blit(text, (12,813))
        if FPS == 60:
            pygame.draw.rect(win,(BLUE),[50,800,50,50])
            text = font.render('x2', True, WHITE)
            win.blit(text, (62,813))
        if FPS == 150:
            pygame.draw.rect(win,(BLUE),[100,800,50,50])
            text = font.render('x5', True, WHITE)
            win.blit(text, (112,813))
        if FPS == 300:
            pygame.draw.rect(win,(BLUE),[150,800,50,50])
            text = font.render('x10', True, WHITE)
            win.blit(text, (158,813))
        if FPS == 750:
            pygame.draw.rect(win,(BLUE),[200,800,50,50])
            text = font.render('x25', True, WHITE)
            win.blit(text, (206,813))
        
        
        mousex = 0
        mousey = 0
        #get position of mouse of clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                mousex = pygame.mouse.get_pos()[0]
                mousey = pygame.mouse.get_pos()[1]
        
        #change buttons
        if mousey > 800:
            if mousex > 0 and mousex < 50:
                FPS = 30
            if mousex > 50 and mousex < 100:
                FPS = 60
            if mousex > 100 and mousex < 150:
                FPS = 150
            if mousex > 150 and mousex < 200:
                FPS = 300
            if mousex > 200 and mousex < 250:
                FPS = 750

        #picks a random coordinate
        x = random.randrange(0,800)
        y = random.randrange(0,800)
        
        
        #depending on if outside or inside, change color accordingly
        if distance((x,y)) <=400:
            coords_in_circle.append((x,y))
        if distance((x,y)) >400:
            coords_out_circle.append((x,y))

        for coord in coords_in_circle:
            win.set_at(coord,GREEN)
        for coord in coords_out_circle:
            win.set_at(coord,RED)


        #calculations to approximate pi
        numberInCircle = len(coords_in_circle)
        numberTotal = len(coords_in_circle) + len(coords_out_circle)
        estimation = round((numberInCircle/numberTotal) * 4,14)

        
        font = pygame.font.Font(None, 22)
        text = font.render('Points within circle: ' + str("{:,}".format(numberInCircle)), True, WHITE)
        win.blit(text, (260,808))
        text = font.render('Total Number of Points: ' + str("{:,}".format(numberTotal)), True, WHITE)
        win.blit(text, (260,830))
        text = font.render('Pi Estimation:', True, WHITE)
        win.blit(text, (650,808))
        text = font.render(str(estimation), True, WHITE)
        win.blit(text, (650,830))

        
        #update the display with all the new visual changes
        pygame.display.update()

        
    
    pygame.quit()

if __name__ == "__main__":
    main()