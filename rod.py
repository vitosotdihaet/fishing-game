from fish import Fish

from curses import A_BOLD

import art.rods as rods

class Rod:
    def __init__(self, power: int, img: list[str]):
        self.power = power

        self.has_fish = False
        self.current_fish = None

        self.img = img

    def fish(self, fish: Fish):
        pass

    def addstr(self, scr, x: int = 1, debug=False):
        rows, _cols = scr.getmaxyx()

        y = (rows - len(self.img)) // 2

        if debug:
            scr.addstr(y, 1, f'{self.power}', A_BOLD)
            y += 1

        for i in range(len(self.img)):
            for j in range(len(self.img[i])):
                c = self.img[i][j]
                if c != ' ':
                    scr.addstr(y + i, x + j, c)
