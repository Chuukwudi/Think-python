'''Exercise 10-1.'''

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

def nested_sum(s):
    total = 0
    for t in s:
        total = add_all(t) + total
    return total


s  = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(s))

'''Exercise 10-2'''
def cumsum(t):
    total = 0
    new = []
    for i in t:
        total = total + i
        new = new + [total]
    print(new)
    return total
t = [1, 2, 3]
cumsum(t)

'''Exercise 10-3'''
def middle(t):
    return t[1:-1]

q = ['a', 'b', 'c', 'd', 'e', 'f']
print(middle(q))

'''Exercise 10-4'''
def chop(t):
    del t[0]
    del t[-1]
    print(t)
chop(q) #even though this prints, it returns none.

'''Exercise10-5'''
def is_sorted(t):
    tt = t[:]
    tt.sort()
    if tt == t[:]:
        return True
    else:
        return False

w = [1, 2, 3, 4]
print(is_sorted(w))

'''Exercise 10-6'''
def is_anagram(word1, word2):
    if len(word1) == len(word2):
        for i in word1:
            if i in word2:
                return True
    else:
        return False
print(is_anagram('spine', 'penis'))

'''Exercise 10-7'''
def has_duplicates(lizt):
    for i in lizt:
        if lizt.count(i) > 1:
            return True
    return False

z = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c']
print(has_duplicates(z))

'''Exercise 10-8'''

def probieren(): #this funtion prints the array
    import random
    lis = []
    for i in range(23):
        bday = random.randint(1, 365)
        lis.append(bday)
    return lis


def probablility(): #this funtion gets the percentage probability.
    nummer = 0
    nummerr = 0
    for i in range(100):
        lis = probieren()
        if has_duplicates(lis) == False:
            nummer += 1
        else:
            nummerr += 1
    print( "%s percent is the probability of having dublicates, while %s is the probability of having none!" % (nummerr, nummer))

print('An example of one of the lists is:\n%s' %probieren() )
probablility()


'''Exercise 10-9.'''

def words_to_list1():
    lesen = open('words.txt')
    full_words = lesen.readlines()
    wordlist = []
    for letters in full_words:
        wordlist.append(letters.strip('\n'))
    return wordlist

def words_to_list2():
    lesen = open('words.txt')
    full_words = lesen.readlines()
    wordlist = []
    for letters in full_words:
        wordlist = wordlist + [letters.strip('\n')]
    return wordlist

#print(words_to_list1())
#print(words_to_list2())

'''"words_t0_list2 takes longer to run. this is because append method updates itself 
while the other funtion continues reassigning'''

'''Exercise 10-10.'''
def in_bisect(liste, suchen):
    liste.sort()
    list1 = liste[ :int(len(liste)/2)]
    list2 = liste[int(len(liste)/2): ]
    if suchen in list1:
        return list1.index(suchen)
    elif suchen in list2:
        return list2.index(suchen)
    else:
        return None

print(in_bisect(z, 'p'))

'''Exercise 10-11'''

def reverse_pair():
    worterbuch = words_to_list1()
    for word in worterbuch:
        if word[::-1] in worterbuch:
            print(word)

#reverse_pair()

'''Exercise 10-12'''

def word1(a): #gets the first word out
    word1 = ''
    r = 0
    for i in range(int((len(a))/2)):
        word1 = word1 + a[r]
        r += 2
    return word1

def word2(a): #gets the second word out
    word2 = ''
    r = 1
    for i in range(int((len(a)) / 2)):
        word2 = word2 + a[r]
        r += 2
    return word2

def interlock():
    worte = words_to_list1()
    for word in worte:
        if len(word) % 2 == 0:
            wor1 = word1(word)
            wor2 = word2(word)
            if wor1 in worte:
                if wor2 in worte:
                    print(word)

interlock()


