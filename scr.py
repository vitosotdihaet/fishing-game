import curses

from enum import IntEnum


class ActionKeys(IntEnum):
    EXIT = ord('q')
    NEXT_SCREEN = ord('n')

    THROW_A_ROD = ord(' ')

    #! Arrow keys
    LEFT = 260
    RIGHT = 261
    UP = 259
    DOWN = 258


class Scr:
    def __init__(self, curses_scr, cursor_is_visible=False):
        self.curses_scr = curses_scr

        curses.noecho()
        curses.cbreak()
        self.curses_scr.keypad(1)
        self.curses_scr.nodelay(1)

        if not cursor_is_visible:
            curses.curs_set(0)

    def close(self):
        self.curses_scr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def update(self):
        self.curses_scr.refresh()

    def clear(self, border=True):
        self.curses_scr.clear()
        if border:
            self.curses_scr.border(0)


if __name__ == '__main__':
    import time

    try:
        STDSCR = Scr(curses.initscr())
        rows, cols = STDSCR.curses_scr.getmaxyx()
        pos = [0, 0]

        while True:
            STDSCR.clear(border=False)

            c = STDSCR.curses_scr.getch()
            m = curses.getmouse()
            s = curses.getsyx()

            STDSCR.curses_scr.addstr(0, 0, f'char: {c}')
            STDSCR.curses_scr.addstr(1, 0, f'mouse: {m}')
            STDSCR.curses_scr.addstr(2, 0, f'syx: {s}')

            match c:
                case int(ActionKeys.EXIT):
                    break
                case int(ActionKeys.RIGHT):
                    pos[0] += 1

            STDSCR.curses_scr.addstr(3, 0, f'pos: {pos}')

            STDSCR.curses_scr.move(pos[1], pos[0])

            curses.flushinp()
            STDSCR.update()
            time.sleep(0.1)

    except:
        curses.endwin()
        exit(1)
