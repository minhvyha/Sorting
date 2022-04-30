import pygame
import random
import copy
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
L_BLUE = (20, 20, 255)

NUM_BAR = 165
BORDER = 25

SORTED = False

SPACE = (WIDTH - 25 - BORDER) / NUM_BAR

BAR_WIDTH, BAR_HEIGHT = SPACE - 1.3, 2.945


FPS = 80

RUN = True

DOWN = 25

COUNT = 0

class Bar:


    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = LIGHT_BLUE
        self.value = value

    def reset(self, num):
        self.x = BORDER + num * SPACE
        return self

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def check(self):
        self.color = RED

    def done(self):
        self.color = GREEN

    def match(self):
        self.color = L_BLUE

    def back(self):
        self.color = LIGHT_BLUE

sort = [x for x in range(1, NUM_BAR + 2)]
random.shuffle(sort)
bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i], sort[i]) for i in range(NUM_BAR)]

def main(win):
    clock = pygame.time.Clock()
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
    global bar

    while RUN:
        clock.tick(FPS)
        draw(win, bar, name, project, sorting, reset)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            random.shuffle(sort)
            bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])), BAR_WIDTH, BAR_HEIGHT * sort[i],
                       sort[i]) for i in range(NUM_BAR)]
        if keys[pygame.K_1]:
            selection(bar,win, name, project, sorting, reset)
        if keys[pygame.K_2]:
            bubble(bar,win, name, project, sorting, reset)
        if keys[pygame.K_3]:
            merge_sort(bar, 0, len(bar) - 1, win, name, project, sorting, reset)
            display(bar)

    pygame.quit()

def draw(win, bar, name, project, sorting, reset, right=None):
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
    if right:
        for i in right:
            i.draw(win)

    pygame.display.update()

def selection(bar,win, name, project, sorting, reset):
    global RUN
    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        min = i
        for u in range(i + 1,len(bar)):
            bar[min].match()
            bar[u].check()
            draw(win, bar, name, project, sorting, reset)
            if bar[u].y > bar[min].y:
                bar[min].back()
                min = u
            if u != i + 1:
                bar[u - 1].back()
        bar[len(bar) - 1].back()
        temp = bar[min]
        bar[min] = bar[i]
        bar[i] = temp
        bar[min].reset(min)
        bar[i].reset(i).done()

def bubble(bar, win, name, project, sorting, reset):
    global RUN
    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        for j in range(len(bar) - 1 - i):
            if j != 0:
                bar[j - 1].back()
            bar[j].check()
            draw(win, bar, name, project, sorting, reset)
            if bar[j].value > bar[j + 1].value:
                temp = bar[j]
                bar[j] = bar[j + 1]
                bar[j + 1] = temp
                bar[j].reset(j)
                bar[j + 1].reset(j + 1)

        bar[len(bar) - 1 - i].done()

def merge(bar, left, mid, right, win, name, project, sorting, reset):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        bar[i].check()
        bar[j].check()
        draw(win, bar, name, project, sorting, reset)
        bar[i].back()
        bar[j].back()
        if bar[i].value < bar[j].value:
            temp.append(bar[i])
            i += 1
        else:
            temp.append(bar[j])
            j += 1
    while i <= mid:
        bar[i].check()
        draw(win, bar, name, project, sorting, reset)
        bar[i].back()
        temp.append(bar[i])
        i += 1
    while j <= right:
        bar[j].check()
        draw(win, bar, name, project, sorting, reset)
        bar[j].back()
        temp.append(bar[j])
        j += 1
    k = 0
    for i in range(left, right + 1):
        bar[i] = temp[k]
        bar[i].reset(i)
        bar[i].check()
        draw(win, bar, name, project, sorting, reset)
        if right - left == len(bar) - 1:
            bar[i].done()
        else:
            bar[i].back()



        k += 1


def merge_sort(bar, left, right, win, name, project, sorting, reset):
    mid = left + (right - left) // 2
    if left < right:
        merge_sort(bar, left, mid, win, name, project, sorting, reset)
        merge_sort(bar, mid + 1, right, win, name, project, sorting, reset)
        merge(bar, left, mid, right, win, name, project, sorting, reset)



def display(bar):
    for i in bar:
        print(i.x, i.y)

if __name__ == "__main__":
  main(win)
