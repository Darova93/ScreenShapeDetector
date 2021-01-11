from Tools.EventStore import EventStore

def OnKeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        EventStore.storeKey(event.Ascii)
    return True