"""
 * @file   : EnumMate.py
 * @time   : 12:53
 * @date   : 2023/10/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from enum import Enum


# TODO:xiedali@20231029 暂时没有使用
class EnumBase(Enum):
    @classmethod
    def is_exist_value(cls, item_value):
        for i, e in enumerate(cls):
            if e.value == item_value:
                return True
            pass
        pass
        return False

    pass


pass
