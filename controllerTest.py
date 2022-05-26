
#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event1')

#prints out device info at start
print(gamepad)

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
    if event.code == 17 and event.value == 1:
        print("OMLAAG")
    if event.code == 16 and event.value == -1:
        print("LINKS")
    if event.code == 16 and event.value == 1:
        print("RECHTS")
