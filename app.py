import pygame
import os


def start_game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    clock = pygame.time.Clock()
    # info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
    # screen_width,screen_height = info.current_w,info.current_h
    screen = pygame.display.set_mode([800, 600], pygame.FULLSCREEN)
    pygame.display.set_caption('Space Fighter')

    GAME_BACKGROUND = pygame.image.load(
        "resources/bkg/space.jpg")
    GAME_BACKGROUND = pygame.transform.scale(GAME_BACKGROUND, (800, 600))

    SPACESHIP = pygame.image.load("resources/assets/spaceship_1.png")
    SPACESHIP = pygame.transform.scale(SPACESHIP, (50, 50))
    SPACESHIP = pygame.transform.rotate(SPACESHIP, -90)

    EARTH = pygame.image.load("resources/assets/earth.png")
    EARTH = pygame.transform.scale(EARTH, (50, 50))

    UFO = pygame.image.load("resources/assets/ufo.png")
    UFO = pygame.transform.scale(UFO, (50, 50))

    misiles = []
    enemies = [1]

    pos_x = 80
    pos_y = (600 - 50)/2

    running = True
    moving = False
    delta_y = 0
    delta_x = 0

    arrows = [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(misiles) < 3:
                    misiles.append({"x": pos_x + 50, "y": pos_y})
                if event.key in arrows:
                    moving = True
                    if event.key == pygame.K_DOWN:
                        delta_y = 6
                    if event.key == pygame.K_UP:
                        delta_y = -6
                    if event.key == pygame.K_LEFT:
                        delta_x = -6
                    if event.key == pygame.K_RIGHT:
                        delta_x = 6

            elif event.type == pygame.KEYUP:
                if event.key in arrows:
                    moving = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        delta_y = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        delta_x = 0

        if moving:
            if (pos_x > 80 and delta_x < 0) or (pos_x < 800 - 50 and delta_x > 0):
                pos_x = pos_x + delta_x
            if (pos_y > 0 and delta_y < 0) or (pos_y < 600 - 50 and delta_y > 0):
                pos_y = pos_y + delta_y

        screen.blit(GAME_BACKGROUND, (0, 0))
        screen.blit(EARTH, (15, (600-50)/2))

        for enemy in enemies:
            screen.blit(UFO, (700, (600-50)/2))
            for misile in misiles:
                if UFO.get_rect(topleft=(700, (600-50)/2)).colliderect(pygame.Rect(misile["x"], misile["y"], 10, 4)):
                    enemies.remove(enemy)
                    misiles.remove(misile)

        screen.blit(SPACESHIP, (pos_x, pos_y))
        for misile in misiles:
            pygame.draw.rect(screen, (255, 255, 255),
                             (misile["x"], misile["y"] + 23, 10, 4), 2)
            misile["x"] = misile["x"] + 7
            if (misile["x"]) > 800:
                misiles.remove(misile)

        pygame.display.update()

    pygame.quit()


if __name__ != 'main':
    start_game()
