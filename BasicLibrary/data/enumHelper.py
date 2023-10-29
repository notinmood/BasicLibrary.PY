"""
 * @file   : enumHelper.py
 * @time   : 12:59
 * @date   : 2023/10/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class EnumHelper:

    @staticmethod
    def is_exist_value(enum_type, item_value):
        for i, e in enumerate(enum_type):
            if e.value == item_value:
                return True
            pass
        pass
        return False

    pass


pass
