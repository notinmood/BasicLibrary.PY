"""
 * @file   : test_NumberHelper.py
 * @time   : 15:39
 * @date   : 2022/3/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.numberHelper import NumberHelper


def test_get_division_result_before_dot():
    actual = NumberHelper.get_division_result_before_dot(10, 3)
    expected = 3
    assert actual == expected


def test_get_division_result_after_dot():
    actual = NumberHelper.get_division_result_after_dot(10, 3)
    expected = 0.3333333333333335
    assert actual == expected


def test_get_division_result():
    actual = NumberHelper.get_division_result(10, 3, 2)
    expected = 3.33
    assert actual == expected
