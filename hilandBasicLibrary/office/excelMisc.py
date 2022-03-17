"""
 * @file   : excelMisc.py
 * @time   : 11:27
 * @date   : 2022/3/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import re

from hilandBasicLibrary import ObjectHelper
from hilandBasicLibrary.data.numberHelper import NumberHelper
from hilandBasicLibrary.data.stringHelper import StringHelper

"""
本模块内方法不对外暴露，如果外部有使用需求，请在 excelHelper.py 内做一个别名转发
"""


def _calc_column_name(start_column_name, delta):
    _len = ObjectHelper.get_length(start_column_name)

    """
    列名称的最大长度为2，超过2不接受直接返回 false
    """
    if _len > 2:
        return False

    # TODO:xiedali@2022/3/17 加入对只能是字母的判断
    # pattern = r"\l"
    # re.fullmatch().group()

    start_column_name = StringHelper.upper_all_chars(start_column_name)
    start_column_name = StringHelper.reverse(start_column_name)

    score = 0
    for i in range(len(start_column_name)):
        item = start_column_name[i]
        if i == 0:
            score = score + ord(item) - 65
        else:
            score = score + (ord(item) - 65 + 1) * 26

    score = score + delta

    """
    最小的列名称是A，比A再小就不存在了。
    """
    if score < 0:
        return False

    i = NumberHelper.get_division_result_before_dot(score, 26)
    n = score % 26

    if i > 0:
        x1 = int(i - 1)
        x2 = int(n)
        result = chr(x1 + 65) + chr(x2 + 65)
    else:
        result = chr(n + 65)

    return result
