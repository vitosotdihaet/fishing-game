from custom_math.vec2 import vec2

from art.rods import DEFAULT_BOBBER

DEFAULT_SPEED = vec2(0, 1)


class Bobber:
    def __init__(self, img: str = DEFAULT_BOBBER, pos: vec2 = vec2(), speed: vec2 = DEFAULT_SPEED):  # img is a char
        self.img = img
        self.pos = pos
        self.speed = speed
