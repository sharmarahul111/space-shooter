from settings import *

class Sprite():
	def __init__(self, texture, pos, speed, direction):
		self.pos = pos
		self.texture = texture
		self.speed = speed
		self.direction = direction
		self.size = Vector2(texture.width, texture.height)
	def move(self, dt):
		self.pos.x += self.direction.x * self.speed * dt
		self.pos.y += self.direction.y * self.speed * dt
	def update(self, dt):
		self.move(dt)
	def draw(self):
		draw_texture_v(self.texture, self.pos, WHITE)

class Player(Sprite):
	def __init__(self, texture, pos, shoot_laser):
		super().__init__(texture ,pos, PLAYER_SPEED, Vector2())
		self.shoot_laser = shoot_laser

	def input(self):
		self.direction.x = int(is_key_down(KEY_RIGHT))-int(is_key_down(KEY_LEFT))
		self.direction.y = int(is_key_down(KEY_DOWN))-int(is_key_down(KEY_UP))
		self.direction = vector2_normalize(self.direction)

		if is_key_pressed(KEY_SPACE):
			self.shoot_laser(Vector2(self.pos.x + self.size.x/2, self.pos.y-60))
	def constraint(self):
		self.pos.x = max(0, min(self.pos.x, WINDOW_WIDTH-self.size.x))
		self.pos.y = max(0, min(self.pos.y, WINDOW_HEIGHT-self.size.y))
	def update(self, dt):
		self.input()
		self.move(dt)
		self.constraint()

class Laser(Sprite):
	def __init__(self, texture, pos):
		super().__init__(texture, pos, LASER_SPEED, Vector2(0, -1))