import pyautogui
import time


# Some useful Testing methods i used :)

def saveScreenShot():
    # img = pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/Nido.PNG')
    img = pyautogui.locateOnScreen('D:/PokemonRevoBot/assets/Health.PNG')
    # img = pyautogui.locateAllOnScreen('D:/PokemonRevoBot/assets/Health.PNG')
    # img = 58, 144, 82, 11
    if (img != None):
        fileToSave = pyautogui.screenshot(region=img)
        fileToSave.save(r"C:\Users\home\Downloads\DownloadStuff\screenshot_1.png")
        print(img)
    else:
        print("finding img")


def locateMouseOnScreen(seconds=40):
    for i in range(0, seconds):
        print(pyautogui.position())


def locateRGBValueOfMousePositionOnScreen(seconds=40):
    for i in range(0, seconds):
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        print(r, g, b)
        time.sleep(1)
