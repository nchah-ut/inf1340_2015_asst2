#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


    # helper functions
def is_vowel(c):
    return c.lower() in "'a','e','i','o','u'"


def position_of_vowel(s):
    """
    get position of the first vowel
    """
    for i in range(len(s)):
        if is_vowel(s[i]):
            return i
    return -1 # no vowel at all


def pig_latinify(word):
    """
    Returns Pig Latin form of an English word

    :param word: any English language string
    :return: string converted to Pig Latin form
    :raises: None
    """
    if len(word) > 0 and word.isalpha():
        first = word[0]
        if is_vowel(first):     # starts with a vowel
            result = str(word) + "yay"
        else:                   # starts with non-vowel
            cut = position_of_vowel(word) # where to cut the word
            if cut > 0:           # "street"-->"eet+str+ay"
                result = word[cut:] + word[:cut] + "ay"
            else:                 # no vowel found
                result = word + "ay"
    elif len(word) > 0 and not word.isalpha():
        print 'Only letters allowed!'
    else:
        print 'empty'

    return result


# ask user to type a word  TODO: remove before submission
print pig_latinify(raw_input('Type a word please: '))
