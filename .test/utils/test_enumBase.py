"""
 * @file   : test_enumBase.py
 * @time   : 18:07
 * @date   : 2023/10/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.enums import ImageTypeEnum


def test_is_exist_value():
    expected = ImageTypeEnum.is_exist_value("png")
    actual = True
    assert actual == expected

    expected = ImageTypeEnum.is_exist_value("jpg")
    actual = False
    assert actual == expected
