
#import evdev
from multiprocessing import Process
from threading import Thread
import time
from evdev import InputDevice, categorize, ecodes
#from gameOfSnake import SnakeGame
from snake import Snake, Move
import sys
from pixelFrame import  Frame
#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)
snake = Snake(Frame(16,16),4,5,0xff0000)
volgendeMove = Move.DOWN

def zetParam():
    global volgendeMove  
    while 1:
        snake.move(volgendeMove,False,True)
        time.sleep(0.5)

#if __name__ == "__main__":
#    Process(target = zetParam).start()
#    #Process(target = laatslangBewegen).start()

t1 = Thread(target=zetParam)
t1.start()

for event in gamepad.read_loop():
    print("loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")  
    if event.code == 17 and event.value == -1:
        volgendeMove = Move.UP
        print("OMHOOG")
        #snake.move(Move.UP,False,True)
    if event.code == 17 and event.value == 1:
        volgendeMove = Move.DOWN
        print("OMLAAG")
        #snake.move(Move.DOWN,False,True)
    if event.code == 16 and event.value == -1:
        volgendeMove = Move.LEFT
        print("LINKS")
        #snake.move(Move.LEFT,False,True)
    if event.code == 16 and event.value == 1:
        volgendeMove = Move.RIGHT
        print("RECHTS")
        #snake.move(Move.RIGHT,False,True)
    #while 1:
        #global volgendeMove
        #reet = volgendeMove
        #snake.move(reet,False,True)
        #time.sleep(0.5)
        #print("NU")


#def laatslangBewegen():
    #while 1:
        #global volgendeMove
        #reet = volgendeMove
        #snake.move(reet,False,True)
        #time.sleep(0.5)

