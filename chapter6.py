
#As an exercise, write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y.

def compare(x, y):
    if x > y :
        return 1
    elif x == y :
        return 0
    else:
        return -1

print(compare(3, 8))

'''fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci n − 1 + fibonacci n − 2
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        recurse = fibonacci(n-2)
        result = fibonacci(n - 1) - recurse
        return result

fibonacci(6)

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

'''x = 1
y = x + 1
print(c(x, y+3, x+y))'''

#The Ackermann function
def ack(m, n):
    if m == 0:
        return (n + 1)
    elif m > 0 and n == 0:      #if m > 0 and n = 0
        return ack(m-1, 1)
    elif m > 0 and n > 0:       #A m − 1, A m, n − 1 if m > 0 and n > 0 .
        return (ack(m-1, ack(m, n-1)))

print(ack(3,4))



'''1. Type these functions into a file named palindrome.py and test them out. What
happens if you call middle with a string with two letters? One letter? What about
the empty string, which is written '' and contains no letters?
2. Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use the
built-in function len to check the length of a string.'''
n = 0
def first(word):
    return word[n]

def last(word):
    return word[n-1]

def middle(word):
    return word[n + 1 : n - 1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif len(word) == 2 and first(word) == last(word):
        return True
    else:
        if first(word) == last(word) and len(word) > 2:
            return is_palindrome(middle(word))
        else:
            return False

print(is_palindrome(input('Which word are you suspecting to be a palindrome? \n' )))


'''A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a
power of b. Note: you will have to think about the base case.'''
c = 1
def is_power(a, b):
    if a == b:
        print('Yes,it is a power')
    elif a % (b**c) == 0:
        recurse = is_power(a/b**(c+1), b)
        return recurse
    else:
        print ('No, not a power')
is_power(int(input("what power number want you to test? \n")), int(input("What power do you think it is? \n")))

'''The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the
remainder when a is divided by b, then gcd(a, b) = gcd(b, r) . As a base case, we can
use gcd(a, 0) = a.
Write a function called gcd that takes parameters a and b and returns their greatest
common divisor.'''

def gcd(a, b):
    if a == 0 or b == 1:
        return b
    elif a == 1 or b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

print(gcd(int(input("You want me to find the HCF of ")), int(input("and "))))
