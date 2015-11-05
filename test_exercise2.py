#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find

pangram = "The quick brown fox jumps over the lazy dog."

def test_find_basic():
    """
    Test find function.
    """
    # Positive Cases
    # Basic strings
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    # DNA sequence matching
    assert find("TCGATCGAACTG", "ACTG", 0, 12) == 8

    # Numbers
    assert find("0123456789", "456", 0, 10) == 4

    # Phrases
    assert find(pangram, "quick brown fox", 0, 71) == 4

    # Returns the lowest index only
    long_string = "This is the first ACTG string. This ACTG string should not be returned."
    assert find(long_string, "ACTG", 0, 71) == 18


    # Errors
    # Returns -1 for failures
    assert find(pangram, "cat", 0, 44) == -1

    # Empty entry
    assert find("", "cat", 0, 0) == -1

    # 'start' param beyond first index occurrence leads to failure
    assert find(pangram, "quick", 20, 71) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    # Positive Cases
    # Basic string with multiple sub-strings
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    # DNA sequence matching, there are 3 ACTG sub-strings
    assert multi_find("TCGAACTGACTGTCGAACTG", "ACTG", 0, 20) == "4,8,16"

    # Numbers
    assert multi_find("01234567890123456789", "456", 0, 20) == "4,14"

    # Returns all sub-string instances
    long_string = "This is the first ACTG string. This ACTG string should be returned."
    assert multi_find(long_string, "ACTG", 0, 66) == "18,36"


    # Errors
    # Returns "" when no sub-strings found
    assert multi_find(pangram, "cat", 0, 44) == ""

    # Empty entry
    assert multi_find("", "cat", 0, 0) == ""

    # 'start' param beyond first index occurrence leads to failure
    assert multi_find(pangram, "quick", 20, 71) == ""



