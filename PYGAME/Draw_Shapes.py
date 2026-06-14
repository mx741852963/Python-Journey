import pygame as pg

# pygame setup stuff
pg.init()
window_height = 600
window_width = 800
screen = pg.display.set_mode((window_width, window_height))
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
    # understand co-ordination
    # Top left corner is 0,0
    # as we move -> x increases , as you go down -> y increases
    # Draw a line
    # (screen,color,starting point (x,y),ending point (x,y),thickness)
    # pg.draw.line(screen, "red", (0, 50), (800, 50), 5)
    # Draw a circle
    # (screen,color,center(x,y),radius,thickness:0=fill)
    # pg.draw.circle(screen, "red", player_position, 100, 10)
    # Draw a rectangle
    # (screen,color,(top_left.x,top_left.y,width,height)
    # pg.draw.rect(
    #     screen,
    #     "green",
    #     (100, 100, 100, 100),
    # )
    # pg.draw.polygon(screen, "green", [(100, 100), (500, 500), (100, 100)], 5)
    # pg.draw.ellipse(screen, "green", (100, 400, 400, 100), 5)
    # pg.draw.arc(screen, "red", (100, 400, 400, 100), 3, 0, 20)
    # pg.draw.lines(screen, "red", False, [(100, 100), (200, 200), (300, 300)], 2)
    # pg.draw.aaline(screen, "green", (100, 400), (200, 400), 2)
    pg.draw.rect(screen, "blue", (50, 50, 200, 100), 0)
    pg.draw.rect(screen, "lightblue", (300, 50, 200, 100), 0, border_radius=15)
    pg.draw.polygon(screen, "yellow", [(600, 150), (700, 50), (800, 150)], 0)
    pg.draw.ellipse(screen, "purple", (300, 250, 200, 100), 4)
    import math

    pg.draw.arc(screen, "orange", (550, 250, 200, 100), 1, math.pi, 3)
    pg.draw.line(screen, "black", (50, 450), (750, 450), 5)
    pg.draw.aaline(screen, "darkgreen", (50, 480), (750, 520))
    pg.draw.lines(
        screen, "brown", False, [(50, 580), (200, 540), (400, 580), (600, 540)], 3
    )
    pg.draw.aalines(screen, "magenta", True, [(650, 540), (700, 580), (750, 540)])
    pg.display.flip()
    delta_time = clock.tick(60) / 1000

pg.quit()
