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


class RandomHelper:
    @staticmethod
    def create(size=8):
        allowed_chars = string.ascii_letters
        return ''.join(random.choice(allowed_chars) for x in range(size))
