from enum import Enum

from manage_scr import Scr

from fish import Fish


class ScreenType(Enum):
    DEFAULT = 'Hmmmm...'

    FISHING = 'It\'s time to fish!'
    BUCKET = 'Your bucket'


# A state of the game on concrete screen with all the info
class Screen:
    def __init__(self, screen_type: ScreenType, scr: Scr, rows: int, cols: int, fish: list[Fish] = []):
        self.screen_type = screen_type
        self.scr = scr

        self.cols = cols
        self.rows = rows

        self.fish = fish

    def update(self):
        match self.screen_type: # handle fish behavior
            case ScreenType.FISHING:
                for f in self.fish:
                    f.update(self.scr.curses_scr)
            case ScreenType.BUCKET:
                for f in self.fish:
                    f.update(self.scr.curses_scr)

    def draw(self):
        for f in self.fish:
            f.remstr(self.scr.curses_scr)

        for f in self.fish:
            f.addstr(self.scr.curses_scr)