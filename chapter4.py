import turtle
bob = turtle.Turtle()
bob.speed(-5)
print(bob)

'''2. Write a function called square that takes a parameter named t, which is a turtle.
It should use the turtle to draw a square.'''

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

'''3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.'''
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

'''5. Write a function called circle that takes a turtle, t, and radius, r, as parameters
and that draws an approximate circle by calling polygon with an appropriate
length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.'''
import math
def circle(t, r,):
    length = 1
    n = round(2*math.pi*r)
    polygon(t, length, n)

'''5. Make a more general version of circle called arc that takes an additional
parameter angle, which determines what fraction of a circle to draw. angle is in
units of degrees, so when angle=360, arc should draw a complete circle.'''


def arc(t, r, angle):
    circumference = 2*math.pi*r
    for i in range(round((angle*circumference)/360)):
        t.fd(1)
        t.lt(360/circumference)

def my_circle(t, r):
    arc(t, r, 360)

#circle_arc(bob, 20, 180)
#my_circle(bob, 50)

def petal(t, r, angle):
    angle = 60
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)
def flower (t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)
    t.pu()
    t.home()

def move_1(t, l):
    t.pu()
    t.fd(l)
    t.lt(90)
    t.fd(-l)
    t.pd()

def move_2(t, l):
    t.lt(90)
    t.fd(l)
    t.pd()

def move_3(t, l):
    t.fd(l)
    t.lt(90)
    t.fd(l)
    t.pd()

move_1(bob, -200)
flower(bob, 100, 7, 60)

move_2(bob, 200)
flower(bob, 100, 10, 80)

move_3(bob, 200)
flower(bob, 100, 20, 20)


def one_triangle(t, n, l):
    t.pd
    h = (l/2)/(math.sin(math.radians(180/n))) #the length of sides of the triangle.
    g = (180 + (360/n))/2                     #the angle at each turning.
    t.lt(360/n)
    t.fd(l)
    t.lt(g)
    t.fd(h)
    t.pu()
    t.fd(-h)
    t.rt(g)
    t.pd()

def trianguligon (t, n, l):
    for i in range(n):
        one_triangle(t, n, l)

def move_down(t, l):
    t.pu()
    t.rt(90)
    t.fd(l)
    t.lt(90)

def move (t, l):
    t.pu()
    t.fd(l)
    t.pd()

move_down(bob, 130)
move(bob, -200)
trianguligon(bob, 5, 100)

move(bob, 210)
trianguligon(bob, 6, 100)

move(bob, 240)
trianguligon(bob, 7, 100)

turtle.mainloop()