import pygame as pg

# pygame setup stuff
pg.init()
w = 800
h = 600
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
# Define the Fonts
sys_font = pg.font.SysFont("imapct", 50)
# download_font = pg.font.Font("", 20)
# Render The text (as Surface) Text , boolean for antialiasing , text color , bg color
sys_font = sys_font.render("This is Impact", True, "red", "silver")

# load our images
cat = pg.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\cat\Idle (1).png"
)
dog = pg.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\dog\Idle (1).png"
)
dog = pg.transform.smoothscale(dog, (w / 5, h / 5))
cat = pg.transform.smoothscale(cat, (w / 5, h / 5))
#  get rect surrounding our images
cat_rect = cat.get_rect()
dog_rect = dog.get_rect()
# Position our images
cat_rect.topleft = (0, 0)
dog_rect.topright = (w, 0)
# Get Rect
sys_font_rect = sys_font.get_rect()
# Position the text
sys_font_rect.center = (w // 2, 200)
sound_flag = 0
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
    # blit screen object at a given coordinate
    # sorting blit make the surface above another
    screen.blit(sys_font, sys_font_rect)
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
    if keys[pg.K_d] and cat_rect.x < w - cat_rect.width:
        cat_rect.x += 500 * delta_time
    # flip the display to output our work to the screen
    pg.display.flip()
    # Set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    delta_time = clock.tick(60) / 1000.0
pg.quit()
