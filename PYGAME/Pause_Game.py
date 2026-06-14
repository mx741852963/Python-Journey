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
    def __init__(self, x, y):
        super().__init__()
        # Define our image
        self.image = CAT_IMAGE
        self.rect = self.image.get_rect()
        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(300, 300)
        self.rect.topleft = self.position

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.position.y > 0:
            self.position.y -= self.velocity.y * dt
        if keys[pg.K_s] and self.position.y < h - self.rect.height:
            self.position.y += self.velocity.y * dt
        if keys[pg.K_a] and self.position.x > 0:
            self.position.x -= self.velocity.x * dt
        if keys[pg.K_d] and self.position.x < w - self.rect.width:
            self.position.x += self.velocity.x * dt
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)


# Define a Game class
class Game:
    def __init__(self):
        self.food_group = pg.sprite.Group()
        self.cat_group = pg.sprite.Group()
        self.spawn_initial_entities()
        self.is_paused = False
        self.font = pg.font.SysFont("Arial", 40, bold=True)
        self.pause_text = self.font.render("PAUSE", True, "red")
        self.pause_rect = self.pause_text.get_rect()
        self.pause_rect.center = (1000 // 2, 700 // 2)

    def spawn_initial_entities(self):
        for i in range(8):
            food = Food(i * 100, 10)
            self.food_group.add(food)
        cat = Cat(200, 400)
        self.cat_group.add(cat)

    def update(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_p]:
            self.is_paused = True
        if self.is_paused:
            if keys[pg.K_RETURN]:
                self.is_paused = False
            return
        self.check_collision()
        self.cat_group.update(dt)
        self.food_group.update(dt)

    def check_collision(self):
        if pg.sprite.groupcollide(self.cat_group, self.food_group, False, True):
            print(len(self.food_group))

    def draw(self, surface):
        self.cat_group.draw(surface)
        self.food_group.draw(surface)
        if self.is_paused:
            surface.blit(self.pause_text, self.pause_rect)


our_game = Game()
while running:
    delta_time = clock.tick(60) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:  # X
            running = False

    # Draw cat and food group
    our_game.update(delta_time)
    screen.fill("silver")
    our_game.draw(screen)
    pg.display.flip()

pg.quit()
