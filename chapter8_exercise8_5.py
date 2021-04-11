'''
str.islower()
Return True if all cased characters in the string are lowercase and there is at least one cased character,
False otherwise.
'''


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


'''Here, the funtion takes the first character, if it is Upper case,
it returns false, if it is lower case, it returns true. it does not iterate over other characters in the string s'''


# -----------------------------------------------------------------------------------------------------------------------

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


'''this function checks only the string 'c' is lower, which always returns True'''


# -----------------------------------------------------------------------------------------------------------------------

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


'''This would have been a nice code except that it only returns after iterating completly.
 Hence, the output is based on the last letter of the string you're checking, it ignores the state of other characters
 but only return its last check '''


# -----------------------------------------------------------------------------------------------------------------------

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


'''This is the perfect code. During the iteration, once a lowercase is met, the flag changes to True.
if another lower case is met, c.islower changes to false but the flag still maintains True because if the
"or" gate'''


# -----------------------------------------------------------------------------------------------------------------------

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True


'''This code returns True by default but, it will only work when the string being tested has not more that one 
upper case letter. Once it encounters an upper case letter, it returns a value and the if statement doesnt run
anymore.
 '''
# -----------------------------------------------------------------------------------------------------------------------

print(any_lowercase1('WaSEe'))
print(any_lowercase2('CSEc'))
print(any_lowercase3('ccSEc'))
print(any_lowercase4('CSddE'))
print(any_lowercase5('EeE'))
