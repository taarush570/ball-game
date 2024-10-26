import pgzrun

from random import randint

TITLE="Ball Game"
WIDTH = 600
HEIGHT = 600

R=randint(0,255)
G=randint(0,255)
B=randint(0,255)

CLR = R,G,B

GRAVITY = 2000.0 #pixels per second

class Ball:
    def __init__(self,initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self): #draw function is used to put the things on the screen
        pos= (self.x , self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


ball = Ball(50,100)

def draw():
    screen.clear()
    ball.draw()



pgzrun.go()