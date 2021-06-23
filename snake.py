import pygame
import sys
import snake_window

class Game(snake_window.SnakeWindow):
    def __init__(self, width, height, title, background_color, FPS) -> None:
        super().__init__(width, height, title, background_color, FPS)

        self.cell_size = 16
        self.is_run = False

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

        self.loop()

    def loop(self):
        while True:
            if self.is_run:
                self.update_field((22, 22, 24), 7)
                self.snake.draw(self.field_surface)
                self.screen.blit(self.field_surface, self.field_surface_position)

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

    def draw(self, surface):
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
            pygame.draw.rect(
                surface,
                color,
                (element['x'], element['y'], self.cell_size, self.cell_size)
            )

    def turn(self, dx, dy):
        self.dx = dx
        self.dy = dy

if __name__ == '__main__':
    Game(550, 650, 'PySnake', (53, 51, 54), 13)
