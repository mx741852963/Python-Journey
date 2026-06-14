import math
import random

import pygame as pg

# pygame setup stuff
pg.init()
w = 1000
h = 700
screen = pg.display.set_mode((w, h))
pg.display.set_caption("PyGame Game")
clock = pg.time.Clock()
running = True
# sounds
pg.mixer.music.load(r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\sound\bg.wav")
pg.mixer.music.set_volume(0.1)
game_over_sound = pg.mixer.Sound(r"sound\game_over.wav")
losing_food_sound = pg.mixer.Sound(r"sound\losing.wav")
pickup_food_sound = pg.mixer.Sound(r"sound\pickup.wav")
# Create Variables to keep track of score and lives
score = 0
lives = 5
angle = 0.0
delta_time = 0
game_over_flag = 1
title_font = pg.font.SysFont("Arial", 50)
score_font = pg.font.SysFont("Arial", 25)
live_font = pg.font.SysFont("Arial", 25)
game_over_font = pg.font.SysFont("Arial", 75)
restart_game = pg.font.SysFont("Arial", 30)
restart_game_text = restart_game.render("Press P To Restart", True, (0, 0, 0))
title_text = title_font.render("Feed Cat", True, (0, 0, 0))
score_text = score_font.render("Score:  " + str(score), True, (0, 0, 0))
live_text = live_font.render("Lives:  " + str(lives), True, (0, 0, 0))
game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))
# Get Text Rect
restart_game_rect = restart_game_text.get_rect()
title_rect = title_text.get_rect()
score_rect = score_text.get_rect()
live_rect = live_text.get_rect()
game_over_rect = game_over_text.get_rect()
# Position the text
title_rect.center = (w // 2, 30)
score_rect.topleft = (10, 5)
live_rect.topleft = (w - live_text.get_width() - 10, 5)
game_over_rect.center = (w // 2, h // 2)
restart_game_rect.center = (w // 2, (h // 2) + 100)
# load our images
cat = pg.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\cat\Idle (1).png"
)
cat = pg.transform.smoothscale(cat, (w / 7, h / 7))
cat_rect = cat.get_rect()
food = pg.Vector2()
food.x = w - 20
food.y = random.randint(150, h - 150)
cat_rect.topleft = (-20, 60)
food_rect = pg.Rect(0, 0, 20, 20)
food_center_y = [food.y]
speed_factor = [300]
move_flag = 1
pg.mixer.music.play(-1)
while running:
    food_rect.center = (food.x, food.y)
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False

    screen.fill("silver")
    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(live_text, live_rect)
    screen.blit(cat, cat_rect)
    pg.draw.aaline(screen, "red", (0, 60), (w, 60))
    pg.draw.circle(screen, "green", food, 10)
    if lives == 0:
        if game_over_flag:
            game_over_sound.play(
                1,
            )
            pg.mixer.music.stop()
            game_over_flag = 0
            move_flag = 0
            food.x = w // 2 + 300
            food.y = h // 2
        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            move_flag = 1
            speed_factor[0] = 300
            game_over_flag = 1
            lives = 6
            score = 0
            # re_render text
            score_text = score_font.render("Score:  " + str(score), True, (0, 0, 0))
            live_text = live_font.render("Lives:  " + str(lives), True, (0, 0, 0))
            pg.mixer.music.play(-1)

        screen.blit(restart_game_text, restart_game_rect)
        screen.blit(game_over_text, game_over_rect)

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and cat_rect.y > 60:
        cat_rect.y -= speed_factor[0] * delta_time
    if keys[pg.K_s] and cat_rect.y < h - cat_rect.height:
        cat_rect.y += speed_factor[0] * delta_time
    if food.x < 0:
        # cat missed the food!
        losing_food_sound.play(1, 400, 300)
        speed_factor[0] = 300
        lives -= 1
        live_text = live_font.render("Lives:  " + str(lives), True, (0, 0, 0))
        if move_flag:
            food_center_y[0] = random.randint(150, h - 150)
            food.x = w - 20
            food.y = food_center_y[0]
    else:
        if move_flag:
            food.x -= 300 * delta_time + score
            angle += 5 * (score * 0.1 + 1) * delta_time
            food.y = food_center_y[0] + math.sin(angle) * 100
    if cat_rect.colliderect(food_rect):
        pickup_food_sound.play(1, 100)
        if score == 10:
            speed_factor[0] = speed_factor[0] - speed_factor[0] * 0.2
        if score == 20:
            speed_factor[0] = speed_factor[0] - speed_factor[0] * 0.4
        if score > 30 and speed_factor[0] > 300:
            speed_factor[0] = speed_factor[0] - speed_factor[0] * 0.5

        score += 1
        score_text = score_font.render("Score:  " + str(score), True, (0, 0, 0))
        if move_flag:
            food_center_y[0] = random.randint(150, h - 150)
            food.x = w - 20
            food.y = food_center_y[0]
    pg.display.flip()

    delta_time = clock.tick(60) / 1000.0
pg.quit()
