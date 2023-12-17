"""
 * @file   : numberHelper.py
 * @time   : 15:17
 * @date   : 2022/3/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import math


class NumberHelper(object):
    """

    """

    def __init__(self):
        pass

    @classmethod
    def get_division_result_before_dot(cls, whole, by):
        """
        获取商数结果中的整数部分
        :param whole:
        :param by:
        :return:
        """
        return cls.__get_division_result_by_math(whole, by)[1]

    pass

    @classmethod
    def get_division_result_after_dot(cls, whole, by):
        """
        获取商数结果中的小数部分
        :param whole:
        :param by:
        :return:
        """
        return cls.__get_division_result_by_math(whole, by)[0]

    pass

    @staticmethod
    def __get_division_result_by_math(whole, by):
        if by == 0:
            return False
        else:
            return math.modf(whole / by)
        pass

    pass

    @staticmethod
    def get_division_result(whole, by, precision_width=2):
        """
        获取带精度小数的商数
        :param whole:
        :param by:
        :param precision_width:精度的长度（默认 2位宽度）
        :return:
        """
        return round(whole / by, precision_width)

    pass


pass
