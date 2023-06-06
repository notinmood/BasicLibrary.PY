"""
 * @file   : databaseEnum.py
 * @time   : 7:39
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from enum import Enum


class BatchMode(Enum):
    """

    """
    ONE = 1
    MANY = 0


class LikeMatchMode(Enum):
    """

    """
    BOTH = 0
    BEFORE = 1
    AFTER = 2
