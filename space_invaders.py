import turtle
import time
import math
import random

wn = turtle.Screen()
wn.setup(1220, 800)
wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.addshape("invader.gif")
wn.addshape("ship.gif")
turtle.tracer(0, 0)

ship = turtle.Turtle()
ship.shape("ship.gif")
ship.speed(1)
ship.penup()
ship.ht()
ship.sety(-350)
ship.setheading(90)
ship.dx = 0
ship.dy = 0

bullet = turtle.Turtle()
bullet.speed(1)
bullet.color("yellow")
bullet.penup()
bullet.dxy = 0
bullet.setheading(90)
bullet.sety(-330)
bullet.state = 0
bullet.ht()


text = turtle.Turtle()
text.ht()
text.pencolor("white")
text.write("  Başlamak İçin R\n\n Ateş Etmek İçin X", False, "center", font=("Arial", 50, "bold"))


def start():
    text.clear()
    ship.st()
    ship.goto(0, -350)
    global game
    game=1
    if level == 0:
        for e in es:
            e.setx(random.randint(-10, 10) * 40)
            e.sety(350)
            e.st()
    text.write(" \n\n\nBAŞLA!", False, "center", font=("Arial", 50, "bold"))
    time.sleep(1)
    text.clear()


def up():
    if ship.dy < 5:
        ship.dy += 1


def down():
    if ship.dy > -5:
        ship.dy += -1


def left():
    if ship.dx > -5:
        ship.dx += -1


def right():
    if ship.dx < 5:
        ship.dx += 1


def stop():
    ship.dx = 0
    ship.dy = 0


def fire():
    if bullet.state == 0:
        bullet.state = 1
        bullet.sety(ship.ycor() + 10)
        bullet.setx(ship.xcor())
        bullet.dxy = 10
        bullet.st()


def collision(t1, t2,size):
    if math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)) < size:
        t1.ht()
        t2.ht()

        bullet.state = 0
        bullet.dxy = 0


def reset(lvl):
    global es
    bullet.ht()
    ship.goto(0,-350)
    ship.dx=0
    ship.dy=0
    bullet.state = 0
    for e in es:
        e.reset()
        e.ht()
    es = []
    for _ in range(5 + lvl * 3):
        es.append(turtle.Turtle())
        for e in es:
            e.speed(1)
            e.penup()
            e.st()
            e.shape("invader.gif")
            e.shapesize(0.1)
            e.setx(random.randint(-10, 10) * 40)
            e.sety(350 - 100 * random.choice((0, 1, 2)))
            e.dx = 2 * random.choice((-1, 1))

es=[]
game = 0
level = 0
nextlevel = 0

turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(stop, "space")
turtle.onkeypress(fire, "x")
turtle.onkey(start, "r")
reset(0)
while 1:
    time.sleep(0.01)

    if ship.isvisible() == 0 and game==1:
        text.write("              BRAVO\n Yeniden Başlamak İçin R", False, "center", font=("Arial", 50, "bold"))
        level = 0
        reset(0)
        ship.st()
        game=0
    if game:
        if abs(ship.xcor()) <= 600:
            ship.setx(ship.xcor() + ship.dx)
        else:
            ship.setx(600 * ship.xcor() / abs(ship.xcor()))
            ship.dx = 0
        if abs(ship.ycor()) <= 350:
            ship.sety(ship.ycor() + ship.dy)
        else:
            ship.sety(350 * ship.ycor() / abs(ship.ycor()))
            ship.dy = 0

        if bullet.state == 1:
            bullet.forward(bullet.dxy)
            for e in es:
                if e.isvisible():
                    collision(e, bullet,30)
            if bullet.ycor() > 400:
                bullet.state = 0
                bullet.dxy = 0
                bullet.ht()
        nextlevel = 1
        for e in es:
            if e.isvisible():
                collision(e, ship,40)
                if abs(e.xcor()) > 600:
                    e.dx *= -1
                    e.sety(e.ycor() - 100)
                e.setx(e.xcor() + e.dx)
                if e.ycor() < -350:
                    game = 0
                nextlevel = 0
        if nextlevel:
            text.write("  Bölüm " + str(level + 2) + "\n Hazır OL!", False, "center", font=("Arial", 50, "bold"))
            level += 1
            reset(level)
            time.sleep(3)
            text.clear()
            start()
    turtle.update()
turtle.mainloop()