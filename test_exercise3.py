#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STUDENTS = [["Number", "Surname", "Age"],
            [7274, "Robinson", 37],
            [1234, "Test student", 56],
            [7890, "New student", 01]]

BAD_SCHEMA = [["Number", "Surname", "First Name", "Age"],
              [7274, "Robinson", "Tom", 37],
              [7432, "O'Malley", "Bob", 39]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    # return set(map(tuple, t1)) == set(map(tuple, t2))
    return t1.sort() == t2.sort()  # Professor Sim's update

###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    # Positive cases
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    # STUDENTS list
    result2 = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [1234, "Test student", 56],
              [7890, "New student", 01]]

    assert is_equal(result2, union(GRADUATES, STUDENTS))

    # BAD_SCHEMA union with itself; works since schemas do match.
    result3 = [["Number", "Surname", "First Name", "Age"],
              [7274, "Robinson", "Tom", 37],
              [7432, "O'Malley", "Bob", 39]]

    assert is_equal(result3, union(BAD_SCHEMA, BAD_SCHEMA))


    # Errors
    # Exception handling - testing schemas not matching
    try:
        union(GRADUATES, BAD_SCHEMA)
    except MismatchedAttributesException:
        assert True



def test_intersection():
    """
    Test intersection operation.
    """

    # Positive cases
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    # STUDENTS list
    result2 = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result2, intersection(GRADUATES, STUDENTS))

    # BAD_SCHEMA intersection with itself; works since schemas do match.
    result3 = [["Number", "Surname", "First Name", "Age"],
              [7274, "Robinson", "Tom", 37],
              [7432, "O'Malley", "Bob", 39]]

    assert is_equal(result3, intersection(BAD_SCHEMA, BAD_SCHEMA))

    # If no common rows exist
    result4 = []

    assert is_equal(result4, intersection(MANAGERS, STUDENTS))

    # Errors
    # Exception handling - testing schemas not matching
    try:
        intersection(GRADUATES, BAD_SCHEMA)
    except MismatchedAttributesException:
        assert True


def test_difference():
    """
    Test difference operation.
    """

    # Positive cases
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

    # STUDENTS list
    result2 = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result2, difference(GRADUATES, STUDENTS))

    # BAD_SCHEMA difference with itself; works since schemas do match.
    # Result only has the header because there are
    # no "unique rows that appear in the first table but not the second."
    # result3 = [["Number", "Surname", "First Name", "Age"]]
    result3 = []  # Updated 2015-11-06

    assert is_equal(result3, difference(BAD_SCHEMA, BAD_SCHEMA))

    # If no common rows exist
    result4 = []

    assert is_equal(result4, difference(MANAGERS, STUDENTS))

    # Errors
    # Exception handling - testing schemas not matching
    try:
        difference(GRADUATES, BAD_SCHEMA)
    except MismatchedAttributesException:
        assert True
