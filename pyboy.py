import pygame, os, math, sys

pygame.init()
pygame.display.set_caption("Pyboy")

WIDTH = 900
HEIGHT = 750
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_gameboy():
    rect1 = pygame.Rect(275, 50, 350, 600)
    rect2 = pygame.Rect(300, 80, 300, 270)
    rect3 = pygame.Rect(325, 105, 240, 210)

    pygame.draw.rect(window, ((197, 190, 188)), rect1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((38, 40, 40)), rect1, 1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((146, 141, 145)), rect2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((114, 109, 111)), rect2, 2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((131, 159, 82)), rect3)
    pygame.draw.rect(window, ((121, 121, 78)), rect3, 1)

def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

        window.fill((255, 255, 255))

        draw_gameboy()

        pygame.display.update()

        if not run:
            print("Exiting...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main(window)
