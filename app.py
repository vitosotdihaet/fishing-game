from screen import Screen
from rod import Rod

from scr import Scr, ActionKeys

import curses

import time


class App:
    def __init__(self, scr: Scr, screens: list[Screen], rods: list[Rod]):
        self.scr = scr

        self.screens = screens
        self.active_screen_ind = 0

        self.active_screen = screens[self.active_screen_ind]

        self.rods = rods
        self.active_rod_ind = 0

        self.active_rod = rods[self.active_rod_ind]


    def run(self):
        title = self.active_screen.screen_type.value
        self.scr.curses_scr.addstr(
            0, int((self.active_screen.cols - len(title))/2), # center title
            f' {title} ',
            curses.A_BOLD
        )

        throwing = False

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
                        0, int((self.active_screen.cols - len(title))/2),
                        f' {title} ',
                        curses.A_BOLD
                    )
                case int(ActionKeys.THROW_A_ROD):
                    if self.active_screen.rod != None:
                        throwing = True
                        self.active_screen.rod.throw_iteration += 1

            if not throwing and self.active_screen.rod != None:
                self.active_screen.rod.throw_iteration = 0
            throwing = False

            self.update()
            time.sleep(0.1)

    def update(self):
        for s in self.screens:
            s.update()

        self.active_screen.draw()
        self.scr.update()

    def next_screen(self):
        self.active_screen_ind = (self.active_screen_ind + 1) % len(self.screens)
        self.active_screen = self.screens[self.active_screen_ind]

    def close(self):
        self.scr.close()