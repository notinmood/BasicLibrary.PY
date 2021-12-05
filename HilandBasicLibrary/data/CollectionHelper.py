"""
 * @file   : CollectionHelper.py
 * @time   : 12:40
 * @date   : 2021/12/4
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class CollectionHelper:
    """
    对集合类型的常用方法进行整合
    """

    @staticmethod
    def sort(iterable, key=None, reverse=False):
        """
        调用系统的sorted方法对可以迭代对象进行排序
        :param iterable:
        :param key:
        :param reverse:
        :return:
        """
        return sorted(iterable, key=key, reverse=reverse)

    @staticmethod
    def sort_for_inner_is_dict(iterable, key_name, reverse=False):
        """
        为内部成员为字典的可迭代对象，按指定的字典键名进行排序
        :param iterable:
        :param key_name:字典的键名称字符串
        :param reverse:
        :return:
        """
        return sorted(iterable, key=lambda k: k[key_name], reverse=reverse)
