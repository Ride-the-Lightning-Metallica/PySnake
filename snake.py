import pygame
import sys
import snake_window

class Game(snake_window.SnakeWindow):
    def __init__(self, width, height, title, background_color, FPS) -> None:
        super().__init__(width, height, title, background_color, FPS)
        self.set_text('Press \'Space\'', 'verdana', 32, (202, 76, 38), 60, bold=True) 
        pygame.draw.rect(
            self.screen,
            (18, 18, 20),
            (self.screen_centerx - 95, 100, 190, 70),
            border_radius=5
        )
        self.set_text('0', 'verdana', 32, (202, 76, 38), 135, bold=True)
        self.make_field(320, 400, (22, 22, 24), 7)
        self.loop()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.draw.rect(self.screen, self.background_color, self.help_text_position)

            self.clock.tick(self.FPS)
            pygame.display.update()


if __name__ == '__main__':
    Game(550, 650, 'PySnake', (53, 51, 54), 60)