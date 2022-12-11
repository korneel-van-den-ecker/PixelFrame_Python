from threading import Thread
import time
from evdev import InputDevice, categorize, ecodes
#from gameOfSnake import SnakeGame
from snake import Snake, Move
from pixelFrame import  Frame
#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad1 = InputDevice('/dev/input/event1')
#gamepad2 = InputDevice('/dev/input/event1')

#prints out device info at start
print(gamepad1)
snake = Snake(Frame(16,8),4,5,0xffd007f)
volgendeMove = Move.DOWN

def snakeControl():
    global volgendeMove  
    while 1:
        snake.move(volgendeMove,False,True)
        time.sleep(0.1)

t1 = Thread(target=snakeControl)
t1.start()

for event in gamepad1.read_loop():
    print("Start")  
    if event.code == 17 and event.value == -1:
        volgendeMove = Move.UP
        print("OMHOOG")
    if event.code == 17 and event.value == 1:
        volgendeMove = Move.DOWN
        print("OMLAAG")
    if event.code == 16 and event.value == -1:
        volgendeMove = Move.LEFT
        print("LINKS")
    if event.code == 16 and event.value == 1:
        volgendeMove = Move.RIGHT
        print("RECHTS")


