"""
 * @file   : ListHelper_test.py
 * @time   : 20:46
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.ListHelper import *


def test_get_union():
    a_list = [1, 2, 3, 4]
    b_list = [1, 4, 5]

    actual = ListHelper.get_union(a_list, b_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_get_intersection():
    a_list = [1, 2, 3, 4]
    b_list = [1, 4, 5]

    actual = ListHelper.get_intersection(a_list, b_list)
    expected = [1, 4]
    assert actual == expected


def test_get_difference_only_in_left():
    a_list = [1, 2, 3, 4]
    b_list = [1, 4, 5]

    actual = ListHelper.get_difference_only_in_left(a_list, b_list)
    expected = [2, 3]
    assert actual == expected


def test_get_difference_only_in_right():
    a_list = [1, 2, 3, 4]
    b_list = [1, 4, 5]

    actual = ListHelper.get_difference_only_in_right(a_list, b_list)
    expected = [5]
    assert actual == expected


def test_get_difference_all():
    a_list = [1, 2, 3, 4]
    b_list = [1, 4, 5]

    actual = ListHelper.get_difference_all(a_list, b_list)
    expected = [2, 3, 5]
    assert actual == expected
