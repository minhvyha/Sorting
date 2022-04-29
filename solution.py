import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 700

FONT_BIG = pygame.font.SysFont('comicsans', 40)
FONT_MEDIUM = pygame.font.SysFont('comicsans', 30)
FONT_SMALL = pygame.font.SysFont('comicsans', 20)


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting')

LIGHT_BLUE = (64,224,208)
BLUE = (41,41,64)
DARK_BLUE = (15,15,38)
BLACK_BLUE = (5,5,28)
RED =  (255, 10 ,10)
GREEN = (10, 255, 10)
WHITE = (255, 255, 255)

NUM_BAR = 125

SPACE = (WIDTH - 40) //  NUM_BAR

BAR_WIDTH, BAR_HEIGHT = SPACE - 2, 3.5

BORDER = 25

FPS = 80

RUN = True

DOWN = 25

class Bar:


    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = LIGHT_BLUE
        self.value = value

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def check(self):
        self.color = RED

    def done(self):
        self.color = GREEN

def main(win):
    clock = pygame.time.Clock()
    sort = [x for x in range(1,NUM_BAR + 2)]
    random.shuffle(sort)
    bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i], sort[i]) for i in range(NUM_BAR)]
    name = FONT_MEDIUM.render('Minh Vy Ha', 1, WHITE)
    project = FONT_BIG.render('SORTING', 1, WHITE)
    sorting = [FONT_SMALL.render('1. Selection Sort', 1, WHITE),
               FONT_SMALL.render('2. Bubble Sort', 1, WHITE),
               FONT_SMALL.render('3. Merge Sort', 1, WHITE),
               FONT_SMALL.render('4. Quick Sort', 1, WHITE),
               FONT_SMALL.render('5. Heap Sort', 1, WHITE),
               FONT_SMALL.render('6. Insertion Sort', 1, WHITE)]
    reset = FONT_SMALL.render('0. Reset', 1, WHITE)
    global RUN
    while RUN:
        clock.tick(FPS)
        draw(win, bar, name, project, sorting, reset)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            selection(bar,win, name, project, sorting, reset)
    pygame.quit()

def draw(win, bar, name, project, sorting, reset):
    win.fill(BLUE)
    pygame.draw.rect(win, DARK_BLUE, (0, 0, 800, 180))
    win.blit(project, (30, 20))
    win.blit(name, (40, 90))
    pygame.draw.rect(win, BLUE,(250, 15, 5, 150))
    for i in range(len(sorting)):
        win.blit(sorting[i], (270, 13 + (25 * i)))
    win.blit(reset, (460, 13))
    for i in bar:
        i.draw(win)

    pygame.display.update()

def selection(bar,win, name, project, sorting, reset):
    pygame.init()
    global RUN
    for i in range(len(bar) - 1):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        pygame.time.delay(100)
        draw(win, bar, name, project, sorting, reset)
        min = i
        for u in range(i + 1,len(bar)):

            if bar[u].y > bar[min].y:
                min = u
        temp = bar[min]
        x = temp.x
        bar[min].x = bar[i].x
        bar[i].x = x
        bar[min] = bar[i]
        bar[i] = temp

def display(bar):
    for i in bar:

        print(i.x, i.y)
if __name__ == "__main__":
  main(win)
