"""
 * @file   : memoryHelper.py
 * @time   : 8:33
 * @date   : 2022/3/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import sys


def get_using_memo(data):
    """
    获取对象占用的内存大小（单位为字节）
    :param data:
    :return:
    """
    return sys.getsizeof(data)
