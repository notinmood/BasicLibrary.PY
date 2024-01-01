"""
 * @file   : randomHelper.py
 * @time   : 19:51
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import random
import string

from BasicLibrary.enums import RandomEnum


class RandomHelper:
    """
    随机字符串生成器
    """

    @staticmethod
    def create(size=8, random_type=RandomEnum.AllLetters):
        """
        生成随机字符串
        :param random_type: 随机字符串可以使用的字符系列
        :param size: 随机字符串的长度
        :return:
        """
        match random_type:
            case RandomEnum.UpperLetters:
                allowed_chars = string.ascii_uppercase
            case RandomEnum.LowerLetters:
                allowed_chars = string.ascii_lowercase
            case RandomEnum.Digits:
                allowed_chars = string.digits
            case RandomEnum.Punctuation:
                allowed_chars = string.punctuation
            case RandomEnum.AllLetters:
                allowed_chars = string.ascii_letters
            case _:
                allowed_chars = string.digits + string.ascii_letters + string.punctuation

        return ''.join(random.choice(allowed_chars) for x in range(size))

    pass


pass
