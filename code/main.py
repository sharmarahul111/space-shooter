from settings import *
from custom_timer import Timer
from sprites import Player
class Game():
	def __init__(self):
		init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
		self.import_assets()

		self.player = Player(self.assets["player"], Vector2(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

	def import_assets(self):
		self.assets = {
			"player": load_texture(join("images", "spaceship.png"))
		}

	def run(self):
		while not window_should_close():
			dt = get_frame_time()
			self.player.update(dt)
			begin_drawing()
			clear_background(BG_COLOR)
			self.player.draw()
			end_drawing()
		close_window()

if __name__ == "__main__":
	game = Game()
	game.run()