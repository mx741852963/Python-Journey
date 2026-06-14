import random

import pygame as pg

pg.init()
w = 1000
h = 700
screen = pg.display.set_mode((w, h))
pg.display.set_caption("PyGame Game")
clock = pg.time.Clock()
running = True


# Define a food class
class Food(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        pg.draw.circle(self.image, "green", (10, 10), 10)
        self.rect = self.image.get_rect()
        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, random.randint(100, 300))
        self.rect.topleft = self.position

    def update(self, dt):
        self.position.y += self.velocity.y * dt
        self.rect.y = int(self.position.y)
        if self.rect.top > h:
            self.kill()


# Define a cat class
CAT_IMAGE = pg.image.load("cat.png")


class Cat(pg.sprite.Sprite):
    def __init__(self, x, y, food_group):
        super().__init__()
        # Define our image
        self.image = CAT_IMAGE
        self.rect = self.image.get_rect()
        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(300, 300)
        self.rect.topleft = self.position
        # Add food Group to cat class
        self.food_group = food_group

    def update(self, dt):
        self.move(dt)
        self.check_collision()

    def move(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position.y -= self.velocity.y * dt
        if keys[pg.K_s]:
            self.position.y += self.velocity.y * dt
        if keys[pg.K_a]:
            self.position.x -= self.velocity.x * dt
        if keys[pg.K_d]:
            self.position.x += self.velocity.x * dt
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)

    def check_collision(self):
        if pg.sprite.spritecollide(self, self.food_group, True):
            print(len(self.food_group))


# Create a food group
food_group = pg.sprite.Group()
# Create food obj
for i in range(8):
    food = Food(i * 100, 10)
    food_group.add(food)
# Create a cat group
cat_group = pg.sprite.Group()
cat = Cat(200, 400, food_group)
cat_group.add(cat)
while running:
    delta_time = clock.tick(60) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False

    # Draw cat and food group
    cat_group.update(delta_time)
    food_group.update(delta_time)
    screen.fill("silver")
    cat_group.draw(screen)

    food_group.draw(screen)
    pg.display.flip()


pg.quit()
