from settings import *

class Sprite():
	def __init__(self, texture, pos, direction):
		self.pos = pos
		self.texture = texture
		self.direction = direction
	def update(self):
		pass
	def draw(self):
		draw_texture_v(self.texture, self.pos, WHITE)

class Player(Sprite):
	def __init__(self, texture, pos):
		super().__init__(pos, texture, PLAYER_SPEED, Vector2())

