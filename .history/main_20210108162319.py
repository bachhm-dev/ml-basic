import pygame

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("Kmeans visualization");

running = True

clock = pygame.time.Clock();

while running:
    clock.tick(60)
