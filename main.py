from screen import Screen, ScreenType

from fish import random_fish

from manage_scr import Scr, curses

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


SCREENS = [
    Screen(ScreenType.FISHING, STDSCR, rows, cols, random_fish(rows, cols, 5)),
    Screen(ScreenType.BUCKET, STDSCR, rows, cols, random_fish(rows, cols, 1))
]

if __name__ == '__main__':
    app = App(STDSCR, SCREENS)
    app.run()