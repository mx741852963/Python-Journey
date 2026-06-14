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
# Display all fonts
# fonts = pg.font.get_fonts()
# for font in fonts:
#     print(font)
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
while running:
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
    if keys[pg.K_w]:
        cat_rect.y -= 500 * delta_time
    if keys[pg.K_s]:
        cat_rect.y += 500 * delta_time
    if keys[pg.K_a]:
        cat_rect.x -= 500 * delta_time
    if keys[pg.K_d]:
        cat_rect.x += 500 * delta_time
    # flip the display to output our work to the screen
    pg.display.flip()
    # Set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    delta_time = clock.tick(60) / 1000.0
pg.quit()
