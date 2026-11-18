import pygame, os, math, sys

pygame.init()
pygame.display.set_caption("Pyboy")

WIDTH = 900
HEIGHT = 750
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

        window.fill((255, 255, 255))

        pygame.display.update()

        if not run:
            print("Exiting...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main(window)
