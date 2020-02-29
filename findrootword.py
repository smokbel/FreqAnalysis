import nltk
from nltk.corpus import stopwords

"""
    simple stemming algorithm that focuses on
    possible word endings for regular english verbs and regular pluralization,
    and returns the root word
    considering all regular verb conjugation cases outlined in https://www.scientificpsychic.com/grammar/regular.html
    pluralization 2 cases:
    +'s' except for words ending in s, sh, ch, x, or z: +'es'
    verbs ending in consonant clusters or sibiliants: endings of 'ed' 'es';
"""

endings = ['ss', 'ies', 'es', 's','ied', 'ing', 'ed']
digraphs = ['ou', 'oi', 'ai', 'ei', 'ea', 'oo', 'eu', 'ee']
longvowel = ['ow', 'oy', 'ew', 'ey', 'uw', 'aw', 'ay']
sibiliants = ['ss', 'sh', 'ch', 'x', 'z', 'ck', 'sk', 'st']
vowel = set('aeiou')
o_end = set('mnwcvb')

stop_words = set(stopwords.words('english'))

def cutString(string, amount):
    string = string[:-amount]
    return string

def contains_di(string):
    for di in digraphs:
        if string.find(di) != -1:
            return True
        else:
            False

def end_sibiliant(str):
    for end in sibiliants:
        if str.endswith(end):
            return True
        else:
            return False

def end_longvowel(str):
    for end in longvowel:
        if str.endswith(end):
            return True
        else:
            return False

"Checking CVC ending - Consonant Vowel Consonant, to determine whether to add a silent 'e' at the end of the verb"

def ends_cvc(str):
    if (str[-1] not in vowel and str[-2] in vowel and str[-3] not in vowel):
        return True
    else:
        return False

def findRootWord(str):
    if str in stop_words:
        return None

    for ends in endings:


        if str.endswith(ends):

            cut = len(ends)
            cut_str = cutString(str,cut)
            n = len(cut_str)

            if n <= 2:
                return str

            if (ends == 'ied' or ends == 'ies'):
                str = cut_str + 'y'
                return str

            if (ends == 'ed' or ends == 'ing'):

                if contains_di(cut_str) == True:
                    return cut_str

                if ends_cvc(cut_str) == True:
                    if cut_str[-3] == cut_str[-4]:
                        return cut_str
                    else:
                        return cut_str + 'e'

                if ends_cvc(cut_str) == False:
                    if end_sibiliant(cut_str) == True:
                        return cut_str
                    if end_sibiliant(cut_str) == False:
                        if cut_str[-1] in o_end:
                            return cut_str + 'e'


                if (cut_str[-2] == cut_str[-1] != 's' or 'z'):
                    return cut_str[:-1]

print(findRootWord('cowboy'))
print(findRootWord('played'))
print(findRootWord('flattered'))
print(findRootWord('desired'))
print(findRootWord('danced'))
print(findRootWord('fizzed'))
print(findRootWord('evolved'))
print(findRootWord('troubling'))

print(contains_di('devour'))
print(contains_di('flater'))
