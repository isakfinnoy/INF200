# -*- coding: utf-8 -*-

__author__ = 'Isak Finnøy'
__email__ = 'isfi@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if len(sdata) == 0:
        raise ValueError
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


# Hentet koden over fra:
# https://github.com/yngvem/INF200-2019-
# Exercises/blob/master/exersices/ex03.rst


def test_median_single():
    """testing if 'median' correctly returns for a list of one element
    """
    one_element = [1]
    assert median(one_element) == 1


def test_several_lists():
    odd_list = [1, 3, 2, 5, 2]
    even_list = [4, 2, 6, 113]
    order_list = [1, 3, 5, 7]
    revers_list = [4, 3, 2, 1]
    assert median(odd_list) == 2
    assert median(even_list) == 5
    assert median(order_list) == 4
    assert median(revers_list) == 2.5


def test_median_valueerror():
    empty_list = []
    with pytest.raises(ValueError):
        median(empty_list)


def test_original_content():
    original_content = [3, 2, 1]
    new_original_content = original_content
    median(new_original_content)
    assert id(new_original_content) == id(original_content)


def test_median_tuple():
    my_tuple = (1, 2, 3)
    assert median(my_tuple) == 2
