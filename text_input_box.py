import pygame as pg

pg.init()

class TextInputBox:
    def __init__(self, screen, x, y, w, h, text='',
                 font=pg.font.Font(None,64)):
        self.rect = pg.Rect(x, y, w, h)
        self.box_color = (255,255,255)
        self.font_color = (0,0,0)
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.font_color)
        self.active = False

    def handle_event(self, event):
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1):
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key in [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4,
                                 pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]:
                    if len(self.text) < 3:
                        self.text += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    pass
                # re-render the text
                self.txt_surface = self.font.render(self.text, True,
                                                    self.font_color)

    def clear(self):
        self.text = ''
        # re-render the text
        self.txt_surface = self.font.render(self.text, True,
                                            self.font_color)

    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.box_color, self.rect)
        if self.active:
            pg.draw.rect(screen, (0,0,0), self.rect, 4)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
