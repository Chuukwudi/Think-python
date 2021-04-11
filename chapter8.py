'''As an exercise, write a function that takes a string as an argument and displays the
letters backward, one per line.'''

def reverse():
    i = -1
    word = input('What word do you want to reverse?: \n')
    while -len(word) <= i:
        print(word[i], end='')
        i -= 1
reverse()

'''Exercise 8-2'''
#s.count(x) counts the number of times 'x' appears in s
def count():
    word = input('\nInput the word/sentence you want to count the letter from: \n')
    letter = input('what letter do you want to count?: \n')
    print('"' + letter + '" ' + 'appears ' + str(word.count(letter)) + ' times.')

count()


'''Exercise 8-3.'''
def is_palindrome():
    word = str(input('\nEnter the word you suspect to be a palindrome here: \n'))
    if word[ : :-1] == word:
        return True
    else:
        return False

print(is_palindrome())

'''Exercise 8-5'''
def rotate_word(string, rotation):
    string = string.lower()
    for letters in string:
        c = ord(letters) - ord('a') #finds the position of the letter in the alphabet
        i = (c + rotation) % 26 + ord('a') #adds the position of this letter to the initial letter. wonderful algorithm!
        print(chr(i), end='', )
    print('')

rotate_word('cheer', 7)
rotate_word('melon', -10)
rotate_word('sleep', 9)

