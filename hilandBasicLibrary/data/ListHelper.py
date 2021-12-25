from builtins import *


class ListHelper:
    @staticmethod
    def get_index(list_data, value, item_property=None):
        """
        获取某个元素在list中的index
        :param list_data:
        :param value:
        :param item_property:
        :return:
        """
        if type(list_data) is not enumerate:
            list_data = enumerate(list_data)

        for index, item in list_data:
            if item_property:
                comparing_data = item[item_property]
            else:
                comparing_data = item

            if comparing_data == value:
                return index

        return None

    @staticmethod
    def remove_duplication_item(data):
        """
        为list去除重复项
        :param data:
        :return:
        """
        return list(set(data))

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

    @staticmethod
    def get_intersection(list_a, list_b):
        """
        获取交集
        :param list_a:
        :param list_b:
        :return:
        """
        return list(set(list_a).intersection(set(list_b)))

    @staticmethod
    def get_difference_only_in_left(list_left, list_right):
        """
        获取单向差集（在左侧中有的元素，在右侧中没有的元素）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_left).difference(set(list_right)))

    @staticmethod
    def get_difference_only_in_right(list_left, list_right):
        """
        获取单向差集（在左侧中没有的元素，在右侧中有的元素）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_right).difference(set(list_left)))

    @staticmethod
    def get_difference_all(list_left, list_right):
        """
        获取双向差集（在左侧中有，右侧中没有；以及在右侧中有，左侧中没有 的所有数据的集合）
        :param list_left:
        :param list_right:
        :return:
        """
        return list(set(list_left) ^ set(list_right))



# def sort_2d(original_data,sort_info=None,reverse=False):
#
