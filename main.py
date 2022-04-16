from pyautogui import *
import pyautogui
import time
import keyboard
import random
from windowcapture import WindowCapture
import cv2 as cv
from mousemovment import moveMouse
from banking import RunescapeBot

time.sleep(2)

wincap = WindowCapture('Runelite - Irenee3')
NormalX = 0
NormalY = 0

minY = 9999
minX = 9999
maxX = -9999
maxY = -9999

purple = False
pink = False
velvet = False

banked = True
goingToBank = False
goingToMine = True
click = False
mining_state = False
mining_search = True
full_inv = False
repeat = True
random_repeat = 0.0

count = 0.0

# Color of center: (255, 219, 195)
bot = RunescapeBot()

# width, height = pic.size
width = wincap.getW()
height = wincap.getH()

cordX = [0]
cordY = [0]

while keyboard.is_pressed('q') == False:
    # time.sleep(random.uniform(5.5, 8.5))
    minY = 9999
    minX = 9999
    maxY = -9999
    maxX = -9999
    click = False

    pic = wincap.get_screenshot()
    move = bot.stoppedmoving()

    if move:
        if goingToBank:
            mouse_cord = bot.find_bank(pic)

    # print("Not there")qining_search = False
            mining_state = False
            for x in range(0, width, 1):
                for y in range(0, height, 1):

                    rgb = pic[y, x]

                    if rgb[0] == 31 and rgb[1] == 77 and rgb[2] == 132:
                        velvet = False
                        pink = False
                        purple = False
                        NormalY = y
                        NormalX = x
                        print('banking')
                        click = True
                        banked = False
                        break
                    elif len(mouse_cord) > 0:
                        rsr = random.randint(0, len(mouse_cord) - 1)
                        NormalX = mouse_cord[rsr][0]
                        NormalY = mouse_cord[rsr][1]
                        click = True
                        print('found bank')
                        break
                    elif rgb[0] == 30 and rgb[1] == 0 and rgb[2] == 77:
                        pink = False
                        purple = False
                        if maxY < y:
                            maxY = y
                            NormalY = maxY
                            NormalX = x
                            print('found velvet')
                            click = True
                        break
                    elif rgb[0] == 136 and rgb[1] == 68 and rgb[2] == 247:
                        purple = False
                        if minX > x and pink:
                            minX = x
                            NormalX = minX
                            NormalY = y
                            print('found pink to')
                            click = True
                        break
                    elif rgb[0] == 189 and rgb[1] == 0 and rgb[2] == 218:
                        if minY > y and purple:
                            minY = y
                            NormalY = minY
                            NormalX = x
                            print('found purplez')
                            click = True
                        break

    if goingToMine:
        if move:
            for x in range(0, width, 1):
                for y in range(0, height, 1):

                    rgb = pic[y, x]

                    if not banked:
                        time.sleep(random.uniform(0.5, 1.5))
                        pyautogui.keyDown("esc")
                        pyautogui.keyUp("esc")
                        banked = True
                        #print("banking")
                        click = False
                    elif rgb[0] == 189 and rgb[1] == 0 and rgb[2] == 218:
                        if maxY < y:
                            maxY = y
                            NormalY = maxY
                            NormalX = x
                            print('found purple')
                            pink = True
                            click = True
                        break
                    elif rgb[0] == 136 and rgb[1] == 68 and rgb[2] == 247:
                        if maxX < x and not pink:
                            maxX = x
                            NormalX = maxX
                            NormalY = y
                            print('found pink')
                            click = True
                            mining_search = True
                        break

    if mining_search:
        for x in range(0, width, 1):
            for y in range(0, height, 1):
                rgb = pic[y, x]

                if rgb[0] == 17 and rgb[1] == 25 and rgb[2] == 51:
                    NormalY = y
                    NormalX = x
                    cordX.append(NormalX)
                    cordY.append(NormalY)
                    goingToBank = False
                    goingToMine = False
                    click = True

        if len(cordY) > 1:
            rand = random.randint(0, len(cordY) - 1)
            NormalY = cordY[rand]
            NormalX = cordX[rand]
            mining_state = True
            mining_search = False
            repeat = True
            count = 0.0

    moveMouse(NormalX + wincap.getX(), NormalY + wincap.getY())

    pic = wincap.get_screenshot()
    time.sleep(0.1)
    # if mining_state:
    #     if bot.confirm_tooltip(pic):
    #         click = True
    #     else:
    #         repeat = False
    #         mining_state = False
    #         mining_search = True
    #         click = False
    #         #print("Not there")

    move = bot.stoppedmoving()
    if click:
        pyautogui.click()
        move = False
        time.sleep(0.1)
        moveMouse(random.randint(500, 1080), random.randint(500, 1080))

    prevOres = bot.count_ores(pic)

    random_repeat = random.uniform(5.5, 8.5)
    while repeat and mining_state:
        pic = wincap.get_screenshot()
        currentOres = bot.count_ores(pic)
       # print(count, " - ", random_repeat)
        mining_search = False

        if currentOres > prevOres:
            repeat = False
            mining_state = False

        time.sleep(0.5)
        count += 0.5

        if count > random_repeat:
            repeat = False
            mining_state = False

        pic = wincap.get_screenshot()

        if bot.full(pic):
            mining_search = False
            mining_state = False
            goingToBank = True
            velvet = True
            purple = True
            pink = True
            banked = True
        else:
            mining_search = True

    pic = wincap.get_screenshot()

    cordY.clear()
    cordX.clear()

    if not pink and not velvet and not purple and not banked:
        goingToBank = False
        goingToMine = True


