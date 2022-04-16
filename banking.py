from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from windowcapture import WindowCapture
import cv2 as cv
import numpy as np
import os


class RunescapeBot:
    MOVEMENT_STOPPED_THRESHOLD = 0.975

    def stoppedmoving(self):
        wincap = WindowCapture('Runelite - Irenee3')

        pic = wincap.get_screenshot()
        time.sleep(0.5)
        pic2 = wincap.get_screenshot()
        result = cv.matchTemplate(pic, pic2, cv.TM_CCOEFF_NORMED)
        similarity = result[0][0]
        if similarity >= self.MOVEMENT_STOPPED_THRESHOLD:
            # pictures look similar, so we've probably stopped moving
            print("stopped")
            return True
        else:
            print("moving")
            return False

    def count_ores(self, pic):
        needle_img = cv.imread('Resources/Mining/ores.png', cv.IMREAD_UNCHANGED)

        result = cv.matchTemplate(pic, needle_img, cv.TM_SQDIFF_NORMED)

        threshold = 0.10
        # The np.where() return value will look like this:
        # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
        locations = np.where(result <= threshold)
        # We can zip those up into a list of (x, y) position tuples
        locations = list(zip(*locations[::-1]))

        return len(locations)

    def find_bank(self, pic):
        needle_img = cv.imread('Resources/Mining/bank.png', cv.IMREAD_UNCHANGED)

        result = cv.matchTemplate(pic, needle_img, cv.TM_SQDIFF_NORMED)

        threshold = 0.10
        # The np.where() return value will look like this:
        # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
        locations = np.where(result <= threshold)
        # We can zip those up into a list of (x, y) position tuples
        locations = list(zip(*locations[::-1]))

        return locations

    def full(self, pic):
        needle_img = cv.imread('Resources/Mining/fullInv.png', cv.IMREAD_UNCHANGED)

        result = cv.matchTemplate(pic, needle_img, cv.TM_SQDIFF_NORMED)

        threshold = 0.01
        # The np.where() return value will look like this:
        # (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
        locations = np.where(result <= threshold)
        # We can zip those up into a list of (x, y) position tuples
        locations = list(zip(*locations[::-1]))

        if len(locations) == 1:
            return True
        else:
            return False

    def confirm_tooltip(self, pic):
        limestone_tooltip = cv.imread('Resources/Mining/toolTip.png')
        TOOLTIP_MATCH_THRESHOLD = 0.72

        # check the current screenshot for the limestone tooltip using match template
        result = cv.matchTemplate(pic, limestone_tooltip, cv.TM_CCOEFF_NORMED)
        # get the best match postition
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # if we can closely match the tooltip image, consider the object found
        if max_val >= TOOLTIP_MATCH_THRESHOLD:
            # print('Tooltip found in image at {}'.format(max_loc))
            # screen_loc = self.get_screen_position(max_loc)
            # print('Found on screen at {}'.format(screen_loc))
            # mouse_position = pyautogui.position()
            # print('Mouse on screen at {}'.format(mouse_position))
            # offset = (mouse_position[0] - screen_loc[0], mouse_position[1] - screen_loc[1])
            # print('Offset calculated as x: {} y: {}'.format(offset[0], offset[1]))
            # the offset I always got was Offset calculated as x: -22 y: -29
            return True
        #print('Tooltip not found.')
        return False

    def confirm_tooltip_bank(self, pic):
        limestone_tooltip = cv.imread('Resources/Mining/toolTipBank.png')
        TOOLTIP_MATCH_THRESHOLD = 0.72

        # check the current screenshot for the limestone tooltip using match template
        result = cv.matchTemplate(pic, limestone_tooltip, cv.TM_CCOEFF_NORMED)
        # get the best match postition
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # if we can closely match the tooltip image, consider the object found
        if max_val >= TOOLTIP_MATCH_THRESHOLD:
            # print('Tooltip found in image at {}'.format(max_loc))
            # screen_loc = self.get_screen_position(max_loc)
            # print('Found on screen at {}'.format(screen_loc))
            # mouse_position = pyautogui.position()
            # print('Mouse on screen at {}'.format(mouse_position))
            # offset = (mouse_position[0] - screen_loc[0], mouse_position[1] - screen_loc[1])
            # print('Offset calculated as x: {} y: {}'.format(offset[0], offset[1]))
            # the offset I always got was Offset calculated as x: -22 y: -29
            return True
        #print('Tooltip not found.')
        return False