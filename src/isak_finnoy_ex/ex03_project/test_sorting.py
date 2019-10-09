# -*- coding: utf-8 -*-

__author__ = 'Isak Finnøy'
__email__ = 'isfi@nmbu.no'


import random
import string


def bubble_sort(data1):

    sorted_data = list(data1)
    cards = len(sorted_data)
    for i in range(cards):
        for j in range(0, cards - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = (sorted_data[j + 1],
                                                      sorted_data[j])
    return tuple(sorted_data)  # returning the processed list as a tuple


def test_empty():
    """Test that the sorting function works for empty list
    """
    empty_list = []
    assert bubble_sort(empty_list) == ()


def test_single():
    """Test that the sorting function works for single-element list"""
    single_element = [1]

    assert bubble_sort(single_element) == tuple(single_element)


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    """Test that sorting works on sorted data."""

    original_list = [3, 2, 1]
    sorted_list = bubble_sort(original_list)
    assert sorted_list != original_list


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    revers_sorted = [7, 4, 3, 1]
    sorted_ = (1, 3, 4, 7)
    assert bubble_sort(revers_sorted) == sorted_


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    list_with_identicals = [2, 1, 3, 1, 2]
    sorted_identical = (1, 1, 2, 2, 3)
    assert bubble_sort(list_with_identicals) == sorted_identical


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """

    list_of_lists_and_strings = []
    for elem1 in range(10):
        n = random.randint(1, 10)
        random_list = random.sample(range(1, 100), n)
        list_of_lists_and_strings.append(random_list)

    letters = string.ascii_letters
    for elem2 in range(5):
        list_string = []
        n = random.randint(1, 5)
        for i in range(n):
            random_string = random.choice(letters)
            list_string.append(random_string)
        list_of_lists_and_strings.append(list_string)

    for ind in range(len(list_of_lists_and_strings)):
        assert bubble_sort(list_of_lists_and_strings[ind]) ==\
               tuple(sorted(list_of_lists_and_strings[ind]))
