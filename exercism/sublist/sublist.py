"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one: list, list_two: list):
    l1 = len(list_one)
    l2 = len(list_two)
    if list_one == list_two:
        return EQUAL
    elif l1 < l2 and list_one in [list_two[i: l1+i]for i in range(l2- l1+1)]:
        return SUBLIST
    elif l2 < l1 and list_two in [list_one[i: l2+i]for i in range(l1- l2+1)]:
        return SUPERLIST
    return UNEQUAL