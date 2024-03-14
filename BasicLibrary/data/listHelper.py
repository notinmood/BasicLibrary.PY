"""
 * @file   : test_DateTimeHelper.py
 * @time   : 16:26
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from typing import Callable

from BasicLibrary import ObjectHelper


class ListHelper:
    """
    列表助手
    """

    @staticmethod
    def get[T](list_data: list[T] | None, index: int, default_value: T = None):
        """
        安装索引，安全地从数组中获取元素
        :param default_value:
        :param list_data:
        :param index:元素的索引号
        :return:返回索引指定的元素；如果指定的索引号在数组内不存在，返回 None。
        """
        if ObjectHelper.is_empty(list_data):
            return default_value
        pass

        list_length = ObjectHelper.get_length(list_data)
        if list_length == 0:
            return default_value
        pass

        if index >= list_length:
            return default_value
        pass

        return list_data[index]

    pass

    @staticmethod
    def get_index(list_data, item, item_property_name: str = None) -> int | None:
        """
        获取某个元素在list中的index
        :param list_data:
        :param item:
        :param item_property_name:
        :return:
        """
        if not isinstance(list_data, enumerate):
            list_data = enumerate(list_data)
        pass

        for _index, _item in list_data:
            if item_property_name:
                comparing_data = _item[item_property_name]
            else:
                comparing_data = _item
            pass

            if comparing_data == item:
                return _index
            pass

        return None

    pass

    @staticmethod
    def remove_duplication_item(data):
        """
        为list去除重复项
        :param data:
        :return:
        """
        return list(set(data))

    pass

    # 以下获取交集并集差集的算法，只支持元素为简单类型的list
    @staticmethod
    def get_union(list_a, list_b):
        """
        获取并集
        :param list_a:
        :param list_b:
        :return:
        """
        return list(set(list_a).union(set(list_b)))

    pass

    @staticmethod
    def get_intersection(list_a, list_b):
        """
        获取交集
        :param list_a:
        :param list_b:
        :return:
        """
        return list(set(list_a).intersection(set(list_b)))

    pass

    @staticmethod
    def get_difference_only_in_left(list_left, list_right):
        """
        获取单向差集（在左侧中有的元素，在右侧中没有的元素）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_left).difference(set(list_right)))

    pass

    @staticmethod
    def get_difference_only_in_right(list_left, list_right):
        """
        获取单向差集（在左侧中没有的元素，在右侧中有的元素）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_right).difference(set(list_left)))

    pass

    @staticmethod
    def get_difference_all(list_left, list_right):
        """
        获取双向差集（在左侧中有，右侧中没有；以及在右侧中有，左侧中没有 的所有数据的集合）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_left) ^ set(list_right))

    pass

    @staticmethod
    def sort[T](list_data: list[T], callback_func: Callable[[T], any] = None, reverse=False):
        """
        对列表内的元素进行排序
        :param reverse:
        :param list_data:
        :param callback_func: 排序规则的回调函数（复合列表下使用。复合列表就是父级list的子元素是其他复杂数据类型的情形，比如子元素是字典等。）
            入参为:列表的元素
            返回值为：依据列表元素计算出的一个可比较（Compare）的值，比如列表元素的某个属性对应的值。（Python内没有类似ICompare接口？
            如果有，需要将返回值类型any进行替换）
        :return:
        :example:
            actual = ListHelper.sort(cars, lambda item: item["year"])
            expected = [{'car': 'Audi', 'year': 2010},
                        {'car': 'Volvo', 'year': 2013},
                        {'car': 'BMW', 'year': 2019},
                        {'car': 'Porsche', 'year': 2023}]
            assert actual == expected
        """
        if callback_func:
            list_data.sort(key=callback_func, reverse=reverse)
        else:
            list_data.sort(reverse=reverse)
        pass

        return list_data

    pass

    @staticmethod
    def merge(*args):
        """
        合并两个 list
        :param list args:
        :return:
        """
        result = []
        for key in args:
            result += key
        pass

        return result

    pass

    @staticmethod
    def reverse(list_data: list):
        """
        返回翻转顺序的 list（翻转的list，不影响原来输入的list）
        :param list_data:
        :return:
        """
        return list(reversed(list_data))

    pass

    @staticmethod
    def remove_item(list_data: list, *item_args: any):
        """
        移除 list 中的 所有的符合条件的item项目
        :param list list_data:
        :param item_args:
        :return:
        """
        if not item_args:
            return list_data
        pass

        for _item in item_args:
            list_data = list(filter(lambda x: x != _item, list_data))
        pass

        return list_data

    pass

    @staticmethod
    def remove_item_by_index(list_data: list, index: int):
        """
        移除 list 中的 item
        :param list list_data:
        :param index:
        :return:
        """
        del list_data[index]

    pass

    @staticmethod
    def is_contains(list_data: list, item):
        """
        判断 list 是否包含 item
        :param list_data:
        :param item:
        :return:
        """
        return item in list_data

    @classmethod
    def has(cls, list_data: list, item):
        """
        判断 list 是否包含 item(is_contains的别名)
        :param list_data:
        :param item:
        :return:
        """
        return cls.is_contains(list_data, item)

    pass

    pass
