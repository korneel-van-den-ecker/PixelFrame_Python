
#import evdev
from evdev import InputDevice, categorize, ecodes
#from gameOfSnake import SnakeGame
from snake import Snake, Move
from pixelFrame import  Frame
import sys
#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)
snake = Snake(Frame(16,16),3,4,0xff0000)

while 1 :
    #evdev takes care of polling the controller in a loop

    
    for event in gamepad.read_loop():
        #filters by event type
        #print(event.value)
        #print(event.code)
        #if event.type == ecodes.EV_KEY:
            #print(event)
        #if event.type == ecodes.ABS:
        if event.code == 17 and event.value == -1:
            print("OMHOOG")
            snake.move(Move.UP,True,True)
        if event.code == 17 and event.value == 1:
            print("OMLAAG")
            snake.move(Move.DOWN,True,True)
        if event.code == 16 and event.value == -1:
            print("LINKS")
            snake.move(Move.LEFT,False,True)
        if event.code == 16 and event.value == 1:
            print("RECHTS")
            snake.move(Move.RIGHT,False,True)
