#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result
    # helper functions
def is_vowel(c):
    return c.lower() in "'a','e','i','o','u'"

# get position of the first vowel
def position_of_vowel(s):
    for i in range(len(s)):
        if is_vowel(s[i]):
            return i
    return -1 # no vowel at all


def pig_latinify(word):
    if len(word) > 0 and word.isalpha():
        first = word[0]
        if is_vowel(first):     # starts with a vowel
            print str(word) + "way"
        else:                   # starts with non-vowel
            cut = position_of_vowel(word) # where to cut the word
            if cut > 0:           # "street"-->"eet+str+ay"
                print word[cut:] + word[:cut] + "ay"
            else:                 # no vowel found
                print word + "ay"
    elif len(word) > 0 and not word.isalpha():
        print 'Only letters allowed!'
    else:
        print 'empty'


### tests
pig_latinify("home")  # one consonant
pig_latinify("children")  # two consonants
pig_latinify("screw")   # three consonants
pig_latinify("Car")   # consonant uppercase
pig_latinify("apple")     # one vowel
pig_latinify("Aaron")  # two vowels + uppercase voewl


# ask user to type a word
pig_latinify(raw_input('Type a word please: '))
