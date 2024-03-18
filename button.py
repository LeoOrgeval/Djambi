import pygame
import constantes


class Button:
    def __init__(self, x, y, width, height, text, color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(constantes.MYFONT, 25)
        self.text_color = text_color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, False, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class MiddleButton(Button):
    def __init__(self, dimensions: tuple, text, offset: tuple = (0, 0), action=None):
        (width, height) = dimensions
        (offset_x, offset_y) = offset
        x = (constantes.SCREEN_WIDTH - width) // 2
        y = (constantes.SCREEN_HEIGHT - height) // 2
        super().__init__(x + offset_x, y + offset_y, width, height, text, constantes.color['BLUE'],
                         constantes.color['WHITE'], action)


class VolumeButton(Button):
    def __init__(self, dimensions: tuple, text, offset: tuple = (0, 0), action=None):
        (width, height) = dimensions
        (offset_x, offset_y) = offset
        x = (constantes.SCREEN_WIDTH - width)
        y = (constantes.SCREEN_HEIGHT - height)
        super().__init__(x + offset_x, y + offset_y, width, height, text, constantes.color['BLUE'],
                         constantes.color['WHITE'], action)

        #    self.sound_enabled = True

        def toggle_sound(self):
            self.sound_enabled = not self.sound_enabled
            self.set_icon(self.icon_on if self.sound_enabled else self.icon_off)
