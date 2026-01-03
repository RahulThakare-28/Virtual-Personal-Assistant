import pyautogui

def get_cursor():
    x, y = pyautogui.position()
    return {"x": x, "y": y}
