"""
 * @file   : test_ObjectHelper.py
 * @time   : 21:12
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.objectHelper import *


def test_is_number():
    actual = ObjectHelper.is_number(0)
    expected = True
    assert actual == expected

    actual = ObjectHelper.is_number({})
    expected = False
    assert actual == expected


def test_is_empty():
    data = 0
    actual = ObjectHelper.is_empty(data)
    expected = True
    assert actual == expected

    data = 0.1
    actual = ObjectHelper.is_empty(data)
    expected = False
    assert actual == expected

    data = True
    actual = ObjectHelper.is_empty(data)
    expected = False
    assert actual == expected

    data = False
    actual = ObjectHelper.is_empty(data)
    expected = True
    assert actual == expected

    data = ""
    actual = ObjectHelper.is_empty(data)
    expected = True
    assert actual == expected

    data = []
    actual = ObjectHelper.is_empty(data)
    expected = True
    assert actual == expected


def test_is_exist():
    data = 0
    actual = ObjectHelper.is_exist(data)
    expected = False
    assert actual == expected


def test_is_index_exist():
    whole = "china"

    index = 0
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = True
    assert actual == expected

    index = 4
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = True
    assert actual == expected

    index = 5
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = False
    assert actual == expected

    index = -3
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = True
    assert actual == expected

    index = -4
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = True
    assert actual == expected

    whole = {"china", "usa"}
    index = 0
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = True
    assert actual == expected

    whole = {"china", "usa"}
    index = 2
    actual = ObjectHelper.is_index_exist(whole, index)
    expected = False
    assert actual == expected


def test_is_number():
    actual = ObjectHelper.is_number("qingdao")
    expected = False
    assert actual == expected

    actual = ObjectHelper.is_number(2)
    expected = True
    assert actual == expected


def test_get_type():
    my_data = 123
    actual = ObjectHelper.get_type(my_data)
    expected = int
    assert actual == expected

    my_data = "123"
    actual = ObjectHelper.get_type(my_data)
    expected = str
    assert actual == expected
