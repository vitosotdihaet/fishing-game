import curses
import traceback

from scr import Scr

STDSCR = None
rows, cols = 0, 0
try:
    STDSCR = Scr(curses.initscr())
    rows, cols = STDSCR.curses_scr.getmaxyx()
except:
    curses.endwin()
    traceback.print_exc()
    exit(1)


import art.rods
from rod import Rod
from bobber import Bobber

RODS = [
    Rod(1, art.rods.DEFAULT_STICK, Bobber())
]


from screen import Screen, ScreenType
from fish import random_fish

SCREENS = [
    Screen(ScreenType.FISHING, STDSCR, rows, cols, RODS[0], random_fish(rows, cols, 5)),
    Screen(ScreenType.BUCKET,  STDSCR, rows, cols, None,    random_fish(rows, cols, 1))
]


from app import App

if __name__ == '__main__':
    app = App(STDSCR, SCREENS, RODS)
    app.run()
