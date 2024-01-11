"""
 * @file   : ioEnum.py
 * @time   : 10:37
 * @date   : 2024/1/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from enum import Enum


class ObjectHasExistedDealStrategyEnum(Enum):
    """
    目标对象已经存在时的处理策略
    """
    DoNoting = "DoNoting"  # 什么都不做
    RenameNew = "RenameNew"  # 给新的对象自动重新命名
    UsingOld = "UsingOld"  # 直接使用旧有的目标对象
    OverWrite = "OverWrite"  # 对既有的文件进行重写覆盖
    Appending = "Appending"  # 在既有的文件后追加新内容（通常用在文本文件场景下）


pass
