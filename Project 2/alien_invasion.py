import sys  # System-specific parameters and functions.
"""We’ll use tools in the sys module to exit the game when the player quits."""

import pygame  # The pygame module contains the functionality we need to make a game.

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Aline


class AlineInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()
        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starts the main loop for the game."""

        while True:

            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            # Redraw the screen during each pass through the loop.

    # def _update_bulltets(self):
    #     """Update position of bullets and get rid of old bullets."""
    #     # Get rid of bullets that have disappeared.
    #     for bullet in self.bullets.copy():
    #         if bullet.rect.bottom <= 0:
    #             self.bullets.remove(bullet)
    #     print(len(self.bullets))

    def _check_events(self):
        # Respond to key presses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key-presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to release."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # When the moving_right flag is False, the ship will be motionless.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        #   if len(self.bullets) < self.settings.bullet_allowed:
        new_bullet = Bullet(self)
        # The add() method is similar to append(), but it’s a method that’s written specifically for Pygame groups.
        self.bullets.add(new_bullet)

    def _creat_fleet(self):
        """Create the fleet of aliens."""
        # Make the alien.
        alien = Aline(self)
        self.aliens.add(alien)

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # The bullets.sprites() method returns a list of all sprites in the group bullets.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlineInvasion()
    ai.run_game()
