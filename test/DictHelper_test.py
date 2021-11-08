"""
 * @file   : DictHelper_test.py
 * @time   : 20:35
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.data.DictHelper import *


def test_contains_key():
    _dict = dict()
    _dict['a'] = "AA"
    _dict['b'] = "BB"
    _dict['c'] = "CC"
    actual = DictHelper.contain_key(_dict, 'a')
    expected = True
    assert actual == expected

    actual = DictHelper.contain_key(_dict, 'f')
    expected = False
    assert actual == expected
