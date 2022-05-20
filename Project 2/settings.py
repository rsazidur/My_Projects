class Settings:
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
