Tetris PyGame
SUDO Code / Read Me:




Tetris has several parts listed below: (Non break Out)
Types of blocks
Grids
movement of blocks
timer
check for row completed. 
change of block orientation
score :amount of rows cleared
speed - based on time/or rows completed : work on after working base piece


Types of Blocks: (Breakout)
All Blocks in tetris are 4 blocks in size.
There are the following shapes
Line = A Stright Line 4 blocks tall
L shape = 3 blocks tall 1 block to right of last block
Reverce L = 3 blocks tall 1 block to left of last block
z shape = 2 blocks tall, 1 block top left one block bottom right
reverse z = 2 blocks tall, 1 block topright one block bottom left
square = 2 blocks tall, 2 blocks wide
T shape = 2 blcoks tall, 1 block on the top left, 1 block top right

Grids:
Grid appears to be a 2tallx1wide ratio. 
so a 10x 20y board seems standard

movement of blocks: (second to last item we work on)
this is left, right, space, 
left moves left
right move right
down moved down faster
space slaps piece down
THINK ABOUT STOPPING PIECES. How do they stop? do they fall? are they locked? 

time: (easy)
use a timer ? simple in python game.time()

block orientation: (third to last)
this is up on keypad
rotates block positions (this one might be more complex than innitally thought)

check row completed: (simple)
when block placement is finished. (cant go down anymore) 
run logic loop to check if 4 rows, 3 rows, 2 rows, 1, row == true accross it. if any item returns false throw next piece. 



