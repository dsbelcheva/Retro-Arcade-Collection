import pygame


class TrafficLight:
    def __init__(self):
        self.images = {
            'RED': pygame.image.load('../images/red.png'),
            'YELLOW': pygame.image.load('../images/yellow.png'),
            'GREEN': pygame.image.load('../images/green.png')
        }
        self.current_color = 'RED'
        self.image = self.images[self.current_color]
        self.rect = self.image.get_rect(center=(370, 150))
        self.change_time = pygame.time.get_ticks()
        self.active = False

    def start(self):
        if not self.active:
            self.active = True
            self.change_time = pygame.time.get_ticks()

    def update(self):
        if not self.active:
            return
        now = pygame.time.get_ticks()
        if self.current_color == 'RED' and now - self.change_time > 1500:
            self.current_color = 'YELLOW'
            self.change_time = now
        elif self.current_color == 'YELLOW' and now - self.change_time > 1500:
            self.current_color = 'GREEN'
            self.change_time = now
        elif self.current_color == 'GREEN' and now - self.change_time > 1500:
            self.current_color = 'RED'
            self.change_time = now

        self.image = self.images[self.current_color]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
