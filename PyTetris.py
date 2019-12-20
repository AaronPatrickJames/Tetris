import pygame
import random
import os
import sys

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
BACKFILL = (0,0,0)

#Each Block
class blocks:

    def __init__(self):
        self.x = 250
        self.y = 2

    def time_fall(self):
        gameDisplay.fill(BACKFILL)
        self.fall_y = 10
        self.y += self.fall_y
        if self.y>755: self.y = 755 #this is where save state would be added
        
    def move_left(self):
        gameDisplay.fill(BACKFILL)
        self.move_x = -50
        self.x += self.move_x
        if self.x<50: self.x = 50
        
    def move_right(self):
        gameDisplay.fill(BACKFILL)
        self.move_x = 50
        self.x += self.move_x
        if self.x>500: self.x = 500

    def rotate(self):
        pass

    def place(self):
        pass
        
#line
class line_tile(blocks):

    def line(self):
        self.color = (90,120,255)#blueish
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+150,45,45])


#key_check function
def key_check(event, shape):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            shape.move_left()
        if event.key == pygame.K_RIGHT:
            shape.move_right()
        if event.key == pygame.K_SPACE:
            print("Space Bar")
        if event.key == pygame.K_UP:
            print("Up")
        
#Run Game Loop
def game_logic_loop():
    shape = line_tile()
    #when false is returned, return score, time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        boarder_maker()    
        shape.line()
        pygame.display.update()
        key_check(event, shape)
        shape.time_fall()
        clock.tick(7)

#make white boarders
def boarder_maker():
    for i in range(0,20):
        pygame.draw.rect(gameDisplay, (255,255,255), [1,((50*i)+2),47,47])
    for i in range(0,20):
        pygame.draw.rect(gameDisplay, (255,255,255), [550,((50*i)+2),47,47])
        

#Main 
def main():
    game_logic_loop()





if __name__ == "__main__":
    main()
