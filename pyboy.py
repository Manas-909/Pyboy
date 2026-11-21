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

    rect4 = pygame.Rect(410, 360, 8, 55)
    rect5 = pygame.Rect(390, 345, 8, 55)
    rect6 = pygame.Rect(430, 370, 8, 55)
    rect7 = pygame.Rect(450, 380, 8, 55)

    font = pygame.font.SysFont("Arial Black", 40)
    branding = font.render("Pyboy", True, ((27, 19, 56)))

    speaker = pygame.Surface((900, 800), pygame.SRCALPHA)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect4, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect5, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect6, border_radius=6)
    pygame.draw.rect(speaker, ((114, 109, 111)), rect7, border_radius=6)

    rotated_speaker = pygame.transform.rotate(speaker, 60)

    pygame.draw.rect(window, ((197, 190, 188)), rect1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((38, 40, 40)), rect1, 1, border_radius=15, border_bottom_right_radius=95)
    pygame.draw.rect(window, ((146, 141, 145)), rect2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((114, 109, 111)), rect2, 2, border_radius=15, border_bottom_right_radius=60)
    pygame.draw.rect(window, ((131, 159, 82)), rect3)
    pygame.draw.rect(window, ((121, 121, 78)), rect3, 1)

    rect = rotated_speaker.get_rect()

    window.blit(rotated_speaker, rect)
    window.blit(branding, (320, 570))

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

SCREEN = pygame.Rect(325, 105, 240, 210)

class Snake():
    def __init__(self):
        self.head = pygame.Rect(435, 200, 20, 20)
        self.move_speed = 3
        self.direction = "right"

    def snake_direction(self, btn_down):
        if "btn_w" in btn_down and self.direction != "down":
            self.direction = "up"
        elif "btn_s" in btn_down and self.direction != "up":
            self.direction = "down"
        elif "btn_d" in btn_down and self.direction != "left":
            self.direction = "right"
        elif "btn_a" in btn_down and self.direction != "right":
            self.direction = "left"

    def move_snake(self):
        lost = False

        if self.head.right >= SCREEN.right or self.head.left <= SCREEN.left or self.head.top <= SCREEN.top or self.head.bottom >= SCREEN.bottom:
            lost = True

        if self.direction == "up" and not lost:
            self.head.y -= self.move_speed
        elif self.direction == "right" and not lost:
            self.head.x += self.move_speed
        elif self.direction == "left" and not lost:
            self.head.x -= self.move_speed
        elif self.direction == "down" and not lost:
            self.head.y += self.move_speed


    def draw_snake(self):
        pygame.draw.rect(window, ((198, 192, 189)), self.head)
        pygame.draw.rect(window, ((20, 20, 20)), self.head, 1)


class Ball():
    def __init__(self):
        self.x = SCREEN.centerx
        self.y = SCREEN.centery
        self.radius = 10
        self.rect = pygame.Rect(self.x - 10, self.y - 10, 20, 20)
        self.ball_speed_x = 2
        self.ball_speed_y = -2

    def draw_ball(self):
        pygame.draw.circle(window, ((198, 192, 189)), (self.x, self.y), self.radius)
        pygame.draw.circle(window, ((20, 20, 20)), (self.x, self.y), self.radius, 1)

    def move_ball(self, wall, opp):
        if self.rect.top < SCREEN.bottom:
            self.x += self.ball_speed_x
            self.y += self.ball_speed_y

            self.rect.centerx = int(self.x)
            self.rect.centery = int(self.y)

            if self.rect.left <= SCREEN.left:
                self.rect.left = SCREEN.left
                self.x = self.rect.centerx
                self.ball_speed_x = abs(self.ball_speed_x)

            if self.rect.right >= SCREEN.right:
                self.rect.right = SCREEN.right
                self.x = self.rect.centerx
                self.ball_speed_x = -abs(self.ball_speed_x)

            if self.rect.colliderect(wall.rect):
                if self.ball_speed_y > 0:
                    self.rect.bottom = wall.rect.top
                else:
                    self.rect.top = wall.rect.bottom
                self.ball_speed_y *= -1

            if self.rect.colliderect(opp.rect):
                if self.ball_speed_y < 0:
                    self.rect.top = opp.rect.bottom
                else:
                    self.rect.bottom = opp.rect.top
                self.ball_speed_y *= -1

            self.x = self.rect.centerx
            self.y = self.rect.centery
            

class Wall():
    def __init__(self):
        self.x = 400
        self.y = 304
        self.width = 50
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_speed = 3

    def draw_wall(self):
        pygame.draw.rect(window, ((198, 192, 189)), self.rect)
        pygame.draw.rect(window, ((20, 20, 20)), self.rect, 1)

    def move_player(self, btn_down, ball):
        if ball.rect.top < SCREEN.bottom:
            if "btn_a" in btn_down and self.rect.left - 5 > SCREEN.left:
                self.rect.x -= self.move_speed
            elif "btn_d" in btn_down and self.rect.right + 5 < SCREEN.right:
                self.rect.x += self.move_speed

