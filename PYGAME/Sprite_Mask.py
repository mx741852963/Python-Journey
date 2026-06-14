from map import tile_map

import pygame

# Initialize the game
pygame.init()

# Set display surface (divisible by 32 tile size)
WINDOW_WIDTH = 960  # 30 columns
WINDOW_HEIGHT = 640  # 20 rows
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")
# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
image1 = pygame.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\tiles\dirt.png"
)
image2 = pygame.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\tiles\grass.png"
)
image3 = pygame.image.load(
    r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\tiles\water.png"
)
vector = pygame.math.Vector2


# Tile Class
class Tile(pygame.sprite.Sprite):
    # Read and Create tiles and put em on the screen
    def __init__(self, x, y, image_integer, main_group, sub_group=None):
        super().__init__()
        # Load image and add to the tile subgroups
        if image_integer == 1:
            self.image = image1

        elif image_integer == 2:
            self.image = image2
            # mask
            self.mask = pygame.mask.from_surface(self.image)
            sub_group.add(self)
        elif image_integer == 3:
            self.image = image3
            sub_group.add(self)
        # add every tile to main tile group
        main_group.add(self)
        # Get rect of images and position within the grid
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group, plear):
        super().__init__()
        self.velocity = 20
        self.range = 450
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)

        self.rect = self.image.get_rect()
        if plear.velocity.x < 0:
            self.velocity = -1 * self.velocity
        self.rect.center = (x, y)
        pygame.draw.circle(self.image, "red", (6, 6), 6)
        bullet_group.add(self)

    def update(self):
        self.rect.x += self.velocity
        # if abs(self.rect.x - self.velocity) > self.range:
        #     self.kill()


