#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    # Basic strings
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    # DNA sequence matching
    assert find("TCGATCGAACTG", "ACTG", 0, 12) == 8

    # find() returns the lowest index only
    long_string = "This is the first ACTG string. This ACTG string should not be returned."
    assert find(long_string, "ACTG", 0, 71) == 18

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    # Basic string with multiple sub-strings
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    # DNA sequence matching, there are 3 ACTG sub-strings
    assert multi_find("TCGAACTGACTGTCGAACTG", "ACTG", 0, 20) == "4,8,16"

    # multi_find() returns all sib-string instances
    long_string = "This is the first ACTG string. This ACTG string should not be returned."
    assert multi_find(long_string, "ACTG", 0, 71) == "18,36"

