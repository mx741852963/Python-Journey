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
delta_time = 0
# Load our sound effects
sound_1 = pg.mixer.Sound(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\sound\sound_2.wav"
)
pg.mixer.music.load(r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\sound\sound.wav")
# Play the BG music
# pg.mixer.music.play(-1, 0.0)  # Repeats and where to start playing
pg.mixer.music.set_volume(0.1)
# Play our sound effects
# sound_1.play()
# Time delay
pg.time.delay(5)
# Change the volume
sound_1.set_volume(0.1)
timer = 0

# load our images
cat = pg.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\cat\Idle (1).png"
)
dog = pg.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\dog\Idle (1).png"
)
dog = pg.transform.smoothscale(dog, (w / 7, h / 7))
cat = pg.transform.smoothscale(cat, (w / 7, h / 7))
#  get rect surrounding our images
cat_rect = cat.get_rect()
dog_rect = dog.get_rect()
# Position our images
cat_rect.topleft = (0, 0)
dog_rect.center = (w // 2, h // 2)
sound_flag = 0
border = (h, w)
while running:
    timer += delta_time
    if timer > 5 and not sound_flag:
        pg.mixer.music.play(-1, 0.0)
        sound_flag = 1
        # poll for events
    # pg.QUIT event means that user clicked the X
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False
    # Pick  the screen color
    screen.fill("silver")
    # Draw some rects
    pg.draw.rect(screen, (0, 255, 0), cat_rect, 1)
    pg.draw.rect(screen, (0, 255, 0), dog_rect, 1)
    # blit screen object at a given coordinate
    # sorting blit make the surface above another
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)

    # Render our game here
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and cat_rect.y > 0:
        cat_rect.y -= 500 * delta_time
    if keys[pg.K_s] and cat_rect.y < h - cat_rect.height:
        cat_rect.y += 500 * delta_time
    if keys[pg.K_a] and cat_rect.x > 0:
        cat_rect.x -= 500 * delta_time
        # sound_1.play(1, 500)
    if keys[pg.K_d] and cat_rect.x < w - cat_rect.width:
        cat_rect.x += 500 * delta_time
    if dog_rect.colliderect(cat_rect):
        # Push image
        # if dog_rect.x < border[0] and dog_rect.y < border[1]:
        #     dog_rect.y += 100 * delta_time
        #     dog_rect.x += 100 * delta_time
        # # Remove The image
        # dog.fill(0)
        # Random Move Image
        dog_rect.x = random.randint(0, h - cat_rect.width)
        dog_rect.y = random.randint(0, h - cat_rect.height)
    # flip the display to output our work to the screen
    pg.display.flip()
    # Set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    delta_time = clock.tick(60) / 1000.0
pg.quit()
