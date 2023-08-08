from custom_math.vec2 import vec2 

from art.rods import DEFAULT_BOBBER

class Bobber:
    def __init__(self, img: str = DEFAULT_BOBBER, pos: vec2 = vec2.empty()): # img is a char
        self.img = img
        self.pos = pos
    
    @staticmethod
    def default():
        return Bobber()