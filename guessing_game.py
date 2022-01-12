import pygame as pg
import sys
import numpy.random as random
import numpy as np

import text_input_box
import score_handler

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
bg_color=random.randint(0,255,3)
screen.fill(bg_color)

# intialise text input boxes
input_boxes=[]
for i in range(3):
    input_boxes.append(text_input_box.TextInputBox(screen, [150,300,450][i],
                                                   screen_height/2-50,
                                                   90, 50))
input_boxes[0].active = True
score_handler = score_handler.ScoreHandler((30,30), (330,200))
colors_guessed = 0



while True:
    # Handling input
    for event in pg.event.get():
        for input_box in input_boxes:
            input_box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Clear input boxes
                for input_box in input_boxes:
                    input_box.clear()
                # Choose random RGB background color
                bg_color = random.randint(0,255,3)
                screen.fill(bg_color)
                score_handler.draw_score(screen)
            if event.key == pg.K_TAB:
                # cycle through the textboxes
                for i in range(3):
                    if input_boxes[i].active:
                        input_boxes[i].active = False
                        input_boxes[(i+1)%3].active = True
                        break
            if event.key == pg.K_RETURN:
                # submit answer
                try:
                    color_guess = (int(input_boxes[0].text),
                                   int(input_boxes[1].text),
                                   int(input_boxes[2].text))
                    # display the guess as a color
                    pg.draw.rect(screen, color_guess,
                                 pg.Rect(0, 0, screen_width, screen_height/2))
                    guess_successful = True
                except:
                    txt_surface = base_font.render('Invalid color!',
                                                   True, (255,255,255))
                    screen.blit(txt_surface, (0, 0))
                    guess_successful = False

                if guess_successful:
                    score_handler.colors_guessed += 1
                    # present answer
                    for i in range(3):
                        txt_surface = base_font.render(str(bg_color[i]),
                                                       True, (255,255,255))
                        screen.blit(txt_surface,
                                    (input_boxes[i].rect[0]+5,
                                     screen_height/2+5))
                    score_handler.calculate_points(bg_color, color_guess)
                    score_handler.score += score_handler.points
                    score_handler.draw_points(screen)
                    score_handler.draw_score(screen)

    for input_box in input_boxes:
        input_box.draw(screen)
    # Update the window
    pg.display.flip() # updates everything
    clock.tick(60) # limits loop to 60 FPS