class Opponent_wall():
    def __init__(self):
        self.x = 400
        self.y = 106
        self.width = 50
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.move_speed = 4

    def move_opp(self, ball):
        if ball.x > self.rect.centerx and self.rect.right + 5 < SCREEN.right:
            self.x += self.move_speed
            self.rect.x += self.move_speed
        elif ball.x < self.rect.centerx and self.rect.left - 5 > SCREEN.left:
            self.x -= self.move_speed
            self.rect.x -= self.move_speed
        

    def draw_opp(self):
        pygame.draw.rect(window, ((198, 192, 189)), self.rect)
        pygame.draw.rect(window, ((20, 20, 20)), self.rect, 1)
        


def play_pong(wall, opp, ball, btn_down):
    wall.move_player(btn_down, ball)
    wall.draw_wall()

    opp.move_opp(ball)
    opp.draw_opp()

    ball.draw_ball()
    ball.move_ball(wall, opp)


def play_snake(snake, btn_down):
    snake.snake_direction(btn_down)
    snake.move_snake()
    snake.draw_snake()



def main(window):
    clock = pygame.time.Clock()
    btn_down = set()
    run = True

    game_selected = False
    game_list = ["pong", "snake"]
    cur_game = 0
    game_choice = None

    font_option1 = pygame.font.SysFont("Comic Sans MS", 30)
    font_option2 = pygame.font.SysFont("Comic Sans MS", 11)
    text1 = font_option1.render("Pong", True, ((198, 192, 189)))
    text2 = font_option1.render("Snake", True, ((198, 192, 189)))

    info_text1 = font_option2.render("1. Use WASD to control", True, ((37, 34, 35)))
    info_text2 = font_option2.render("2. Use Space to enter and ESC to quit", True, ((37, 34, 35)))

    btn_text1 =  font_option2.render("SPACE", True, ((37, 34, 35)))
    btn_text2 =  font_option2.render("ESC", True, ((37, 34, 35)))

    game_text = font_option1.render("GAME OVER", True, ((198, 192, 189)))

    next_text = font_option2.render("D: Next >>        << Previous :A", True, ((198, 192, 189)))

    text_pos = (410, 195)
    opt_list = [text1, text2]

    wall = Wall()
    ball = Ball()
    opp = Opponent_wall()

    snake = Snake()

    info_rect = pygame.Rect(20, 550, 220, 50)

    while run:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    btn_down.add("btn_w")
                elif events.key == pygame.K_s:
                    btn_down.add("btn_s")
                elif events.key == pygame.K_a:
                    btn_down.add("btn_a")
                elif events.key == pygame.K_d:
                    btn_down.add("btn_d")
                elif events.key == pygame.K_SPACE:
                    btn_down.add("btn_spc")
                elif events.key == pygame.K_ESCAPE:
                    btn_down.add("btn_esc")

            elif events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    btn_down.discard("btn_w")
                elif events.key == pygame.K_s:
                    btn_down.discard("btn_s")
                elif events.key == pygame.K_a:
                    btn_down.discard("btn_a")
                    if not game_selected:
                        cur_game -= 1
                        if cur_game < 0:
                            cur_game = len(game_list) - 1

                elif events.key == pygame.K_d:
                    btn_down.discard("btn_d")
                    if not game_selected:
                        cur_game += 1
                        if cur_game >= len(game_list):
                            cur_game = 0
                elif events.key == pygame.K_SPACE:
                    btn_down.discard("btn_spc")
                    if not game_selected:
                        game_selected = True
                        game_choice =  game_list[cur_game]

                elif events.key == pygame.K_ESCAPE:
                    btn_down.discard("btn_esc")
                    if game_selected:
                        if game_choice == "pong":
                            ball.x, ball.y = SCREEN.centerx, SCREEN.centery
                            ball.rect.x, ball.rect.y = SCREEN.centerx, SCREEN.centery
                            ball.ball_speed_x, ball.ball_speed_y = 2, -2

                            opp.x, opp.y = 400, 106
                            wall.x, wall.y = 400, 304

                        if game_choice == "snake":
                            snake.head.x, snake.head.y = 435, 200
                        
                        game_selected = False
                        game_choice = None
                        cur_game = 0

        window.fill((255, 255, 255))
        pygame.draw.rect(window, ((0,0,0)), info_rect, 1, 10)

        draw_gameboy()
        draw_btn(btn_down)

        if ball.rect.top >= SCREEN.bottom:
            window.blit(game_text, (360, 195))

        if snake.head.right >= SCREEN.right:
            window.blit(game_text, (360, 195))
        elif snake.head.left <= SCREEN.left:
            window.blit(game_text, (360, 195))
        elif snake.head.top <= SCREEN.top:
            window.blit(game_text, (360, 195))
        elif snake.head.bottom >= SCREEN.bottom:
            window.blit(game_text, (360, 195)) 

        window.blit(info_text1, (30, 560))
        window.blit(info_text2, (30, 575))
        
        window.blit(btn_text1, (485, 480))
        window.blit(btn_text2, (545, 450))

        if not game_selected:
            window.blit(opt_list[cur_game], text_pos)
            window.blit(next_text, (380, 290))
        if game_selected:
            window.set_clip(SCREEN)
            if game_choice == "pong":
                play_pong(wall, opp, ball, btn_down)
            elif game_choice == "snake":
                play_snake(snake, btn_down)
            window.set_clip(None)

        pygame.display.update()

        if not run:
            print("Exiting...")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main(window)
