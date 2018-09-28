import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from paddle import Paddle
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Sushi Pong')

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a single ship and groups of sushi_balls, user paddles and ai paddles.
    ship = Paddle(ai_settings, screen)
    user_paddles = Group()
    ai_paddles = Group()
    sushi_ball = Group()

    # Create the fleet of sushi.
    gf.create_fleet(ai_settings, screen, ship, sushi_ball)
    # Create the fleet of user paddles.
    gf.create_user_paddles(ai_settings, screen, user_paddles)
    # Create the fleet of ai paddles.
    gf.create_ai_paddles(ai_settings, screen, ai_paddles)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, sushi_ball)

        if stats.game_active:
            # Move the ship
            ship.update()
            # Check for collisions between sushi, screen edges and padles
            gf.update_aliens(ai_settings, screen, stats, sb, ship, sushi_ball)

        gf.update_screen(ai_settings, screen, stats, sb, ship, sushi_ball, play_button)

run_game()