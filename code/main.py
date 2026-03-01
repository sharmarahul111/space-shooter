from settings import *
from custom_timer import Timer
from sprites import Player, Laser, Meteor, ExplosionAnimation


class Game():
	def __init__(self):
		init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space Shooter")
		set_target_fps(60)
		self.import_assets()
		self.lasers, self.meteors, self.explosions = [], [], []
		self.meteor_timer = Timer(METEOR_TIMER_DURATION, True, True, self.create_meteor)
		self.player = Player(self.assets["player"], Vector2(
			WINDOW_WIDTH/2, WINDOW_HEIGHT/2), self.shoot_laser)

	def import_assets(self):
		self.assets = {
			"player": load_texture(join("images", "spaceship.png")),
			"star": load_texture(join("images", "star.png")),
			"laser": load_texture(join("images", "laser.png")),
			"meteor": load_texture(join("images", "meteor.png")),
			"explosion": [load_texture(join("images", "explosion", f"{i}.png")) for i in range(1, 29)],
			"font": load_font_ex(join("font", "Stormfaze.otf"), FONT_SIZE, ffi.NULL, 0)
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
	def discard_sprites(self):
		self.lasers = [laser for laser in self.lasers if not laser.discard]
		self.meteors = [meteor for meteor in self.meteors if not meteor.discard]
		self.explosions = [explosion for explosion in self.explosions if not explosion.discard]
	def draw_score(self):
		score = int(get_time())
		text = measure_text_ex(self.assets["font"], str(score), FONT_SIZE, 0)
		draw_text_ex(self.assets["font"], str(score), Vector2(WINDOW_WIDTH/2 - text.x/2, 100), FONT_SIZE, 0, WHITE)
		pass
	def create_meteor(self):
		self.meteors.append(Meteor(self.assets["meteor"]))
	def check_collision(self):
		#laser and meteor
		for laser in self.lasers:
			for meteor in self.meteors:
				if check_collision_circle_rec(
					meteor.get_center(),
					meteor.collision_radius,
					laser.get_rect()
				):
					laser.discard, meteor.discard = True, True
					pos = Vector2(laser.pos.x-laser.size.x/2, laser.pos.y)
					self.explosions.append(ExplosionAnimation(pos, self.assets["explosion"]))
		#player and meteor
		for meteor in self.meteors:
			if check_collision_circles(
				self.player.get_center(),
				self.player.collision_radius,
				meteor.get_center(), meteor.collision_radius
			):
				pass
				# close_window()
	def update(self):
		dt = get_frame_time()
		self.meteor_timer.update()
		self.player.update(dt)
		self.discard_sprites()
		for sprite in self.lasers + self.meteors + self.explosions:
			sprite.update(dt)
		self.check_collision()
	def draw(self):
		begin_drawing()
		clear_background(BG_COLOR)
		self.draw_stars()
		self.draw_score()
		self.player.draw()
		for sprite in self.lasers + self.meteors + self.explosions:
			sprite.draw()
		end_drawing()
	def run(self):
		while not window_should_close():
			self.update()
			self.draw()

		close_window()


if __name__ == "__main__":
	game = Game()
	game.run()
