from fish import Fish, random_fish
from fish_parts import DEFAULT_TAIL, DEFAULT_LOWER_BODY, DEFAULT_UPPER_BODY, DEFAULT_HEAD

import curses

import datetime
import time

import traceback

APP_NAME = 'Fishing game'
QUIT_SPLASH = 'Press q to close this screen'


try:
	# -- Initialize --
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.nodelay(1)

	FISH = random_fish(stdscr, 5)

	rows, cols = stdscr.getmaxyx()

	stdscr.border(0)
	stdscr.addstr(0, int((cols - len(APP_NAME))/2), f' {APP_NAME} ', curses.A_BOLD)
	stdscr.addstr(1, int((cols - len(QUIT_SPLASH))/2), QUIT_SPLASH, curses.A_NORMAL)
	
	while True:
		rows, cols = stdscr.getmaxyx()

		for f in FISH:
			f.update(stdscr)
			f.remstr(stdscr)

		for f in FISH:
			f.addstr(stdscr)

		stdscr.refresh()
		time.sleep(0.1)

		ch = stdscr.getch()
		if ch == ord('q'):
			break

except:
	stdscr.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()
	traceback.print_exc()
	exit(1)

stdscr.keypad(0)
curses.echo()
curses.nocbreak()
curses.endwin()
