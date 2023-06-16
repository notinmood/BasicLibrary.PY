from BasicLibrary import ObjectHelper


class ListHelper:
    """

    """

    @staticmethod
    def get(list_data, index, default_value=None):
        """
        安装索引，安全地从数组中获取元素
        :param default_value:
        :param list_data:
        :param index:元素的索引号
        :return:返回索引指定的元素；如果指定的索引号在数组内不存在，返回 None。
        """
        if ObjectHelper.is_empty(list_data):
            return default_value
        else:
            list_length = ObjectHelper.get_length(list_data)
            if list_length == 0:
                return default_value
            else:
                if index >= list_length:
                    return default_value
                else:
                    return list_data[index]

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

    @staticmethod
    def sort(list_data, callback_in__list__item_out__item_property=None, reverse=False):
        """
        对数组内的元素进行排序
        :param reverse:
        :param list_data:
        :param callback_in__list__item_out__item_property: 排序规则的回调函数
            入参为:数组的元素
            返回值为：数组元素的某个属性名称字符串
        :return:
        :example:
            actual = ListHelper.sort(cars, lambda item: item["year"])
            expected = [{'car': 'Audi', 'year': 2010},
                        {'car': 'Volvo', 'year': 2013},
                        {'car': 'BMW', 'year': 2019},
                        {'car': 'Porsche', 'year': 2023}]
            assert actual == expected
        """
        if callback_in__list__item_out__item_property:
            list_data.sort(key=callback_in__list__item_out__item_property, reverse=reverse)
        else:
            list_data.sort(reverse=reverse)

        return list_data

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

        return result

    @staticmethod
    def reverse(list_data):
        """
        返回翻转顺序的 list（翻转的list，不影响原来输入的list）
        :param list_data:
        :return:
        """
        return list(reversed(list_data))

    pass
