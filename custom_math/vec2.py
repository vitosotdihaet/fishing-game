import random


class vec2:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __mult__(self, num: int):
        return vec2(self.x * num, self.y * num)

    def __rmult__(self, num: int):
        return self.__mult__(num)

    def __imul__(self, num: int):
        self.x *= num
        self.y *= num
        return self

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __iter__(self):
        yield self.x
        yield self.y

    @staticmethod
    def random(mini: int = -1, maxi: int = 1):
        return vec2(random.randint(mini, maxi), random.randint(mini, maxi))

    def zero(self):
        self.x, self.y = 0, 0
