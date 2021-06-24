import pygame

class SnakeWindow():
    def __init__(self, width, height, title, background_color, FPS) -> None:
        pygame.init() # pylint: disable=no-member
        self.width = width
        self.height = height
        self.title = title
        self.background_color = background_color
        self.FPS = FPS

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.background_color)
        self.screen_centerx = self.screen.get_width() / 2
        self.screen_centery = self.screen.get_height() / 1.7
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

    def set_text(self, text, font_name, font_size, font_color, centery, bold=False) -> tuple:
        font = pygame.font.SysFont(font_name, font_size, bold=bold)

        text = font.render(text, True, font_color)
        text_position = text.get_rect(centerx=self.screen_centerx, centery=centery)

        self.screen.blit(text, text_position)

        return text_position

    def make_field(self, width, height) -> None:
        self.field_surface = pygame.Surface((width, height))
        self.field_surface.fill(self.background_color)
        # If not need -> make local variable
        self.field_surface_position = self.field_surface.get_rect(
            centerx=self.screen_centerx,
            centery=self.screen_centery
        ) 

    def update_field(self, color, border_radius):
        pygame.draw.rect(
            self.field_surface,
            color,
            self.field_surface.get_rect(),
            border_radius=border_radius
        )

    def loop(self):
        raise Exception('Override this method')
