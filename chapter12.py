import time


'''Exercise 12-1.
Write a function called most_frequent that takes a string
and prints the letters in decreasing order of frequency.
Find text samples from several different languages and
see how letter frequency varies between languages.
Compare your results with the'''

def histogram(s):
    """takes strings as argument and returns a dictionary with each character as key and the frequency of appearance as
values"""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

#histogram is a dictionary.
#Now, convert histogram to list of tuples
#sort the list and print
def most_frequent(s):
    freq = histogram(s)
    dictlist = []
    for key, value in freq.items():
        temp = (key, value)
        dictlist.append(temp)
        dictlist.sort(key = lambda x: x[1], reverse= True)
    for letter, frreq in dictlist:
        print(letter, frreq)

most_frequent('iloveyouu ihechi')

#if index one of word in word, append word to list.
def create_dic():
    offen = open('words.txt')
    dictionairy = dict()
    for line in offen:
        word = line.strip('\n')
        dictionairy[word] = None
    return dictionairy

dictio = create_dic()

def finde(word, another_word):
    '''This function checks if two words are perfect anagrams'''
    t = list(another_word)
    if len(word) == len(another_word):
        for i in word:
            if i in t:
                t.remove(i)
            else:
                return False
    else:
        return False
    return True


def find_anagram(word):
    '''This funtion generates a list of anagrams in a text file'''
    anag = []
    for words in dictio:
        if finde(word, words):
                anag.append(words)
    return anag

start = time.time()
def is_anagrams():
    '''Finds all anagrams in the text file'''
    dict1 = {}
    for item in dictio:
        fd = find_anagram(item)
        if len(fd) > 1 and item not in dict1:
            dict1[item] = find_anagram(item)
            '''You can un-comment the line below to see that the code is working'''
            #print(item, find_anagram(item))
    return dict1

#print(is_anagrams())

#f = open("aagram.txt", "w")
#f.write(str(is_anagrams()))
#f.write('Duration: {} seconds'.format(time.time() - start))


def diic():
    offe = open('anagram.txt')

    for line in offe:
        word = line.strip('\n')
        return word

our_dic = eval(diic())

'''Exercise 12-2-2'''
def sort_it():
    for k in sorted(our_dic, key=lambda k: len(our_dic[k]), reverse=True):
        print(k, our_dic[k])
'''Sorry, I noticed something here. I iterated through all the elements in the dictionary while looking for the 
anagrams. I am supposed to rewrite this program such that, elements that appear as values do not get iterated through
a second time. You have to pardon me. I can rewrite the code but it would take so much ime to run and to generate 
another'''

'''Exercise 12-2-3'''
def bingo():
    for thing in sorted(our_dic, key=lambda thing: len(our_dic[thing]), reverse=True):
        if len(thing) == 8:
            print(thing, our_dic[thing])
            break

bingo()


'''Exercise 12-3
In the anagram, if two words resemble themselves completely except in two
letters, it ia a metathesis pair
I will match one word to another and check if their differences  are exactly in 
two letters. I will use the zip function to map these words and then, I will
count the number of differnces in position. it should be exactly 2, not more, 
not less otherwise, It is not a metathesis pair.'''

def position(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    if count == 2:
        return True
    else:
        return False

def methathesis():
    for anagrams in our_dic.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if position(word1, word2):
                    print(word1, word2)

#methathesis()


'''
Exercise 12-4
choose a word
get the length of the word
remove one letter each from the word'''

for letter in ['a', 'i', '']:
    if letter not in dictio:
        dictio[letter] = None


def has_children(word):
    if len(word) <= 1:
        return True
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in dictio:
            print(child)
            return has_children(child)

has_children('complecting')

def is_in():
    dii = list()
    for word in dictio:
        if has_children(word):
            dii.append(word)
    return sorted( dii, key = len, reverse=True)

#
print(is_in())

''' we get 
completing
competing
compting
comping
coping
oping
ping
pig
pi
i
as one of the longest words'''
