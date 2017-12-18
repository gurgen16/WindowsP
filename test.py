import win32gui

def testo(hw,ok):
    print(hw)

yo=''
win32gui.EnumWindows(testo,yo)