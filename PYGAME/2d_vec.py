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
            sub_group.add(self)
        elif image_integer == 3:
            self.image = image3
            sub_group.add(self)
        # add every tile to main tile group
        main_group.add(self)
        # Get rect of images and position within the grid
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


CAT_IMAGE = pygame.image.load(r"C:\Users\ahmad\Desktop\Python-Journey\PYGAME\cat.png")


class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y, grass_tile, water_tile):
        super().__init__()
        # Define our image
        self.image = CAT_IMAGE
        self.rect = self.image.get_rect(bottomleft=(x, y))
        self.grass_tiles = grass_tile
        self.water_tile = water_tile
        # kinematic  Vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)  # Don'ts move to start
        self.acceleration = vector(0, 0)  # no Speed up
        # kinematic constants
        self.horizontal_acceleration = 2  # speed up
        self.horizontal_friction = 0.10
        self.vertical_acceleration = 0.5  # gravity
        self.vertical_friction = 10  # going to determine how high we can jump

    def jump(self):
        # only want to jump when cat is on grass
        if pygame.sprite.spritecollide(self, self.grass_tiles, False):
            print("grass")
            self.velocity.y = -1 * self.vertical_friction

    def update(self):
        # set acceleration to 0,0
        self.acceleration = vector(0, self.vertical_acceleration)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.position.x > 0:
            self.acceleration.x = -1 * self.horizontal_acceleration
        if keys[pygame.K_d] and self.position.x < 960 - self.rect.width:
            self.acceleration.x = self.horizontal_acceleration
        self.acceleration.x -= self.velocity.x * self.horizontal_friction
        self.velocity += self.acceleration  # (1,2) +(3,4) = (4,6)
        self.position += self.velocity + 0.5 * self.acceleration
        if self.position.x < 0:
            self.position.x = 960
        if self.position.x > 960:
            self.position.x = 0
        self.rect.bottomleft = self.position
        touched_platforms = pygame.sprite.spritecollide(
            self, self.grass_tiles, False
        )  # Return a python list of tiles we touched
        if touched_platforms:
            self.position.y = touched_platforms[0].rect.top + 1
            self.velocity.y = 0
        # water
        if pygame.sprite.spritecollide(self, self.water_tile, False):
            print("water tile collision")


# Define our sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
cat_group = pygame.sprite.Group()
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
            cat = Cat(j * 32, i * 32 + 32, grass_tile_group, water_tile_group)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cat.jump()
    # Draw the Tiles
    display_surface.blit(bg, (0, 0))
    main_tile_group.draw(display_surface)
    cat_group.update()
    cat_group.draw(display_surface)

    # Update Display
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()
