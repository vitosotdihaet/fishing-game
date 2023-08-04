import random

class vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'{self.x}, {self.y}'

    @staticmethod
    def random(mini: int = -1, maxi: int = 1):
        return vec2(random.randint(mini, maxi), random.randint(mini, maxi))
