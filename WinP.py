import pyhk
import webbrowser
import pyautogui
import win32gui
import win32con
import os.path
import time
import random

random.seed()
# iPath=r'C:\Users\Bob-Lap\Pictures\2300857-star-wars-kit-fisto-coloring-pages.png'
pPath=os.path.abspath("Penis.jpg")

hot = pyhk.pyhk()


def FloatyP():
    print('Jop')
    webbrowser.open(pPath)
    time.sleep(1)
    foto = win32gui.FindWindow("IrfanView", None)

    win32gui.ShowWindow(foto,win32con.SW_SHOW)
    #win32gui.SetForegroundWindow(foto)
    win32gui.BringWindowToTop(foto)
    #fotos=win32gui.GetForegroundWindow()
    b=600
    h=700
    x = 20
    y = 20
    x_d=2
    y_d=2
    x_r=1
    y_r=1
    yo=True
    count=1
    change=0
    while yo==True:

        if count>change:
            speed=1/random.randint(100,5000)
            change=random.randint(25,1000)
            print(speed,change)

            count=0
        if (x+x_d+b>=2560)or(x+x_d<=0):
            x_d = x_d*(-1)
        if (y+y_d+h>=1440)or(y+y_d<=0):
            y_d = y_d*(-1)
        x=x+x_d
        y=y+y_d
        win32gui.MoveWindow(foto, x, y, b, h,True)

        time.sleep(speed)
        count += 1

# def Stopo():
#     hot.end()


winp=hot.addHotkey(['Win','P'],FloatyP)
# stop=hot.addHotkey(['P'],Stopo)
hot.start()
