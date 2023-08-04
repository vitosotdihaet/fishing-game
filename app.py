from screen import Screen, ScreenType

from manage_scr import Scr, ActionKeys

import curses

import time


class App:
    def __init__(self, scr: Scr, screens: list[Screen]):
        self.scr = scr

        self.screens = screens
        self.active_screen_ind = 0

        self.active_screen = screens[self.active_screen_ind]

    def update(self):
        for s in self.screens:
            s.update()
        
        self.active_screen.draw()

        self.scr.update()

    def run(self):
        title = self.active_screen.screen_type.value
        self.scr.curses_scr.addstr(
            0, int((self.active_screen.cols - len(title))/2), # center title
            f' {title} ',
            curses.A_BOLD
        )

        while True:
            c = self.scr.curses_scr.getch()

            match c:
                case int(ActionKeys.EXIT):
                    break
                case int(ActionKeys.NEXT_SCREEN):
                    self.next_screen()
                    self.scr.curses_scr.erase()

                    self.scr.curses_scr.border(0)

                    title = self.active_screen.screen_type.value
                    self.scr.curses_scr.addstr(
                        0, int((self.active_screen.cols - len(title))/2), # center title
                        f' {title} ',
                        curses.A_BOLD
                    )

            self.update()
            time.sleep(0.1)

    def next_screen(self):
        self.active_screen_ind = (self.active_screen_ind + 1) % len(self.screens)
        self.active_screen = self.screens[self.active_screen_ind]

    def close(self):
        self.scr.close()