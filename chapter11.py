
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    return d

print(histogram('assdddffffggggg'))

'''Exercise 11-1'''
def create_dic():
    offen = open('words.txt')
    counter = 0
    dictionairy = {}
    for line in offen:
        word = line.strip('\n')
        dictionairy[word] = counter
        counter += 1
    return dictionairy

#print(create_dic())

'''Exercise 11-2'''
def invert_dict(s):
    worter = {}
    for key in s:
        v = s[key]
        worter.setdefault(v, []).append(key)
    return worter

'''Exercise 11-3'''
#The Ackermann function
#Ransom, please, d
def ack(m, n):
    known = {0: n + 1}
    know = {}
    if m in known:
        return known[m]
    elif m > 0 and n == 0:      #if m > 0 and n = 0
        return ack(m-1, 1)
    elif m > 0 and n > 0:       #A m − 1, A m, n − 1 if m > 0 and n > 0 .
        return (ack(m-1, ack(m, n-1)))

print(ack(3,4))

'''Exercise 11-4'''
def has_duplicates(t):
    d = {}
    for thing in t:
        if thing in d:
            return True
        d[thing] = "rubbish"
    return False

z = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c']

print(has_duplicates(z))

'''Exercise 11-5'''
def rotate_letter(letter, rotation):
    letter = letter.lower()
    c = ord(letter) - ord('a') #finds the position of the letter in the alphabet
    i = (c + rotation) % 26 + ord('a') #adds the position of this letter to the initial letter. wonderful algorithm!
    return chr(i)

def rotate_word(word, rotation):
    result = ''
    for letter in word:
        result += rotate_letter(letter, rotation)
    return result

'''to solve this problem, I will create 2 dictionaries with the 
rotated words as key and another with the dictionary words as key.
if any word in the rotated in words, print that word'''

def rotate_pair(rotation):
    offen = open('words.txt')
    dicta = {}
    for line in offen:
        word = line.strip('\n')
        dicta[rotate_word(word, rotation)] = word
    return dicta


def rotate_pair_check(rotation):
    rodict = rotate_pair(rotation)
    for key in rodict:
        if key in create_dic():
            print('"' + rotate_word(key, -(rotation)) + '" is the word and when rotated by ' + str(rotation) + ' we have "' + key + '".')


#print(rotate_word('nowhere', -13))
#print(rotate_pair(-13))
#rotate_pair_check(13) #very slow!!!

'''Exercise 11-6
Create a dictionary of 5 letter words from the word.txt with keys
eliminating their first letter and their values, the as thw word itself.'''

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue
        t = line.split()
        word = t[0].lower()
        pron = t[1:]
        d[word] = pron

    return d

def do_it():
    dictionari = read_dictionary()
    for key in dictionari:
        if key[1:] in dictionari:
            if len(key) == 5:
                if dictionari[key] == dictionari[key[1:]]:
                    print(key)

do_it()