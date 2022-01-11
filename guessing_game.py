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
bg_color=random.randint(0,255,3)
screen.fill(bg_color)

# intialise text input boxes
input_boxes=[]
for i in range(3):
    input_boxes.append(text_input_box.TextInputBox(screen, [150,300,450][i],
                                                   screen_height/2-50,
                                                   90, 50))
input_boxes[0].active = True
# text_box_1 = text_input_box.TextInputBox(screen,
#                                          150, screen_height/2-50,
#                                          90, 50)
# text_box_1.active = True
# text_box_2 = text_input_box.TextInputBox(screen,
#                                          300, screen_height/2-50,
#                                          90, 50)
# text_box_3 = text_input_box.TextInputBox(screen,
#                                          450, screen_height/2-50,
#                                          90, 50)
# text_input_boxes = [text_box_1, text_box_2, text_box_3]

while True:
    # Handling input
    for event in pg.event.get():
        for input_box in input_boxes:
            input_box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # if (event.type == pg.MOUSEBUTTONDOWN) and (event.button == 1) :
        #     if not (input_boxes[0].active or input_boxes[1].active
        #             or input_boxes[2].active):
        #         # Choose random RGB color
        #         bg_color = random.randint(0,255,3)
        #         screen.fill(bg_color)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # Choose random RGB color
                bg_color = random.randint(0,255,3)
                screen.fill(bg_color)
            if event.key == pg.K_TAB:
                # cycle through the textboxes
                for i in range(3):
                    if input_boxes[i].active:
                        input_boxes[i].active = False
                        input_boxes[(i+1)%3].active = True
                        break
            if event.key == pg.K_RETURN:
                try:
                    color_guess = (int(input_boxes[0].text),
                                   int(input_boxes[1].text),
                                   int(input_boxes[2].text))
                    pg.draw.rect(screen, color_guess,
                                 pg.Rect(0, 0, screen_width, screen_height/2))
                    for i in range(3):
                        txt_surface = base_font.render(str(bg_color[i]),
                                                       True, (255,255,255))
                        screen.blit(txt_surface,
                                    (input_boxes[i].rect[0], screen_height/2))

                    # answer_string = f'{bg_color[0]}  {bg_color[1]}  {bg_color[2]}'
                    # txt_surface = base_font.render(answer_string,
                    #                                True, (255,255,255))
                    # screen.blit(txt_surface, (230, 250))
                except:
                    txt_surface = base_font.render('Invalid color!',
                                                   True, (255,255,255))
                    screen.blit(txt_surface, (0, 0))
    for input_box in input_boxes:
        input_box.draw(screen)
    # Update the window
    pg.display.flip() # updates everything
    clock.tick(60) # limits loop to 60 FPS
