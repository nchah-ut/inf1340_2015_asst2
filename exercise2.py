#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    # Convert to int type, in case of floats
    start, end = int(start), int(end)

    # This is the range that substring will search over
    searchable_string = input_string[start:end]

    for char_index in range(0, len(searchable_string)):
        # Search the searchable_string in chunks of len equal to substring
        if substring in searchable_string[char_index:char_index + len(substring)]:
             return char_index

    return -1



def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    # Convert to int type, in case of floats
    start, end = int(start), int(end)

    # This is the range that substring will search over
    searchable_string = input_string[start:end]

    for char_index in range(0, len(searchable_string)):
        # Search the searchable_string in chunks of len equal to substring
        if substring in searchable_string[char_index:char_index + len(substring)]:
            # First entry in the string should not have a comma
            if len(result) > 0:
                result += "," + str(char_index)
            else:
                result += str(char_index)

    return result


