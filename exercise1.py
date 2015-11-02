#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# TODO(nchah): We can get rid of this part since it's duplicated below
# def pig_latinify(word):
#     """
#     Describe your function
#
#     :param :
#     :return:
#     :raises:
#
#     """
#     result = ""
#
#     return result


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
    if len(word) > 0 and word.isalpha():
        first = word[0]
        if is_vowel(first):     # starts with a vowel
            pig_latined_word = str(word) + "yay"
        else:                   # starts with non-vowel
            cut = position_of_vowel(word) # where to cut the word
            if cut > 0:           # "street"-->"eet+str+ay"
                pig_latined_word = word[cut:] + word[:cut] + "ay"
            else:                 # no vowel found
                pig_latined_word = word + "ay"
    elif len(word) > 0 and not word.isalpha():
        print 'Only letters allowed!'
    else:
        print 'empty'

    return pig_latined_word


# ask user to type a word
# pig_latinify(raw_input('Type a word please: '))
