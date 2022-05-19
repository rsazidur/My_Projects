import sys  # We’ll use tools in the sys module to exit the game when the player quits.

import pygame  # The pygame module contains the functionality we need to make a game.

from settings import Settings
from ship import Ship


class AlineInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # surface

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # Redraw the screen during each pass through the loop.

    def _check_events(self):
        # Respond to key presses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlineInvasion()
    ai.run_game()
