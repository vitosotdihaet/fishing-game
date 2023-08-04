import curses

from enum import IntEnum


class ActionKeys(IntEnum):
    EXIT = ord('q')
    NEXT_SCREEN = ord('n')


class Scr:
    def __init__(self, curses_scr):
        self.curses_scr = curses_scr

        curses.noecho()
        curses.cbreak()
        self.curses_scr.keypad(1)
        self.curses_scr.nodelay(1)

        self.curses_scr.border(0)

    def close(self):
        self.curses_scr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def update(self):
        self.curses_scr.refresh()
