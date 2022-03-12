"""
 * @file   : enums.py
 * @time   : 19:59
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from enum import Enum


class RandomEnum(Enum):
    LowerLetters = "ascii_lowercase"
    UpperLetters = "ascii_uppercase"
    AllLetters = "ascii_letters"
    Digits = "digits"
    Punctuation = "punctuation"
    All = "all"


class OSNameEnum(Enum):
    Windows = "Windows"
    Linux = "Linux"
    Other = "Other"
