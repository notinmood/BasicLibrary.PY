"""
 * @file   : typeHelper.py
 * @time   : 19:17
 * @date   : 2023/6/13
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.typeEnum import TypeEnum


# TODO:xiedali@20230613 添加其他的各种数据类型
class TypeHelper(object):
    @staticmethod
    def get_type(data):
        return type(data)
    pass


pass
