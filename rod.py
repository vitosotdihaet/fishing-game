from scr import Scr
from fish import Fish
from bobber import Bobber

from curses import A_BOLD

from custom_math.vec2 import vec2

import random

BOBBER_MOVE_CHANCE = 0.1


class Rod:
    def __init__(self, power: int, stick_img: list[str], bobber: Bobber = Bobber()):
        self.power = power

        self.has_fish = False
        self.current_fish = None

        self.stick_img = stick_img
        self.bobber = bobber

        self.thrown = False

    def throw(self):
        self.thrown = not self.thrown

    def fish(self, fish: Fish):
        pass

    def addstr(self, scr, x: int = 1, debug=False):
        rows, _cols = scr.getmaxyx()

        y = (rows - len(self.stick_img)) // 2

        if debug:
            scr.addstr(y, 1, f'{self.power}', A_BOLD)
            y += 1

        for i in range(len(self.stick_img)):
            for j in range(len(self.stick_img[i])):
                c = self.stick_img[i][j]
                if c != ' ':
                    scr.addstr(y + i, x + j, c)

        try:
            abs_bobber_x, abs_bobber_y = x + len(self.stick_img[0]) + self.bobber.pos.x, y + self.bobber.pos.y
            if self.thrown:
                draw_string(scr, vec2(x + len(self.stick_img[0]), y), vec2(abs_bobber_x, abs_bobber_y))
            scr.addstr(abs_bobber_y, abs_bobber_x, self.bobber.img)
        except:
            self.bobber.pos.zero()

    def update(self):
        if random.random() < BOBBER_MOVE_CHANCE:
            self.bobber.pos += self.bobber.speed
            self.bobber.speed *= -1


def draw_string(scr, pos1: vec2, pos2: vec2):
    width, height = pos2 - pos1
    x, y = pos1

    if width == 0:
        for i in range(min(0, height), max(0, height)):
            scr.addstr(y + i, x, '|')
        return

    if height == 0:
        for i in range(min(0, width), max(0, width)):
            scr.addstr(y - 1, x + i, '_')
        return

    if width < 0:
        return

    if height > 0:
        if width > height:
            j = 0
            for i in range(0, width):
                if i/width > j/height:
                    j += 1
                    scr.addstr(y + j - 1, x + i, '\\')
                else:
                    scr.addstr(y + j - 1, x + i, '_')

        if width <= height:
            i = 1
            for j in range(0, height):
                if i/width < j/height:
                    i += 1
                    scr.addstr(y + j, x + i - 1, '\\')
                else:
                    scr.addstr(y + j, x + i - 1, '|')
    else:
        if width > -height:
            j = 0
            for i in range(0, width):
                if i/width > -j/height:
                    j += 1
                    scr.addstr(y - j, x + i, '/')
                else:
                    scr.addstr(y - j - 1, x + i, '_')

        if width <= -height:
            i = 1
            for j in range(0, -height):
                if i/width < -j/height:
                    i += 1
                    scr.addstr(y - j, x + i - 1, '/')
                else:
                    scr.addstr(y - j, x + i - 1, '|')
