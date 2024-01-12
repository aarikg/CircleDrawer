import pyautogui
import math
import time
 
R = 400

(x,y) = pyautogui.size()

(X,Y) = pyautogui.position(960,520) # dot

pyautogui.moveTo(X+R,Y)
time.sleep(3) # switch to tab
pyautogui.mouseDown()
for i in range(360):
    
    # lower = slower + precise, higher = faster + less precise
    if i%1==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
pyautogui.mouseUp()
