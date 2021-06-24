import pygame
import sys
from random import randint

import snake_window

class Game(snake_window.SnakeWindow):
    def __init__(self, width, height, title, background_color, FPS) -> None:
        super().__init__(width, height, title, background_color, FPS)

        self.cell_size = 16
        self.is_run = False
        self.score = 0

        self.help_text_position = self.set_text(
                'Press \'Space\'',
                'verdana', 32, (202, 76, 38),
                60, bold=True
            ) 
        pygame.draw.rect(
            self.screen,
            (18, 18, 20),
            (self.screen_centerx - 95, 100, 190, 70),
            border_radius=5
        )
        self.score_count_position = self.set_text(
                '0',
                'verdana', 32, (202, 76, 38),
                135, bold=True
            )
        
        self.make_field(320, 400)
        self.update_field((22, 22, 24), 7)
        self.screen.blit(self.field_surface, self.field_surface_position)

        self.snake = Snake(100, 100, 0, self.cell_size, 3, (62, 194, 90), (47, 158, 71))
        self.apple = Apple(self.field_surface, self.cell_size, (202, 76, 38))

        self.loop()

    def restart(self):
        self.score = 0
        self.snake = Snake(100, 100, 0, self.cell_size, 3, (62, 194, 90), (47, 158, 71))

    def collision_with_border(self):
        surface_width = self.field_surface.get_width()
        surface_height = self.field_surface.get_height()

        if self.snake.x <= 0:
            self.snake.x = surface_width - self.cell_size
        elif self.snake.x >= surface_width:
            self.snake.x = 0

        if self.snake.y <= 0:
            self.snake.y = surface_height - self.cell_size
        elif self.snake.y >= surface_height:
            self.snake.y = 0


    def loop(self):
        while True:
            if self.is_run:
                self.collision_with_border()
                self.update_field((22, 22, 24), 7)
                self.apple.draw()
                self.snake.draw(self.field_surface, self.apple)
                self.screen.blit(self.field_surface, self.field_surface_position)
                self.field_surface.fill(self.background_color)

                if self.snake.collision_with_self:
                    self.restart()
                    continue
                
                if not self.apple.is_exists:
                    self.score += 1
                    print(self.score)

            for event in pygame.event.get():
                if event.type == pygame.constants.QUIT:
                    sys.exit()
                if event.type == pygame.constants.KEYDOWN:
                    if event.key == pygame.constants.K_SPACE:
                        self.is_run = True
                        pygame.draw.rect(self.screen, self.background_color, self.help_text_position)
                    if event.key == pygame.constants.K_UP:
                        if self.snake.tails[0]['x'] != self.snake.tails[1]['x']: 
                            self.snake.turn(0, -self.cell_size)
                    elif event.key == pygame.constants.K_DOWN:
                        if self.snake.tails[0]['x'] != self.snake.tails[1]['x']:
                            self.snake.turn(0, self.cell_size)
                    elif event.key == pygame.constants.K_LEFT:
                        if self.snake.tails[0]['y'] != self.snake.tails[1]['y']:
                            self.snake.turn(-self.cell_size, 0)
                    elif event.key == pygame.constants.K_RIGHT:
                        if self.snake.tails[0]['y'] != self.snake.tails[1]['y']:
                            self.snake.turn(self.cell_size, 0)

            self.clock.tick(self.FPS)
            pygame.display.update()

class Snake():
    def __init__(self, x, y, dy, cell_size, max_tails, head_color, color) -> None:
        self.x = x
        self.y = y
        self.dx = cell_size
        self.dy = dy
        self.cell_size = cell_size
        self.tails = []
        self.max_tails = max_tails
        self.head_color = head_color
        self.color = color
        self.collision_with_self = False

    def draw(self, surface, apple):
        self.x += self.dx
        self.y += self.dy

        self.tails.insert(0, {'x': self.x, 'y': self.y})

        if len(self.tails) > self.max_tails:
            self.tails.pop()

        for index, element in enumerate(self.tails):
            if index == 0:
                color = self.head_color
            else:
                color = self.color
            rect = pygame.draw.rect(
                surface,
                color,
                (element['x'], element['y'], self.cell_size, self.cell_size)
            )
            if rect.colliderect(apple.get_rect()):
                self.max_tails += 1
                apple.is_exists = False

            for position in self.tails[index+1:]:
                if element['x'] == position['x'] and element['y'] == position['y']:
                    self.collision_with_self = True

    def turn(self, dx, dy):
        self.dx = dx
        self.dy = dy

class Apple():
    def __init__(self, surface, cell_size, color) -> None:
        self.x = 16
        self.y = 16
        self.surface = surface
        self.size = cell_size / 2
        self.cell_size = cell_size
        self.color = color 
        self.is_exists = False

    def draw(self):
        if not self.is_exists:
            self.update_position()
            self.is_exists = True
        self.rect = pygame.draw.rect(
            self.surface,
            self.color,
            (self.x, self.y, self.size, self.size)
        )
        
    def update_position(self):
        self.x = randint(5, (self.surface.get_width() / self.cell_size - 2)) * self.cell_size
        self.y = randint(5, (self.surface.get_height() / self.cell_size -2)) * self.cell_size

    def get_rect(self):
        return self.rect

if __name__ == '__main__':
    Game(550, 650, 'PySnake', (53, 51, 54), 12)
