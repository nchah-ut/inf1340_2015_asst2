#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_table = []

    # Schema match check:
    if table1[0] == table2[0]:
        # Append header row
        new_table.append(table1[0])

        # Matching table1 rows to table2
        for t1_row in table1[1:]:
            if t1_row not in table2 or t1_row not in new_table:
                new_table.append(t1_row)

        # Matching table2 rows to table1
        for t2_row in table2[1:]:
            if t2_row not in table1 or t2_row not in new_table:
                new_table.append(t2_row)
    else:
        raise MismatchedAttributesException("Bad Schema.")

    return new_table


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_table = []

    if table1[0] == table2[0]:
        # Append header row
        new_table.append(table1[0])

        # Matching table1 rows to table2
        for t1_row in table1[1:]:
            if t1_row in table2:
                new_table.append(t1_row)

        # Matching table2 rows to table1
        for t2_row in table2[1:]:
            if t2_row in table1 and t2_row not in new_table:
                new_table.append(t2_row)
    else:
        raise MismatchedAttributesException("Bad Schema.")

    return new_table


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_table = []



    return new_table


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result




