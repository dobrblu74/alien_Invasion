class Settings:
    """Класс для хранения всех настроек игры Alien Invision"""

    def __init__(self):
        """Инициализируем настройки игры"""
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # self.bg_color = (51, 153, 255)

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
