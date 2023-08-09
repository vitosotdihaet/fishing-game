from curses import A_BOLD

import random

import art.fishes as fishes
from colour import Color
from custom_math.vec2 import vec2


MAX_X_SPEED = 4
MAX_Y_SPEED = 1


class Fish:
    def __init__(self, size: int, pos: vec2, color: Color, tail: list[str], lower_body: list[str], upper_body: list[str], head: list[str], speed=vec2(0, 0)):
        self.size = size
        self.health = size
        self.color = color

        self.prev_pos = pos
        self.pos = pos
        self.speed = speed

        self.tail = tail
        self.lower_body = lower_body
        self.upper_body = upper_body
        self.head = head

        self.img = [tail, lower_body, upper_body, head]
        self.reversed_img = reverse_fish(self.img)

        self.is_alive = True

    @staticmethod
    def random(rows: int, cols: int):
        size = random.random() * 100
        color = Color()
        color.set_rgb([random.random(), random.random(), random.random()])

        pos = vec2(random.randint(1, cols - 10), random.randint(1, rows - 10))
        speed = vec2(random.randint(0, MAX_X_SPEED), random.randint(0, MAX_Y_SPEED))

        fish_index = random.randint(0, len(fishes.TAILS) - 1)

        tail = fishes.TAILS[fish_index]
        lower_body = fishes.L_BODIES[fish_index]
        upper_body = fishes.U_BODIES[fish_index]
        head = fishes.HEADS[fish_index]

        return Fish(int(size), pos, color, tail, lower_body, upper_body, head, speed)

    def update(self, scr, is_on_rod=False):
        rows, cols = scr.getmaxyx()

        if is_on_rod:
            temp_pos = self.pos + vec2.random()
        else:
            temp_pos = self.pos + self.speed

        if temp_pos.x + 9 >= cols or temp_pos.x <= 0:
            self.speed.x *= -1
        if temp_pos.y + 3 >= rows or temp_pos.y <= 0:
            self.speed.y *= -1

        self.prev_pos = self.pos
        self.pos += self.speed

    def addstr(self, scr, debug=False):
        rows, cols = scr.getmaxyx()

        x = self.pos.x
        y = self.pos.y

        if debug:
            scr.addstr(y, x, f'{self.size}: {self.color} with {self.speed} at {self.pos}', A_BOLD)
            x += 1
            y += 1

        off_x = 0
        fish_width = len(self.img)

        img = self.img

        if self.speed.x < 0:
            img = self.reversed_img

        for i in range(fish_width):
            for j in range(len(img[i])):
                if (y + j <= 0 or rows <= y + j) or (x + off_x <= 0 or cols <= x + off_x):
                    continue
                scr.addstr(y + j, x + off_x, img[i][j])
            off_x += len(img[i][0])

    def __str__(self):
        fish_width = len(self.img)
        fish_height = len(self.img[0])

        img = self.img
        # if not facing_right: img = self.reversed_img

        out = ''

        for i in range(fish_height):
            for j in range(fish_width):
                out += img[j][i]
            out += '\n'

        return out


def random_fish(rows: int, cols: int, count=1):
    fish = []

    for _ in range(count):
        fish.append(Fish.random(rows, cols))

    return fish


reverse_map = {
    '>': '<',
    '<': '>',
    ')': '(',
    '(': ')',
    ']': '[',
    '[': ']',
    '}': '{',
    '{': '}',
    '\\': '/',
    '/': '\\',
}


def reverse_fish(img: list[list[str]]):
    new_img = [[] for _ in range(len(img))]

    for i in range(len(img)):
        new_img[len(img) - 1 - i] = reverse_slice(img[i])

    return new_img


def reverse_slice(part: list[str]):
    new_part = ['' for _ in range(len(part))]

    for i in range(len(part)):
        for c in part[i][::-1]:
            if c in reverse_map:
                new_part[i] += reverse_map[c]
            else:
                new_part[i] += c

    return new_part


if __name__ == '__main__':
    new_fish = Fish(5, vec2(0, 0), Color('blue'), fishes.DEFAULT_TAIL,
                    fishes.DEFAULT_LOWER_BODY, fishes.DEFAULT_UPPER_BODY, fishes.DEFAULT_HEAD)
    print(new_fish)
