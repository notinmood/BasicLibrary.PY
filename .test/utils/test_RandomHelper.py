"""
 * @file   : test_RandomHelper.py
 * @time   : 20:02
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.enums import RandomEnum


def test_create():
    random_data = RandomHelper.create(8)
    print(random_data)
    actual = 8
    expected = len(random_data)
    assert actual == expected

    random_data = RandomHelper.create(20, random_type=RandomEnum.Digits)
    print(random_data)
    actual = 20
    expected = len(random_data)
    assert actual == expected

    random_data = RandomHelper.create(10, random_type=RandomEnum.All)
    print(random_data)
    actual = 10
    expected = len(random_data)
    assert actual == expected
