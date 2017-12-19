import pygame
import random
pygame.init()

pygame.key.set_repeat(50,50)

class Player:
    def __init__(self, player_images, screen):
        self.images = player_images
        self.screen = screen
        self.player_rect = self.images[0].get_rect().unionall([self.images[i].get_rect() for i in range(1, len(self.images))])
        self.run_speed = 5
        self.jump_speed = 0
        self.screen_rect = self.screen.get_rect()
        self.player_rect.bottom = self.screen_rect.bottom
        self.can_jump = True
        self.key_space_up = True

    def player_draw(self, background, item):
        for pic in self.images:
            self.player_jump()
            if self.player_rect.left >= self.screen_rect.right / 8:
                self.player_rect.left = self.screen_rect.right / 8
            else:
                self.player_rect.left += self.run_speed
            self.player_rect.bottom += self.jump_speed
            self.screen.blit(background, [0, 0])
            self.screen.blit(pic, self.player_rect)
            item.item_draw(self.screen, self)
            pygame.display.update() # try pygame.display.update(self.player_rect)
            pygame.time.delay(80)
# maybe it's better to make the value of jump_speed as a variable
    def player_jump(self):
        if self.can_jump == False:
            self.jump_speed = 30
            if self.player_rect.bottom >= self.screen_rect.bottom:
                self.jump_speed = 0
                self.can_jump = True
        elif self.player_rect.bottom <= self.screen_rect.bottom / 2:
            self.jump_speed = 30
            self.can_jump = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.can_jump == True and self.key_space_up == True:
                    self.jump_speed = -60
                    self.key_space_up = False
                elif event.key == pygame.K_SPACE and self.can_jump == False:
                    self.key_space_up = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.can_jump = False
                    self.key_space_up = True


class Item:
    def __init__(self, item_image):
        self.item_image = item_image
        self.item_rect = self.item_image.get_rect()
        self.item_positions = []
        self.item_speed = 20

    def positions(self, *pos_func):
        for carrot_pos in range(1280 / 6, 1280 * 20, 120):
            self.item_positions.append(pygame.Rect(carrot_pos, random.randint(720 / 2, (720 / 2 + 720 - 170)) / 2, self.item_rect[2], self.item_rect[3]))
            self.item_positions.append(pygame.Rect(carrot_pos, random.randint((720 / 2 + 720 - 170) / 2, 720 - 170), self.item_rect[2], self.item_rect[3]))

    def item_draw(self, screen, player):
        # self.positions()
        for item_pos in self.item_positions:
            item_pos.left -= self.item_speed
            screen.blit(self.item_image, item_pos)
            if player.player_rect.colliderect(item_pos):
                self.item_positions.remove(item_pos)


class Game():
    def __init__(self, screen, player, item):
        pass
#         self.screen_x = screen.screen_x
#         self.screen_y = screen.screen_y
#         self.screen = pygame.display.set_mode((screen.screen_x, screen.screen_y))
#         self.images = player.images
#         self.x = player.start_coord[0]
#         self.y = player.start_coord[1]
#         self.rect_coord = self.images[0].get_rect().unionall([self.images[i].get_rect() for i in range(1, len(self.images))])
#         self.speed = player.speed

# class Colors:
#     def __init__(self):
#         self.WHITE = (255, 255, 255)
#         self.BLACK = (0, 0, 0)
#         self.RED = (255, 0, 0)
#         self.GREEN = (0, 255, 0)
#         self.DARKER_GREEN = (0, 200, 0)
#         self.BLUE = (0, 0, 255)
#         self.SKY = (0, 126, 255)
#         self.YELLOW = (255, 255, 0)
#         self.ORANGE = (255, 126, 0)
#
#
# class Screen:
#     def __init__(self, screen_x, screen_y):
#         self.screen_x = screen_x
#         self.screen_y = screen_y
#         self.screen = pygame.display.set_mode((screen_x, screen_y))

screen_x = 1280
screen_y = 720
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('Bunny running v3.0 beta')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKER_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
SKY = (0, 126, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 126, 0)

font = pygame.font.SysFont('Calibri', 25, True, False)
font_large = pygame.font.SysFont('Calibri', 72, True, False)

background_image = pygame.transform.scale(pygame.image.load("the-house-in-the-field.jpg"), (screen_x, screen_y))

image_bunny_1 = pygame.image.load("Bunny (1).png")
image_bunny_2 = pygame.image.load("Bunny (2).png")
image_bunny_3 = pygame.image.load("Bunny (3).png")
image_bunny_4 = pygame.image.load("Bunny (4).png")
image_bunny_5 = pygame.image.load("Bunny (5).png")
image_bunny_6 = pygame.image.load("Bunny (6).png")
image_bunny_7 = pygame.image.load("Bunny (7).png")
image_bunny_8 = pygame.image.load("Bunny (8).png")

bunny_images = [image_bunny_1, image_bunny_2, image_bunny_3, image_bunny_4, image_bunny_5, image_bunny_6,
                image_bunny_7, image_bunny_8]

# list1 = []
# print image_bunny_1
# print pygame.transform.scale(image_bunny_1, (135, 100))
# list1.append(pygame.transform.scale(image_bunny_1, (135, 100)))
# print list1
#
# im_new = []
# im_new.append(pygame.transform.scale(image, (image.get_rect()[2] / 2, image.get_rect()[3] / 2)) for image in bunny_images)
# print im_new

carrot_image = pygame.image.load("cartoon-carrot.png")

Bunny = Player(bunny_images, screen)
Carrot = Item(carrot_image)
Carrot.positions()

while True:
    # --- Main event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()

    Bunny.player_draw(background_image, Carrot)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
quit()