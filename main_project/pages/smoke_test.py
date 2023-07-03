import time
import pyautogui
from seleniumbase import SB

with SB(headed=True) as driver:
    driver.open('http://localhost:5173/#/sensors?pageIndex=undefined/')
    # driver.maximize_window()
    # driver.click('div.menu-item')
    # time.sleep(2)
    time.sleep(1)
    pyautogui.keyDown('alt')
    time.sleep(0.5)
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyDown('1')
    time.sleep(2)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('s')
    pyautogui.keyUp('1')

    time.sleep(5)

