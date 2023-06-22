import time
import pyautogui
from seleniumbase import SB

with SB(headed=True) as driver:
    driver.open('https://key-test.ru/')
    # driver.maximize_window()
    # driver.click('div.menu-item')
    # time.sleep(2)

    pyautogui.keyDown('altleft')
    pyautogui.keyDown('s')
    pyautogui.keyDown('1')
    time.sleep(0.5)
    pyautogui.keyUp('1')
    pyautogui.keyUp('s')
    pyautogui.keyUp('altleft')

    time.sleep(5)
