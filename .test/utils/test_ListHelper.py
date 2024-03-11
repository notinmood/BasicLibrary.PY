"""
 * @file   : test_ListHelper.py
 * @time   : 20:46
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.listHelper import *


def test_sort():
    cars = [
        {'car': 'Porsche', 'year': 2023},
        {'car': 'Audi', 'year': 2010},
        {'car': 'BMW', 'year': 2019},
        {'car': 'Volvo', 'year': 2013}
    ]

    actual = ListHelper.sort(cars, lambda item: item["year"])
    expected = [{'car': 'Audi', 'year': 2010},
                {'car': 'Volvo', 'year': 2013},
                {'car': 'BMW', 'year': 2019},
                {'car': 'Porsche', 'year': 2023}]
    assert actual == expected

    actual = ListHelper.sort(cars, lambda item: item["year"], reverse=True)
    expected = [{'car': 'Porsche', 'year': 2023},
                {'car': 'BMW', 'year': 2019},
                {'car': 'Volvo', 'year': 2013},
                {'car': 'Audi', 'year': 2010}]
    assert actual == expected

    my_list = [5, 8, 3, 6, 1, 10, 2]
    actual = ListHelper.sort(my_list, reverse=True)
    expected = [10, 8, 6, 5, 3, 2, 1]
    assert actual == expected


def test_get():
    my_list = []
    actual = ListHelper.get(my_list, 0)
    expected = None
    assert actual == expected

    my_list = None
    actual = ListHelper.get(my_list, 0)
    expected = None
    assert actual == expected

    my_list = [1, 2, 4]
    actual = ListHelper.get(my_list, 3)
    expected = None
    assert actual == expected

    actual = ListHelper.get(my_list, 2)
    expected = 4
    assert actual == expected


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


def test_merge1():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [6, 7, 8]
    actual = ListHelper.merge(a, b, c)
    expected = [1, 2, 3, 4, 5, 6, 6, 7, 8]
    assert actual == expected


def test_merge2():
    a = [1, 2, 3]
    b = [4, 2, 3]

    actual = ListHelper.merge(a, b)
    expected = [1, 2, 3, 4, 2, 3]
    assert actual == expected


def test_reverser():
    a = [4, 5, 6]
    b = [6, 5, 4]

    c = ListHelper.reverse(a)

    actual = c
    expected = b
    assert actual == expected

    # 验证返回的结果，对传入的原值没有影响
    actual = c
    expected = a
    assert actual != expected


pass


def test_remove_item():
    original_list = ["", "a", "\n", "b", "c", "", "\n"]

    actual = ListHelper.remove_item(original_list, "", "\n")
    expected = ['a', 'b', 'c']
    assert actual == expected


pass
