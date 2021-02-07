import pygame


class Ship:
    """Класс для управления кораблем"""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ship_speed = 1.5

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/rocket_min.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра коробля
        self.x = float(self.rect.x)

        # Флаги перемещения коробля
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию коробля с учетом флага"""
        # Обновляет атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
