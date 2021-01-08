import pygame

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("Kmeans visualization");

running = True

clock = pygame.time.Clock();

BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (245,255,230)
WHITE = (255,255,255)

font = pygame.font.SysFont('sans', 40)
text_plus = font.render('+', True, WHITE)

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    # Draw interface
    # Draw panel

    pygame.draw.rect(screen, BLACK, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

    # K button +
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (860,50))

    # End draw interface

    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip();

pygame.quit()
