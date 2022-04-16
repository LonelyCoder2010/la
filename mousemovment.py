import random
import subprocess as sp
import pyautogui
from pyclick import HumanClicker


def moveMouse(x, y):
    hc = HumanClicker()
    time_gap = random.uniform(0.4, 0.8)
    hc.move((x, y), time_gap)

