"""
 * @file   : test_DictHelper.py
 * @time   : 20:35
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.dictHelper import *


def test_contains_key():
    _dict = dict()
    _dict['a'] = "AA"
    _dict['b'] = "BB"
    _dict['c'] = "CC"
    actual = DictHelper.is_contains_key(_dict, 'a')
    expected = True
    assert actual == expected

    actual = DictHelper.is_contains_key(_dict, 'f')
    expected = False
    assert actual == expected


def test_contains_value():
    _dict = dict()
    _dict['a'] = "AA"
    _dict['b'] = "BB"
    _dict['c'] = "CC"
    actual = DictHelper.is_contains_value(_dict, 'AA')
    expected = True
    assert actual == expected

    actual = DictHelper.is_contains_value(_dict, 'a')
    expected = False
    assert actual == expected
