"""
 * @file   : test_Singleton.py
 * @time   : 14:48
 * @date   : 2022/1/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.student import Student


def test_singleton():
    cls1 = Student()
    cls2 = Student()

    assert cls1 == cls2
