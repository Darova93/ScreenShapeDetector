from Tools.ImageStore import ImageStore

def left_down(event):
    ImageStore.TakeScreenshot()
    return True

def right_down(event):
    print("right click")
    return True    

def middle_down(event):
    print("middle click")
    return True