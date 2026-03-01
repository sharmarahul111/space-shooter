from settings import *
from custom_timer import Timer
from sprites import Player, Laser


class Game():
	def __init__(self):
		init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
		set_target_fps(60)
		self.import_assets()
		self.lasers = []
		self.player = Player(self.assets["player"], Vector2(
			WINDOW_WIDTH/2, WINDOW_HEIGHT/2), self.shoot_laser)

	def import_assets(self):
		self.assets = {
			"player": load_texture(join("images", "spaceship.png")),
			"star": load_texture(join("images", "star.png")),
			"laser": load_texture(join("images", "laser.png"))
		}
		self.star_data = [
			(
				Vector2(randint(0, WINDOW_WIDTH),
						randint(0, WINDOW_HEIGHT)),  # pos
				uniform(.5, 1.6)  # size
			) for i in range(40)
		]

	def shoot_laser(self, pos):
		self.lasers.append(Laser(self.assets["laser"], pos))
	def draw_stars(self):
		for star in self.star_data:
			draw_texture_ex(self.assets["star"], star[0], 0, star[1], WHITE)

	def update(self):
		dt = get_frame_time()
		self.player.update(dt)
		for laser in self.lasers:
			laser.update(dt)

	def draw(self):
		begin_drawing()
		clear_background(BG_COLOR)
		self.draw_stars()
		self.player.draw()
		for laser in self.lasers:
			laser.draw()
		end_drawing()

	def run(self):
		while not window_should_close():
			self.update()
			self.draw()

		close_window()


if __name__ == "__main__":
	game = Game()
	game.run()
