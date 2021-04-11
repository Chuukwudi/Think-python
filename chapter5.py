'''1. Write a function named check_fermat that takes four parameters—a, b, c and n
—and checks to see if Fermat’s theorem holds. If n is greater than 2 and
a^n + b^n = c^n'''

def check_femat(a, b, c, n):
    a = int(input('Enter value of a: \n'))
    b = int(input('Enter value of b: \n'))
    c = int(input('Enter value of c: \n'))
    n = int(input('Enter value of n: \n'))
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!”")
        else:
            print("No, that doesn’t work.”!!!")
    else:
        if a ** n + b ** n == c ** n :
            print("Oh! that works")
        else:
            print('Sorry, will not work!')



'''Exercise 5-3.
If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch
long, you will not be able to get the short sticks to meet in the middle. For any three
lengths, there is a simple test to see if it is possible to form a triangle:
If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)
1. Write a function named is_triangle that takes three integers as arguments, and
that prints either “Yes” or “No”, depending on whether you can or cannot form a
triangle from sticks with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them
to integers, and uses is_triangle to check whether sticks with the given lengths
can form a triangle.'''
def is_triangle(d, e, f):
    d = int(input('Enter side 1: \n'))
    e = int(input('Enter side 2: \n'))
    f = int(input('Enter side 3: \n'))
    if d + e < f or d + f < e or e + f < d:
        print("No")
    else:
        print("Yes")

#check_femat(a, b, c, n)
is_triangle(5,6,7)

import turtle
bob = turtle.Turtle()
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

#draw (bob, 20, 5)