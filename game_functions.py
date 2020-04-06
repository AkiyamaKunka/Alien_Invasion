import sys, pygame

def check_event(ship):
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("kdown")
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                print("w is pressed")
                ship.moving_up = True
            if pressed[pygame.K_s]:
                print("s is pressed")
                ship.moving_down = True
            if pressed[pygame.K_d]:
                ship.moving_right =True
            if pressed[pygame.K_a]:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
           # pressed = pygame.key.get_pressed()
            if event.key == pygame.K_w:
                print("w is pressed")
                ship.moving_up = False
            if event.key == pygame.K_s:
                print("s is pressed")
                ship.moving_down = False
            if event.key == pygame.K_d:
                ship.moving_right = False
            if event.key == pygame.K_a:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
