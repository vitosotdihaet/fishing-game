from scr import Scr
from fish import Fish
from bobber import Bobber

from curses import A_BOLD


class Rod:
    def __init__(self, power: int, stick_img: list[str], bobber: Bobber):
        self.power = power

        self.has_fish = False
        self.current_fish = None

        self.stick_img = stick_img
        self.bobber = bobber

        self.throw_iteration = 0

    # def throw(self, iter = 0):
    #     pass

    # def fish(self, fish: Fish):
    #     pass

    def addstr(self, scr, x: int = 1, debug = False):
        rows, _cols = scr.getmaxyx()

        y = (rows - len(self.stick_img)) // 2

        if debug:
            scr.addstr(y, 1, f'{self.power}', A_BOLD)
            y += 1

        maxy, maxx = y, x

        stick_img = self.stick_img
        if self.throw_iteration == 0:
            stick_img = self.stick_img[:-2]

        for i in range(len(self.stick_img)):
            for j in range(len(self.stick_img[i])):
                c = self.stick_img[i][j]
                if c != ' ':
                    scr.addstr(y + i, x + j, c)
                maxx = max(x + j, x)
            maxy = max(y + i, maxy)

        scr.addstr(self.bobber.pos.y, self.bobber.pos.x, self.bobber.img)