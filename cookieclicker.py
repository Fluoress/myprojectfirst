import random
import pygame
import time
pygame.init()
class Cookie:
    def __init__(self, x,  y, w, h, filename):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])
    def set_picture(self, picture):
        self.image = pygame.image.load(picture)
a = 200
b = 200
c = 100
d = 200
cookie = Cookie(a, b, 50, 50, "pixil-frame-0.png")
cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
fps = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
score_counter = 0#counter
lastChanges = time.time()
startTime = time.time()
timer = int(time.time()-startTime)
timeText = pygame.font.Font(None, 56).render("Час: " + str(timer), True, (0, 0, 0))
background = pygame.image.load("pixil-frame-0 (8).png")
background = pygame.transform.scale(background, (1000, 800))
scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
loseText = pygame.font.Font(None, 25).render("Ти програв! Автор гри: Волкова Вікторія", True, (0,0,0))
winText = pygame.font.Font(None, 25).render("Ти виграв! Автор гри: Волкова Вікторія", True, (0,0,0))
while True:
    timer = int(time.time()-startTime)
    timeText = pygame.font.Font(None, 56).render("Час: " + str(timer), True, (0, 0, 0))
    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
    winText = pygame.font.Font(None, 25).render("Ти виграв! Автор гри: Волкова Вікторія", True, (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if cookie.rect.collidepoint(x, y):
                a = random.randint(0, 300)
                b = random.randint(0, 300)
                c = random.randint(0, 300)
                d = random.randint(0, 300)
                if score_counter >= 10 and score_counter < 40:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (4).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
                    score_counter = score_counter + 2
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                elif score_counter >= 40 and score_counter < 70:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (5).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
                    score_counter = score_counter + 3
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                elif score_counter >= 70:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (6).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
                    score_counter = score_counter + 4
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                else:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0.png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
                    score_counter = score_counter + 1
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
            elif cookie2.rect.collidepoint(x, y):
                a = random.randint(0, 200)
                b = random.randint(0, 200)
                c = random.randint(0, 200)
                d = random.randint(0, 200)
                if score_counter >= 10 and score_counter < 40:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (4).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (4).png")
                    score_counter = score_counter - 2
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                elif score_counter >= 40 and score_counter < 70:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (5).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (5).png")
                    score_counter = score_counter - 3
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                elif score_counter >= 70:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0 (6).png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (6).png")
                    score_counter = score_counter - 4
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
                else:
                    cookie = Cookie(a, b, 50, 50, "pixil-frame-0.png")
                    cookie2 = Cookie(c, d, 50, 50, "pixil-frame-0 (1).png")
                    score_counter = score_counter - 1
                    scoreText = pygame.font.Font(None, 56).render("Очки " + str(score_counter), True, (0, 0, 0))
    if score_counter >= 100:
        screen.fill((0, 250, 0))
        screen.blit(winText, [100,100])
        pygame.display.flip()
        break
    if timer >= 60:
        screen.fill((250, 0, 0))
        screen.blit(loseText, [100,100])
        pygame.display.flip()
        break
    if score_counter < 0:
        screen.fill((250, 0, 0))
        screen.blit(loseText, [100,100])
        pygame.display.flip()
        break
    screen.blit(background, (0, 0))
    cookie.draw(screen)
    cookie2.draw(screen)
    screen.blit(timeText, (10, 10))
    screen.blit(scoreText, (200, 10))
    pygame.display.flip()
    fps.tick(30)
