class Settings:
    """Each time we introduce new functionality into the game, we’ll typically
create some new settings as well. Instead of adding settings throughout
the code, let’s write a module called settings that contains a class called
Settings to store all these values in one place. This approach allows us to
work with just one settings object any time we need to access an individual
setting. This also makes it easier to modify the game’s appearance and
behavior as our project grows: to modify the game, we’ll simply change
some values in settings.py, which we’ll create next, instead of searching for
different settings throughout the project."""
    """A class to store all settings for alien invasion."""
    def __init__(self):
        """Initialize the games settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_speed = 1.5

        # Bullet setting
        self.bullet_speed = 1.0
        self.width = 3
        self.height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
