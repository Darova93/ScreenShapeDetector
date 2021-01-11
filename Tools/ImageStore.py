import pyautogui
    
class ImageStore:

    class __ImageStore:
        def __init__(self, path):
            self.path = str(path)
            self.count = 1
        def increaseCount(self):
            self.count += 1
        def __str__(self):
            return repr(self) + self.count + self.path

    instance = None

    def __init__(self, path):
        if not ImageStore.instance:
            ImageStore.instance = ImageStore.__ImageStore(path)
        else :
            ImageStore.instance.path = path
        
    def TakeScreenshot():
        filePath = ImageStore.instance.path + "\image" + str(ImageStore.instance.count) + ".png"

        image = pyautogui.screenshot(filePath, region=(860, 340, 200, 400)) 

        ImageStore.instance.count += 1