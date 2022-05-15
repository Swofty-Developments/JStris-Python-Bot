#!/usr/bin/python
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from field import Field
from optimizer import Optimizer
from tetromino import Tetromino
import keyboard
import threading
import pyautogui
import PIL.ImageGrab
from twisted.internet import task, reactor
import time
from collections import Counter

import pyautogui
import time

global field
global driver

pieces = {
    (15, 155, 216): "i",
    (89, 178, 2): "s",
    (215, 14, 56): "z",
    (227, 158, 2): "o",
    (227, 91, 3): "j",
    (175, 41, 138): "t",
    (33, 66, 199): "l",
}

def gameplayLoop():
    image = ImageGrab.grab()
    # checks which colour a specific spot of your screen has, by coordinates
    color = image.getpixel((700, 270))
    print(color)
    key = ""

    if not color == (0, 0, 0):

        if color == (15, 155, 216):
            key = "i"

        if color == (89, 178, 2):
            key = "s"

        if color == (215, 14, 56):
            key = "z"

        if color == (227, 158, 2):
            key = "o"

        if color == (227, 91, 3):
            key = "j"

        if color == (175, 41, 138):
            key = "t"

        if color == (33, 66, 199):
            key = "l"

        tetromino = Tetromino.create(key)
        opt = Optimizer.get_optimal_drop(field, tetromino)
        rotation = opt['tetromino_rotation']
        column = opt['tetromino_column']
        tetromino.rotate(rotation)
        field.drop(tetromino, column)
        print(field)
        newMove(rotation, column)
        '''thread = threading.Thread(target=newMove, args=(keys, column))
        thread.start()'''

    #time.sleep(0.01)
    gameplayLoop()

def newMove(rotation, column):
    global driver
    pog = ""

    if rotation == 1:
        pog += "w"
    elif rotation == 2:
        pog += "ww"
    elif rotation == 3:
        pog += "h"

    pog += "aaaaa"
    pog += "d" * column

    '''if "left" in keys:
        count = Counter(keys)['left']
        print(count)

        pog += "a" * count


    if "right" in keys:
        count = Counter(keys)['right']
        print(count)

        pog += "d" * count'''

    pog += "s"

    actions = ActionChains(driver)
    actions.send_keys(pog)
    actions.perform()
    pass

def start():
    gameplayLoop()


def stop():
    global field

    keyboard.send("left", True, False)

    field = Field()
    pass


if __name__ == '__main__':
    global timer
    global driver
    field = Field()
    tetromino = None

    keyboard.add_hotkey("z", start)
    keyboard.add_hotkey("x", stop)

    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://jstris.jezevec10.com/?play=1&mode=2")
    driver.maximize_window()

    driver.find_element_by_id("settings").click()

    time.sleep(0.1)

    input1 = driver.find_element_by_xpath("//input[@id='input1']")
    input1.click()
    input1.send_keys("a")

    input2 = driver.find_element_by_xpath("//input[@id='input2']")
    input2.click()
    input2.send_keys("d")

    input4 = driver.find_element_by_xpath("//input[@id='input4']")
    input4.click()
    input4.send_keys("s")

    input5 = driver.find_element_by_xpath("//input[@id='input5']")
    input5.click()
    input5.send_keys("h")

    input6 = driver.find_element_by_xpath("//input[@id='input6']")
    input6.click()
    input6.send_keys("w")

    input7 = driver.find_element_by_xpath("//input[@id='input8']")
    input7.click()
    input7.send_keys("p")

    input7 = driver.find_element_by_xpath("//a[@data-target='tab_skin']")
    input7.click()

    input7 = driver.find_element_by_xpath("//input[@id='bs12']")
    input7.click()

    driver.find_element_by_id("settingsSave").click()

    while True:
        pass
