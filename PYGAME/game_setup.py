import pygame as pg

# pygame setup stuff
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("PyGame Game")
clock = pg.time.Clock()
running = True
delta_time = 0
player_position = pg.Vector2(screen.get_width() // 2, screen.get_height() // 2)
while running:
    # poll for events
    # pg.QUIT event means that user clicked the X
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False
    # Pick  the screen color
    screen.fill("silver")
    # Render our game here
    pg.draw.circle(screen, "green", player_position, 20)
    # Move our circle
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_position.y -= 900 * delta_time
    if keys[pg.K_s]:
        player_position.y += 900 * delta_time
    if keys[pg.K_a]:
        player_position.x -= 900 * delta_time
    if keys[pg.K_d]:
        player_position.x += 900 * delta_time
    # flip the display to output our work to the screen
    pg.display.flip()
    # Set the clock stuff / delta time in seconds since the last frame
    # used for framerate independent physics
    delta_time = clock.tick(60) / 1000.0


pg.quit()
