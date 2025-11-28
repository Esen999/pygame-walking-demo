import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 360))#, flags= pygame.NOFRAME
pygame.display.set_caption("Esen The Best")
icon = pygame.image.load("image/Icon.webp")
pygame.display.set_icon(icon)

# square = pygame.Surface((50, 170))
# square.fill('Forest Green')
#
# myfont = pygame.font.Font('fonts/Roboto-BoldItalic.ttf', 40)
# text_surface = myfont.render("AzizDaun", True, "White")

bg = pygame.image.load("image/bg.jpg")
walk_left = [
    pygame.image.load('image/player_left/1670754087.png'),
    pygame.image.load('image/player_left/1670754090.png'),
    pygame.image.load('image/player_left/1670754092.png'),
    pygame.image.load('image/player_left/1670754094.png')
]

walk_right = [
    pygame.image.load('image/player_right/1670754038.png'),
    pygame.image.load('image/player_right/1670754040.png'),
    pygame.image.load('image/player_right/1670754060.png'),
    pygame.image.load('image/player_right/1670754063.png')
]

player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound('sounds/beat.mp3')
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))
    screen.blit(walk_left[player_anim_count], (260, 210))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count +=1

    bg_x -= 2
    if bg_x == -600:
        bg_x = 0


    # pygame.draw.circle(screen, 'Red', (10, 7), 5)
    # screen.blit(square, (10, 0))
    # screen.blit(text_surface, (300, 100))



    # screen.fill(('White'))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_1:
        #         screen.fill((10, 69, 27))

    clock.tick(10)