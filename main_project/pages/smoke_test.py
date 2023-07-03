import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from seleniumbase import SB

with SB(headed=True) as driver:
    driver.open('http://localhost:5173/#/sensors?pageIndex=undefined/')

    action_chains = ActionChains(driver.driver)
    action_chains.key_down(Keys.ALT)
    action_chains.send_keys('s')
    action_chains.send_keys('2')
    action_chains.key_up(Keys.ALT)
    action_chains.perform()

    time.sleep(5)
