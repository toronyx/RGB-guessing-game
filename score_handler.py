import pygame as pg
import numpy as np

pg.init()

class ScoreHandler:
    def __init__(self, score_pos, points_pos,# colors_guessed_pos,
                 font=pg.font.Font(None,64)):
        self.score_pos = score_pos
        self.points_pos = points_pos
        #self.colors_guessed_pos = colors_guessed_pos
        self.font = font
        self.font_color = (255,255,255)
        self.score = 0
        self.points = 0
        self.colors_guessed = 0

    def calculate_points(self, bg_color, color_guess):
        # max difference possible is 765, but for most colors max is ~300
        difference = np.sum(np.abs(bg_color - color_guess))
        self.points = int(100*np.exp(-difference/50))
        return self.points

    def draw_string(self, screen, string, pos):
        txt_surface = self.font.render(string, True,
                                       self.font_color)
        # Blit the text.
        screen.blit(txt_surface, pos)

    def draw_score(self, screen):
        string = "Score: " + str(self.score)
        self.draw_string(screen, string, self.score_pos)

        string = "Colors guessed: " + str(self.colors_guessed)
        colors_guessed_pos = tuple(map(sum, zip(self.score_pos, (0,50))))
        self.draw_string(screen, string, colors_guessed_pos)
        return

    def draw_points(self, screen):
        string = "+ " + str(self.points)
        self.draw_string(screen, string, self.points_pos)
        return
