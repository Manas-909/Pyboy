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
    rect4 = pygame.Rect(410, 330, 8, 55)
    rect5 = pygame.Rect(390, 310, 8, 75)
    rect6 = pygame.Rect(430, 350, 8, 35)
    rect7 = pygame.Rect(370, 290, 8, 95)

    speaker = pygame.Surface((900, 800), pygame.SRCALPHA)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect4, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect5, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect6, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect7, border_radius=6)

    rotated_speaker = pygame.transform.rotate(speaker, 40)

    pygame.draw.rect(window, ((197, 190, 188)), rect1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((38, 40, 40)), rect1, 1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((146, 141, 145)), rect2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((114, 109, 111)), rect2, 2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((131, 159, 82)), rect3)
    pygame.draw.rect(window, ((121, 121, 78)), rect3, 1)

    rect = rotated_speaker.get_rect()

    window.blit(rotated_speaker, rect)

def draw_btn(btn_down):
    btn_1 = pygame.Rect(355, 380, 35, 60)
    btn_2 = pygame.Rect(355, 430, 35, 60)
    btn_3 = pygame.Rect(355, 420, 70, 35)
    btn_4 = pygame.Rect(320, 420, 70, 35)


    if "btn_w" in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_1.scale_by(0.9))
    elif "btn_w" not in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_1)

    if "btn_s" in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_2.scale_by(0.9))
    elif "btn_s" not in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_2)

    if "btn_d" in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_3.scale_by(0.9))
    elif "btn_d" not in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_3)

    if "btn_a" in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_4.scale_by(0.9))
    elif "btn_a" not in btn_down:
        pygame.draw.rect(window, ((39, 42, 41)), btn_4)

    if "btn_spc" in btn_down:
        pygame.draw.circle(window, ((156, 36, 90)), (500, 450), 20)
        pygame.draw.circle(window, ((40, 40, 40)), (500, 450), 20, 1)
    elif "btn_spc" not in btn_down:
        pygame.draw.circle(window, ((156, 36, 90)), (500, 450), 25)
        pygame.draw.circle(window, ((40, 40, 40)), (500, 450), 25, 1)

    if "btn_esc" in btn_down:
        pygame.draw.circle(window, ((156, 36, 90)), (550, 420), 20)
        pygame.draw.circle(window, ((40, 40, 40)), (550, 420), 20, 1)
    elif "btn_esc" not in btn_down:
        pygame.draw.circle(window, ((156, 36, 90)), (550, 420), 25)
        pygame.draw.circle(window, ((40, 40, 40)), (550, 420), 25, 1)

    


def main(window):
    clock = pygame.time.Clock()
    btn_down = []
    run = True

    while run:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    btn_down.append("btn_w")
                elif events.key == pygame.K_s:
                    btn_down.append("btn_s")
                elif events.key == pygame.K_a:
                    btn_down.append("btn_a")
                elif events.key == pygame.K_d:
                    btn_down.append("btn_d")
                elif events.key == pygame.K_SPACE:
                    btn_down.append("btn_spc")
                elif events.key == pygame.K_ESCAPE:
                    btn_down.append("btn_esc")

            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    btn_down.remove("btn_w")
                elif events.key == pygame.K_s:
                    btn_down.remove("btn_s")
                elif events.key == pygame.K_a:
                    btn_down.remove("btn_a")
                elif events.key == pygame.K_d:
                    btn_down.remove("btn_d")
                elif events.key == pygame.K_SPACE:
                    btn_down.remove("btn_spc")
                elif events.key == pygame.K_ESCAPE:
                    btn_down.remove("btn_esc")


        window.fill((255, 255, 255))

        draw_gameboy()
        draw_btn(btn_down)

        pygame.display.update()

        if not run:
            print("Exiting...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main(window)
