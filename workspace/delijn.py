import pygetwindow
import time
import os
import pyautogui
import PIL
import pyscreenshot as ImageGrab
import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
import os
import mss

def screenshot():
    # get screensize
    x,y = pyautogui.size()
    print(f"width={x}\theight={y}")

    x2,y2 = pyautogui.size()
    x2,y2=int(str(x2)),int(str(y2))
    print(x2//2)
    print(y2//2)

    # find new window title
    z1 = pygetwindow.getAllTitles()
    time.sleep(1)
    print(len(z1))
    # test with pictures folder
    os.startfile("C:\\Users\\timle\\Downloads")
    time.sleep(1)
    z2 = pygetwindow.getAllTitles()
    print(len(z2))
    time.sleep(1)
    z3 = [x for x in z2 if x not in z1]
    z3 = ''.join(z3)
    time.sleep(3)

    # also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"
    my = pygetwindow.getWindowsWithTitle(z3)[0]
    # quarter of screen screensize
    x3 = x2 // 2
    y3 = y2 // 2
    my.resizeTo(x3,y3)
    # top-left
    my.moveTo(0, 0)
    time.sleep(3)
    my.activate()
    time.sleep(1)

    # save screenshot
    p = pyautogui.screenshot()
    p.save(r'C:\\Users\\timle\\Downloads\\\\p.png')

    # edit screenshot
    # im = PIL.Image.open('C:\\Users\\yourname\\Pictures\\p.png')
    # im_crop = im.crop((0, 0, x3, y3))
    # im_crop.save('C:\\Users\\yourname\\Pictures\\p.jpg', quality=100)

    # close window
    time.sleep(1)
    my.close()

def screenshot(x1, y1, x2, y2):
    # part of the screen
    im=ImageGrab.grab(bbox=(x1, y1, x2, y2)) # X1,Y1,X2,Y2
    return im

def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    if template is None:
        raise FileNotFoundError('Image file not found: {}'.format(image))

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

screenshot(0, 100, 0, 100).show()
screen = screenshot(0, 0, 1920, 1080)
imagesearcharea(screen, 0, 100, 0, 100)