from screen import Screen, ScreenType
from rod import Rod

import art.rods

from fish import random_fish

from scr import Scr, curses

import traceback

from app import App


APP_NAME = 'Fishing game'
QUIT_SPLASH = 'Press q to close this screen'


STDSCR = None
rows, cols = 0, 0
try:
    STDSCR = Scr(curses.initscr())
    rows, cols = STDSCR.curses_scr.getmaxyx()
except:
    curses.endwin()
    traceback.print_exc()
    exit(1)


RODS = [
    Rod(1, art.rods.DEFAULT)
]

SCREENS = [
    Screen(ScreenType.FISHING, STDSCR, rows, cols, RODS[0], random_fish(rows, cols, 5)),
    Screen(ScreenType.BUCKET, STDSCR, rows, cols, RODS[0], random_fish(rows, cols, 1))
]

if __name__ == '__main__':
    app = App(STDSCR, SCREENS, RODS)
    app.run()