class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y, grass_tile, water_tile, bullet):
        super().__init__()
        # Define our image
        # self.image = CAT_IMAGE
        # self.rect = self.image.get_rect(bottomleft=(x, y))
        self.cur_s = 0  # first in list
        # Animations lists
        self.move_r = []
        self.move_l = []
        self.idle_r = []
        self.idle_l = []
        self.Jump_l = []
        self.Jump_r = []
        self.slide_r = []
        self.slide_l = []
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (1).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (2).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (3).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (4).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (5).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (6).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (7).png"), (85, 74)
            )
        )
        self.Jump_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Jump (8).png"), (85, 74)
            )
        )
        for sprites in self.Jump_r:
            self.Jump_l.append(pygame.transform.flip(sprites, True, False))
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (1).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (2).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (3).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (4).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (5).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (6).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (7).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (8).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (9).png"), (85, 74)
            )
        )
        self.move_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Walk (10).png"), (85, 74)
            )
        )
        for sprites in self.move_r:
            self.move_l.append(pygame.transform.flip(sprites, True, False))
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (1).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (2).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (3).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (4).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (5).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (6).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (7).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (8).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (9).png"), (85, 74)
            )
        )
        self.idle_r.append(
            pygame.transform.smoothscale(
                pygame.image.load(r"png\cat\Idle (10).png"), (85, 74)
            )
        )
        for sprites in self.idle_r:
            self.idle_l.append(pygame.transform.flip(sprites, True, False))

        # set our image
        self.image = self.move_r[self.cur_s]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.grass_tiles = grass_tile
        self.water_tile = water_tile
        self.mask = pygame.mask.from_surface(self.idle_r[0])
        self.bullet = bullet
        # kinematic  Vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)  # Don'ts move to start
        self.acceleration = vector(0, 0)  # no Speed up
        # kinematic constants
        self.horizontal_acceleration = 0.5  # speed up
        self.horizontal_friction = 0.10
        self.vertical_acceleration = 0.5  # gravity
        self.vertical_friction = 10  # going to determine how high we can jump

    def animation(self, sprite_list, speed=1):
        if self.cur_s < len(sprite_list) - 1:
            self.cur_s += speed
        else:
            self.cur_s = 0
        self.image = sprite_list[int(self.cur_s)]

    def jump(self):
        # only want to jump when cat is on grass
        if pygame.sprite.spritecollide(self, self.grass_tiles, False):
            self.velocity.y = -1 * self.vertical_friction
            if abs(self.velocity.x) < 0.1:
                self.velocity.x = 0
            elif self.velocity.x > 0:
                self.velocity.x = 1 * self.vertical_friction
            elif self.velocity.x < 0:
                self.velocity.x = -1 * self.vertical_friction

    def update(self):

        # pygame.draw.rect(display_surface, "red", self.rect, 1)
        # Create a mask
        # self.mask = pygame.mask.from_surface(self.image)
        # # Draw Mask (points surrounding player)
        # mask_out = self.mask.outline()
        # pygame.draw.lines(self.image, "blue", True, mask_out)
        # set acceleration to 0,0
        self.acceleration = vector(0, self.vertical_acceleration)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()
        elif keys[pygame.K_a] and self.position.x > 0:
            self.acceleration.x = -1 * self.horizontal_acceleration
        elif keys[pygame.K_d] and self.position.x < 960 - self.rect.width:
            self.acceleration.x = self.horizontal_acceleration
        if keys[pygame.K_LEFT]:
            self.shoot()
        if not self.velocity.y:
            if self.velocity.x > 0:
                self.animation(self.idle_r, 0.8)
            else:
                self.animation(self.idle_l, 0.8)
        if self.acceleration.x < 0:
            self.animation(self.move_l)
        if self.acceleration.x > 0:
            self.animation(self.move_r)
        if self.velocity.y and self.velocity.x > 0:
            self.animation(self.Jump_r, 0.15)
        if self.velocity.y and self.velocity.x < 0:
            self.animation(self.Jump_l, 0.15)
        if self.velocity.y and self.velocity.x == 0.0:
            if self.velocity.y > 0:
                self.animation(self.Jump_r, 0.15)
            if self.velocity.y < 0:
                self.animation(self.Jump_l, 0.15)

        self.acceleration.x -= self.velocity.x * self.horizontal_friction
        self.velocity += self.acceleration  # (1,2) +(3,4) = (4,6)
        self.position += self.velocity + 0.5 * self.acceleration
        if self.position.x < 0:
            self.position.x = 960
        if self.position.x > 960:
            self.position.x = 0
        self.rect.bottomleft = self.position
        touched_platforms = pygame.sprite.spritecollide(
            self, self.grass_tiles, False, pygame.sprite.collide_mask
        )  # Return a python list of tiles we touched
        if touched_platforms:
            if self.velocity.y > 0:
                self.position.y = touched_platforms[0].rect.top + 3
                self.velocity.y = 0
        # water
        if pygame.sprite.spritecollide(self, self.water_tile, False):
            print("water tile collision")

    def shoot(self):
        Bullet(self.rect.centerx, self.rect.centery, self.bullet, self)


# Define our sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
cat_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Create a tile map, nested python list: 0=no tile, 1=dirt, 2=grass, 3=water
# Create Tile objects from the tile map
# 2 for loops because tile map is nested. 20 i down
for i in range(len(tile_map)):
    # loop thru the 30 elements in each list, j across
    for j in range(len(tile_map[i])):
        # Check for 0,1,2,3
        if tile_map[i][j] == 1:
            # dirt
            Tile(j * 32, i * 32, 1, main_tile_group)
        elif tile_map[i][j] == 2:
            # grass
            Tile(j * 32, i * 32, 2, main_tile_group, grass_tile_group)

        elif tile_map[i][j] == 3:
            # water
            Tile(j * 32, i * 32, 3, main_tile_group, water_tile_group)
        elif tile_map[i][j] == 4:
            cat = Cat(
                j * 32, i * 32 + 32, grass_tile_group, water_tile_group, bullet_group
            )
            cat_group.add(cat)
# Add a bg
bg = pygame.image.load(r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\png\tiles\bg.png")
# bg = pygame.image.load("png".join("tiles",'bg.png'))
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)
# Game Loop
running = True
while running:
    # Check to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # # Jump
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         cat.jump()
    # Draw the Tiles
    display_surface.blit(bg, (0, 0))
    main_tile_group.draw(display_surface)
    cat_group.update()
    cat_group.draw(display_surface)
    bullet_group.update()
    bullet_group.draw(display_surface)

    # Update Display
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
