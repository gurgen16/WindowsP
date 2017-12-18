import pyhk
import webbrowser
import pyautogui
import win32gui
import os.path
import time

# iPath=r'C:\Users\Bob-Lap\Pictures\2300857-star-wars-kit-fisto-coloring-pages.png'
pPath=os.path.abspath("Penis.jpg")

hot = pyhk.pyhk()


def FloatyP():
    print('Jop')
    webbrowser.open(pPath)
    # foto = win32gui.FindWindow(None, r'Penis.png - InfranView')
    # print(foto)
    time.sleep(0.2)
    fotos=win32gui.GetForegroundWindow()
    b=600
    h=700
    x = 20
    y = 20
    x_d = 2
    y_d = 2
    x_r=1
    y_r=1
    yo=True
    while yo==True:
        if (x+x_d+b>=1920)or(x+x_d<=0):
            x_d = x_d*(-1)
        if (y+y_d+h>=1080)or(y+y_d<=0):
            y_d = y_d*(-1)
        x=x+x_d
        y=y+y_d
        win32gui.MoveWindow(fotos, x, y, b, h,True)
        time.sleep(0.01)

def Stopo():
    hot.end()


winp=hot.addHotkey(['Win','P'],FloatyP)
stop=hot.addHotkey(['P'],Stopo)
hot.start()
