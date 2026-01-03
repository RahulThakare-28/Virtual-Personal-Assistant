import pygetwindow as gw

def get_active_app():
    win = gw.getActiveWindow()
    return win.title if win else "Unknown"
