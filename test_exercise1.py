#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # one consonant
    assert pig_latinify("home") == "omehay"

    # two consonants
    assert pig_latinify("children") == "ildrenchay"

    # three consonants
    assert pig_latinify("screw") == "ewscray"

    # consonant uppercase
    assert pig_latinify("Car") == "arCay"

    # one vowel
    assert pig_latinify("apple") == "appleyay"
    assert pig_latinify("Aaron") == "Aaronyay"

    # numbers
    assert pig_latinify("123") == "Only letters allowed!"
    
    # blank space
    assert pig_latinify("   ") == "Only letters allowed!"
    
    # only consonants
    assert pig_latinify("123") == "Only letters allowed!"

