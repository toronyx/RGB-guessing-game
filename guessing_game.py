import pygame as pg
import sys
import numpy.random as random

import text_input_box

# General setup
pg.init()
clock = pg.time.Clock()

# Setting up the main window
screen_width = 720
screen_height = 720
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('RGB Guesser')
user_text = 'test'

base_font=pg.font.Font(None,64)

# Initial background color
color=random.randint(0,255,3)
screen.fill(color)

# intialise text input boxes
text_box_1 = text_input_box.TextInputBox(screen,
                                         150, screen_height/2,
                                         100, 50)
text_box_2 = text_input_box.TextInputBox(screen,
                                         300, screen_height/2,
                                         100, 50)
text_box_3 = text_input_box.TextInputBox(screen,
                                         450, screen_height/2,
                                         100, 50)

while True:
    # Handling input
    for event in pg.event.get():
        text_box_1.handle_event(event)
        text_box_2.handle_event(event)
        text_box_3.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) :
            if not (text_box_1.active or text_box_2.active
                    or text_box_3.active):
                # Choose random RGB color
                color = random.randint(0,255,3)
                screen.fill(color)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                color_guess = (int(text_box_1.text), int(text_box_2.text),
                               int(text_box_3.text))
                invalid_color = False
                for number in color_guess:
                    if number>255:
                        txt_surface = base_font.render('Invalid color!',
                                                       True, (255,255,255))
                        screen.blit(txt_surface, (0, 0))
                        invalid_color = True
                if not invalid_color:
                    pg.draw.rect(screen, color_guess, pg.Rect(10, 10, 100, 100))
                    answer_string = f'{color[0]}  {color[1]}  {color[2]}'
                    txt_surface = base_font.render(answer_string,
                                                   True, (255,255,255))
                    screen.blit(txt_surface, (230, 250))
    text_box_1.draw(screen)
    text_box_2.draw(screen)
    text_box_3.draw(screen)

    # Update the window
    pg.display.flip() # updates everything
    clock.tick(60) # limits loop to 60 FPS
