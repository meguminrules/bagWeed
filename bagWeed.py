import pydirectinput as di
import keyboard as k
from time import sleep
from threading import Thread
import os

def detectKeyPress(key):
    while 1:
        if (k.is_pressed(key)):
            print("Stopped bagging")
            sleep(0.2)
            os._exit(0)

t = Thread(target=detectKeyPress, args=["k"])

#Point(x=749, y=328) weed bag
#Point(x=651, y=352) weed
#Point(x=939, y=678) combine
def bagWeed():
    x = 0
    while 1:
        di.press("tab")
        sleep(0.2)
        di.mouseDown(749, 328)
        di.moveTo(651, 352)
        di.mouseUp()
        sleep(0.1)
        di.click(939, 678)
        sleep(8)
        x += 1
        print("Bagged " + str(x))

print("Press 'K' to begin bagging")

while 1:
    if k.is_pressed("k"):
        sleep(0.5)
        t.start()
        break

print("Started bagging")
bagWeed()