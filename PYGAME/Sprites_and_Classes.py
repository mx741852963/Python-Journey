import random

from PIL import Image

import pygame as pg

pg.init()
w = 1000
h = 700
screen = pg.display.set_mode((w, h))
pg.display.set_caption("PyGame Game")
clock = pg.time.Clock()
running = True
# img = Image.open(r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\dog\Idle (1).png")
# new_dimensions = (int(w / 7), int(h / 7))
#
# resized_img = img.resize(new_dimensions, Image.Resampling.LANCZOS)
#
# resized_img.save("dog.png")
# Define a cat class
CAT_IMAGE = pg.image.load("cat.png")


class Cat(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Define our image
        self.image = CAT_IMAGE
        self.rect = self.image.get_rect()
        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, random.randint(100, 300))
        self.rect.topleft = self.position

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)


# Create a cat group
cat_group = pg.sprite.Group()
# Create cat obj
for i in range(10):
    cat = Cat(i * 100, 10)
    cat_group.add(cat)

while running:
    delta_time = clock.tick(60) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False
    screen.fill("silver")
    # Draw cat group
    cat_group.update(delta_time)
    cat_group.draw(screen)
    pg.display.flip()


pg.quit()
