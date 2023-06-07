"""
 * @file   : excelMisc.py
 * @time   : 11:27
 * @date   : 2022/3/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import re

from BasicLibrary import ObjectHelper
from BasicLibrary.data.listHelper import ListHelper
from BasicLibrary.data.numberHelper import NumberHelper
from BasicLibrary.data.regexHelper import RegexHelper
from BasicLibrary.data.stringHelper import StringHelper

"""
本模块内方法不对外暴露，如果外部有使用需求，请在 excelHelper.py 内做一个别名转发
"""


def _calc_range_marker(original_range_marker, row_delta, column_delta):
    original_range_marker = StringHelper.replace(original_range_marker, "：", ":")

    if StringHelper.is_contains(original_range_marker, ":"):
        marker_begin = StringHelper.get_before_content(original_range_marker, ":")
        marker_end = StringHelper.get_after_content(original_range_marker, ":")

        new_marker_begin = _calc_cell_marker(marker_begin, row_delta, column_delta)
        new_marker_end = _calc_cell_marker(marker_end, row_delta, column_delta)

        return f"{new_marker_begin}:{new_marker_end}"
    else:
        return _calc_cell_marker(original_range_marker, row_delta, column_delta)


def _calc_cell_marker(original_cell_marker, row_delta, column_delta=0):
    """
    通過單元格的標識值和偏移量，計算新單元格的標識值
    :param original_cell_marker:
    :param row_delta:
    :param column_delta:
    :return:
    """
    # 先从类似 "A2" 里面分离出 字母和数字
    column_pattern = r"[a-zA-Z]+"
    column_matched = RegexHelper.get_matched_items(original_cell_marker, column_pattern)

    row_pattern = r"\d+"
    row_matched = RegexHelper.get_matched_items(original_cell_marker, row_pattern)

    if ObjectHelper.is_exist(column_matched):
        column_name = column_matched[0]
        row_name = ListHelper.get(row_matched, 0, 1)
        new_column_name = _calc_column_name(column_name, column_delta)
        new_row_name = int(row_name) + row_delta

        return f"{new_column_name}{new_row_name}"
    else:
        return None


def _calc_column_name(start_column_name, delta):
    """
    通過當前列的名稱和偏移量，計算新列的名稱
    :param start_column_name:
    :param delta:
    :return:
    """
    _len = ObjectHelper.get_length(start_column_name)

    """
    列名称的最大长度为2，超过2不接受，直接返回 false
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
