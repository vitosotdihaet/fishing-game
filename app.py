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

    def run(self, debug=False):
        rows, cols = self.scr.curses_scr.getmaxyx()

        while True:
            c = self.scr.curses_scr.getch()

            match c:
                case int(ActionKeys.EXIT):
                    break
                case int(ActionKeys.NEXT_SCREEN):
                    self.next_screen()
                case int(ActionKeys.THROW_A_ROD):
                    self.active_rod.throw()
            
            # Moving bobber
            if not self.active_rod.thrown:
                match c:
                    case int(ActionKeys.LEFT):
                        self.active_rod.bobber.pos.x -= 1
                    case int(ActionKeys.RIGHT):
                        self.active_rod.bobber.pos.x += 1
                    case int(ActionKeys.UP):
                        self.active_rod.bobber.pos.y -= 1
                    case int(ActionKeys.DOWN):
                        self.active_rod.bobber.pos.y += 1
            else:
                self.active_rod.update()

            curses.flushinp()
            self.update(debug=debug)
            time.sleep(0.1)

        self.close()

    def update(self, debug=False):
        for s in self.screens:
            s.update()

        self.scr.clear()
        self.active_screen.draw(debug=debug)
        self.scr.update()

    def next_screen(self):
        self.active_screen_ind = (self.active_screen_ind + 1) % len(self.screens)
        self.active_screen = self.screens[self.active_screen_ind]

    def close(self):
        self.scr.close()
