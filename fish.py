import curses
import random

import fish_parts
from colour import Color
from vec2 import vec2

from typing import List


MAX_X_SPEED = 4
MAX_Y_SPEED = 1

class Fish:
	def __init__(self, size: int, pos: vec2, color: Color, tail: List[str], lower_body: List[str], upper_body: List[int], head: List[int], speed=vec2(0, 0)):
		self.size = size
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

		self.is_alive = True;

	def update(self, scr):
		rows, cols = scr.getmaxyx()
		
		temp_pos = self.pos + self.speed

		if temp_pos.x + 9 >= cols or temp_pos.x <= 0: self.speed.x *= -1
		if temp_pos.y + 3 >= rows or temp_pos.y <= 0: self.speed.y *= -1

		self.prev_pos = self.pos
		self.pos += self.speed

	def addstr(self, scr, facing_right=True):
		x = self.pos.x
		y = self.pos.y

		off_x = 0
		fish_width = len(self.img)

		img = self.img

		if self.speed.x < 0:
			img = self.reversed_img

		for i in range(fish_width):
			for j in range(len(img[i])):
				scr.addstr(y + j, x + off_x, img[i][j], curses.A_NORMAL)
			off_x += len(img[i][0])

	def addstr_with_info(self, scr):
		x = self.pos.x
		y = self.pos.y

		scr.addstr(y, x, f'Size = {self.size}, Color = {self.color}', curses.A_NORMAL)
		self.addstr(scr)
	
	def remstr(self, scr):
		x = self.prev_pos.x
		y = self.prev_pos.y

		off_x = 0
		fish_width = len(self.img)

		for i in range(fish_width):
			for j in range(len(self.img[i])):
				for k in range(len(self.img[i][j])):
					scr.addstr(y + j, x + off_x + k, ' ', curses.A_NORMAL)
			off_x += len(self.img[i][0])

	def print(self, facing_right=True):
		fish_width = len(self.img)
		fish_height = len(self.img[0])

		img = self.img
		if not facing_right: img = self.reversed_img
		
		for i in range(fish_height):
			for j in range(fish_width):
				print(img[j][i], end='')
			print()


def random_fish(scr, count=1):
	fish = []

	for _ in range(count):
		size = random.random() * 100
		color = Color()
		color.set_rgb([random.random(), random.random(), random.random()])

		pos = vec2(random.randint(1, scr.getmaxyx()[1] - 9), random.randint(1, scr.getmaxyx()[0] - 4))
		speed = vec2(random.randint(0, MAX_X_SPEED), random.randint(0, MAX_Y_SPEED))

		fish_index = random.randint(0, len(fish_parts.TAILS) - 1)

		tail = fish_parts.TAILS[fish_index]
		lower_body = fish_parts.L_BODIES[fish_index]
		upper_body = fish_parts.U_BODIES[fish_index]
		head = fish_parts.HEADS[fish_index]

		fish.append(Fish(int(size), pos, color, tail, lower_body, upper_body, head, speed))

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

def reverse_fish(img: List[List[str]]):
	new_img = [[] for _ in range(len(img))]

	for i in range(len(img)):
		new_img[len(img) - 1 - i] = reverse_slice(img[i])

	return new_img

def reverse_slice(part: List[str]):
	new_part = ['' for _ in range(len(part))]

	for i in range(len(part)):
		for c in part[i][::-1]:
			if c in reverse_map:
				new_part[i] += reverse_map[c]
			else:
				new_part[i] += c

	return new_part


if __name__ == '__main__':
	new_fish = Fish(5, vec2(0, 0), Color('blue'), fish_parts.DEFAULT_TAIL, fish_parts.DEFAULT_LOWER_BODY, fish_parts.DEFAULT_UPPER_BODY, fish_parts.DEFAULT_HEAD)
	new_fish.print()
	new_fish.print(False)