class Settings():
    """A class to store all settings for Sushi Pong"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Paddle settings
        self.user_paddle_speed_factor = 1.5
        self.ai_paddle_speed_factor = .8
        self.ship_limit = 3

        # Sushi settings
        self.sushi_speed_factor = 1
        self.sushi_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.001
        # How quickly the alien point value increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.user_paddle_speed_factor = 1.5
        self.ai_paddle_speed_factor = .8
        self.sushi_speed_factor = .5

        # fleet direction of 1  represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.user_paddle_speed_factor *= self.speedup_scale
        self.ai_paddle_speed_factor *= self.speedup_scale
        self.sushi_speed_factor *= self.speedup_scale
