
'''Exercise 7-1'''

def mysqrt(a):
    x = a/2
    epsilon = 0.0001
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

#print(mysqrt(2))
import math
def pringt(a):
    for i in range (10):
        print(a, end="      ")
        print(mysqrt(a), end="      ")
        root = math.sqrt(a)
        print(root, end="        ")
        diff = abs(mysqrt(a) - root)
        print(diff)
        a = a + 1

pringt(1)

'''Exercise 7-2'''
'''Write a function called eval_loop that iteratively prompts the user, takes the resulting
input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last
expression it evaluated.'''

def eval_loop():
    while True:
        a = input('Enter what you wish to evaluate here: \n')
        if a == 'done':
            print(a)
            break
        else:
            print(eval(a))
    return

eval_loop()

'''Exercise 7-3'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

#print(factorial(100))

def estimate_pi_inverse():
    k = 0
    y = (factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k) ** 4) * 396 ** (4 * k))
    while y < 1e-15:
        k = k + 1
    return ((2*math.sqrt(2)) * y)/9801

print(1/(estimate_pi_inverse()))
print(math.pi)