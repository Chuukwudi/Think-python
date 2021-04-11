# Exercise 9-1
"""Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace)."""


def look():
    fin = open('words.txt')
    for word in look:
        if len(word) > 20:
            print(word)


"""
Exercise 9-2

Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it.
Modify your program from the previous section to print only the words that have no
“e” and compute the percentage of the words in the list that have no “e”.
"""


def hass_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


# print(has_no_e(input("\nEnter the word you wish to check if it has no 'e' here: \n")))


def look_has_no_e():
    look = open('words.txt')
    for word in look:
        if hass_no_e(word):
            print(word)


# or


look = open('words.txt')
# lets get total number of words in the text file.

count_line = 0
for line in look:
    count_line += 1
a = count_line  # total number of words in the text file.
print(a)

look = open('words.txt')


def has_no_e():
    count_e = 0
    for line in look:
        if 'e' not in line:
            print(line)
            count_e += 1
    print(count_e)
    perc = count_e * 100 / a
    print('words without e is ' + str(round(perc, 2)) + '%')


#has_no_e()

'''Exercise 9-3
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and
then print the number of words that don’t contain any of them. Can you find a combination
of five forbidden letters that excludes the smallest number of words?'''


def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True


# print(avoids('wording', 'qqqqqq'))

def look_avoid(forbidden):
    look = open('words.txt')
    for word in look:
        if avoids(word, forbidden):
            print(word)
    return


# look_avoid('ationbcdef')

'''Exercise 9-4
Write a function named uses_only that takes a word and a string of letters, and that
returns True if the word contains only letters in the list. Can you make a sentence
using only the letters acefhlo? Other than “Hoe alfalfa?”'''

#first solution
def uses_only(word, available):
    for i in range(len(word)):
        if not word[i] in available:
            return False
    return True


def words_from(initial):
    look = open('words.txt')
    full_words = look.readlines()
    for letters in full_words:
        if uses_only(letters.strip('\n'), initial):
            print(letters)

#second solution:
def uses_onlyy(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True




#print(uses_onlyy('door', 'drosr'))


def word_from(word):
    look = open('words.txt')
    whole = look.readlines()
    for words in whole:
        if uses_onlyy(words.strip('\n'), word):
            print(words)

#appears_once('ade')






#word_from('acefhlo')

'''if letters in word is part of aceflo
    print letters'''

'''Exercise 9-5.
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many
words are there that use all the vowels aeiou? How about aeiouy?'''


def uses_all(word, required):
    return uses_only(required, word)

print(uses_all('window', 'wind'))


def make_sentence_fromm(wordd):
    look = open('words.txt')
    whole = look.readlines()
    for word in whole:
        if uses_all(word.strip('\n'), wordd):
            print(word)

#make_sentence_fromm('aeiou')
'''Exercise 9-6.
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many
words are there that use all the vowels aeiou? How about aeiouy?'''


def is_abcedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1
    return True

#print(is_abcedarian('acde'))


#Exercise 9-7.

def double_consecutive(word):
    for i in range(len(word)-5):
        if word[i] == word[1 + i] and word[2 + i] == word[3 + i] and word[4 + i] == word[5 + i] and len(word) >= 6:
            return True
        i += 1
    else:
        return False
#

def check_3_double_consecutive():
    look = open('words.txt')
    whole = look.readlines()
    for word in whole:
        if len(word) >= 6:
            if double_consecutive(word.strip('\n')):
                print(word)

#print(double_consecutive('eryyttrryu'))
#check_3_double_consecutive()

def is_palindrome(word):
    if word[ : :-1] == word:
        return True
    else:
        return False

def find_number():
    x = 100000
    print('what the man first saw on his odometer must have been either of the following numbers:')
    for u in range(999999-400000):
        x += 1
        b = str(x)
        if is_palindrome(b[2:6]):
            x += 1
            b = str(x)
            if is_palindrome(b[1:6]):
                x += 1
                b = str(x)
                if is_palindrome(b[1:5]):
                    x += 1
                    b = str(x)
                    if is_palindrome(b[0:6]):
                        print(x - 3)
    x += u

find_number()


def find_age(girl, mom):
    print('The woman gave birth at ' + str(mom - girl) + '.')
    if str(girl)[::-1] != str(mom):
        print('Age of mum should be the reverse of age of girl')
    for i in range(200):
        if str(girl + i)[::-1] == str(mom + i):
            print(girl + i, mom + i)


find_age(12, 21)
'''This last question forces one to make an assumption.  :(