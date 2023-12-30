import pyautogui
from math import cos, sin

#you can have fun with radius and steps this just works the best for me idk
steps = 1000
radius = 400

#gathering current x and y coordiantes of cursor
xcursor = pyautogui.position()[0]
ycursor = pyautogui.position()[1]

#yup whole logic is this
#you can use pi in this logic for calculating i and in for loop but idk this was easiest and fastest way
pyautogui.moveTo(xcursor + radius, ycursor)
pyautogui.mouseDown()
for i in range(7):
    x = cos(i) * radius
    y = sin(i) * radius
    pyautogui.moveTo(xcursor + x, ycursor + y)
    i += 6 / steps
pyautogui.mouseUp()

#it works the best if you place your cursor in middle on center dot
