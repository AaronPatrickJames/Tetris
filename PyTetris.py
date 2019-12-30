import pygame
import random
import os
import sys
import copy

gameDisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption("Tetris")
BOARDDICT = {}
clock = pygame.time.Clock()
BACKFILL = (0,0,0)

#Each Block
class blocks:

    def __init__(self):
        self.x = 250
        self.y = 2
        self.state = 0
        self.lock = 0

    def time_fall(self):
        gameDisplay.fill(BACKFILL)
        self.fall_y = 2
        self.y += self.fall_y
        if self.y>753: self.y = 753
        
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
        gameDisplay.fill(BACKFILL)
        self.state += 1
        if self.state>3: self.state = 0

    def rapid_down(self):
        gameDisplay.fill(BACKFILL)
        self.fall_y = 10
        self.y += self.fall_y
        if self.y>753: self.y = 753
        
    def place(self):
        pass
        
#line
class line_tile(blocks):

    def draw(self):
        self.color = (90,120,255)#blueish
        self.name = "Line"
        if self.state == 0 or self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+150,45,45])
        else:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+150, self.y,45,45])

#Reverse L
class reverse_l_tile(blocks):

    def draw(self):
        self.color = (0,0,255)
        self.name = "Reverse L"
        if self.state == 0:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y+100,45,45])
        if self.state == 1:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y-50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
        if self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
        if self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y+50,45,45])

#L
class l_tile(blocks):
    
    def draw(self):
        self.color = (255,165,0)
        self.name = "L"
        if self.state == 0:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+100,45,45])
        if self.state == 1:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
        if self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
        if self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y-50,45,45])

#Reverse Z
class reverse_z_tile(blocks):

    def draw(self):
        self.color = (0,255,0)
        self.name = "Reverse Z"
        if self.state == 0 or self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y+50,45,45])
        if self.state == 1 or self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y-50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
#Z
class z_tile(blocks):
    
    def draw(self):
        self.color = (255,0,0)
        self.name = "Z"
        if self.state == 0 or self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y+50,45,45])
        if self.state == 1 or self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y-50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y+50,45,45])

            
#Square
class square_tile(blocks):

    def draw(self):
        self.color = (255,255,0)
        self.name = "Square"
        if self.state == 0 or self.state == 1 or self.state == 2 or self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
            
#T
class t_tile(blocks):
    
    def draw(self):
        self.color = (75,0,130)
        self.name = "T"
        if self.state == 0:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+100, self.y,45,45])
        if self.state == 1:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y-50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
        if self.state == 2:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x-50, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
        if self.state == 3:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x+50, self.y+50,45,45])
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y+100,45,45])
            


#key_check function
def key_check(event, shape):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            shape.move_left()
        if event.key == pygame.K_RIGHT:
            shape.move_right()
        if event.key == pygame.K_DOWN:
            shape.rapid_down()
        if event.key == pygame.K_SPACE:
            print("Space Bar")
        if event.key == pygame.K_UP:
            shape.rotate()

#spawns a new shape
def spawn_new_shape():
    picker = random.randint(0,6)
    if picker == 0:
        shape = line_tile()
    elif picker == 1:
        shape = reverse_l_tile()
    elif picker == 2:
        shape = l_tile()
    elif picker == 3:
        shape = reverse_z_tile()
    elif picker == 4:
        shape = z_tile()
    elif picker == 5:
        shape = square_tile()
    else:
        shape = t_tile()

    return shape

#Saves the state of locked objects in a dict - BOARDDICT
def board_save(shape):
    #make key from length
    key = len(BOARDDICT)
    #make value from shape items
    name = copy.deepcopy(shape.name)
    color = copy.deepcopy(shape.color)
    x = copy.deepcopy(shape.x)
    y = copy.deepcopy(shape.y)
    state = copy.deepcopy(shape.state)
    
    values = [name, color, x, y, state]
    BOARDDICT.update(key = values)
    print(BOARDDICT)
    
    
#Changes Lock state, calls new object spawner
def lock_shape(shape):
    if shape.y == 753:
        shape.lock = 1

    #lock Shape on board and call new shape
    if shape.lock == 1:
        board_save(shape)
        shape = spawn_new_shape()
        
    return(shape)
    
#Run Game Loop
def game_logic_loop():
    shape = spawn_new_shape()
    #when false is returned, return score, time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        boarder_maker()
        #board_printer()
        shape.draw()
        pygame.display.update()
        key_check(event, shape)
        shape.time_fall()
        #RunLockStateCheck
        shape = lock_shape(shape)
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
