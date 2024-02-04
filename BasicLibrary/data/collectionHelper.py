"""
 * @file   : collectionHelper.py
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

    pass

    @staticmethod
    def sort_dict(iterable, key_name, reverse=False):
        """
        为内部成员为字典的可迭代对象，按指定的字典键名进行排序
        :param iterable:
        :param key_name:字典的键名称字符串
        :param reverse:
        :return:
        """
        return sorted(iterable, key=lambda k: k[key_name], reverse=reverse)

    pass

    @staticmethod
    def is_contains(iterable, item, item_value=None):
        """
        判断集合中是否存在某个元素
        如果判断是list,set集合，则自动忽略 item_value
        如果判断的dict集合，item是指某元素的key,item_value是指元素的value
        :param item_value:
        :param iterable:
        :param item:
        :return:
        """
        _type = type(iterable)

        if _type is dict:
            for key in iterable:
                if key == item and iterable[key] == item_value:
                    return True
                pass
            pass

            return False
        else:
            for key in iterable:
                if key == item:
                    return True
                pass
            pass

            return False
        pass

    pass


pass
