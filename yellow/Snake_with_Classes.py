import pygame
import random, math, sys
from pygame.locals import *

class Game_Object:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.colour = (6,8,0)
        self.r = 10
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    
    def drawSelf (self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r, 0)
        
    def distance(self, x, y):
        return math.sqrt( (self.x - x)**2 + (self.y - y)**2 )
    
class Head(Game_Object):
    def __init__(self, x, y):
        super().__init__ (x, y)
        self.colour = (8, 102, 6)
        self.dir = 'right'

    def setDir(self, direction):
        self.dir = direction
    
    def move(self):
        if self.dir == 'up':
            self.y -= 20
        elif self.dir == 'down':
            self.y += 20
        elif self.dir == 'right':
            self.x += 20
        elif self.dir == 'left':
            self.x -= 20

class Tail(Game_Object):
    def __init__(self, x, y):
        super().__init__ (x, y)
        self.colour = (4, 53, 3)

class Apple(Game_Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.colour = (255, 51, 0)
        self.eat()

    def eat(self):
        self.x = random.randint(2, screen.get_width() / 100 - 1) * 100
        self.y = random.randint(2, screen.get_height() / 100 - 1) * 100

pygame.init()
screen = pygame.display.set_mode( (400,400) )
pygame.display.set_caption("DigiLocal Snake")
clock = pygame.time.Clock()

snakeSpeed = 4
head = Head(100, 100)  # step 2
apple = Apple(0,0)  # step 3
screen.fill((153, 51, 0))

tail_arr = []

def mainloop():

    for event in pygame.event.get():
        # DBG print(pygame.event.event_name(event.type))
        if event.type == QUIT:
            pygame.display.quit()
            raise SystemExit
        if event.type == KEYDOWN:
            if event.key == K_w:
                head.setDir('up')
            elif event.key == K_s:
                head.setDir('down')
            elif event.key == K_a:
                head.setDir('left')
            elif event.key == K_d:
                head.setDir('right')

    pygame.draw.rect (screen, (204, 102, 0), Rect((10,10), 
                                (screen.get_width()-20, screen.get_height()-20)))
    
    lastX = head.getX()
    lastY = head.getY()
    head.move()
    prevX = head.getX()
    prevY = head.getY()
    if prevX < 0 or prevX > screen.get_width() or prevY < 0 or prevY > screen.get_height():
        tail_arr.clear()    # remove tail
        head.setX(int(screen.get_width()/2))
        head.setY(int(screen.get_height()/2))
    head.drawSelf()     # step 2
    
    apple.drawSelf()    # step 3
    distance = head.distance(apple.getX(), apple.getY())
    if distance == 0:
        apple.eat()
        tail_arr.append(Tail(0,0))  # eat apple, grow tail
    
    for tail in tail_arr:
        prevX = tail.getX()
        prevY = tail.getY()
        tail.setX(lastX)    # move next tail position to previous
        tail.setY(lastY)
        lastX = prevX
        lastY = prevY
        if head.getX() == lastX and head.getY() == lastY:
            tail_arr.clear()    # collide with tail
            break

    for tail in tail_arr:
        tail.drawSelf()
        
    pygame.display.update()
    clock.tick(snakeSpeed + (snakeSpeed * int(len(tail_arr)/5)))        # speed up each time tail is 5 elements longer


def main():
    while True:
      mainloop()

if __name__ == '__main__':
    sys.exit(main())
