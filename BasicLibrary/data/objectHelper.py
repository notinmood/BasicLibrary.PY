from BasicLibrary.model.dataCompare import DataSummary


class ObjectHelper:
    """

    """

    @staticmethod
    def is_empty(data):
        """
        判断给定的数据是否为空，包括 None、空字符串、空列表、空字典、空元组等。
        :param data:
        :return:
        """
        if not data:
            return True
        else:
            return False
        pass

    @staticmethod
    def is_exist(data):
        if ObjectHelper.is_empty(data):
            return False
        else:
            return True
        pass

    pass

    @staticmethod
    def is_index_exist(collection, index):
        """
        判断一个索引值是否存在
        :param collection:
        :param index:
        :return:
        """
        if index is None:
            return False
        else:
            if collection is None:
                return False
            else:
                length = len(collection)
                if length > index >= -length:
                    return True
                else:
                    return False
                pass
            pass
        pass

    pass

    @staticmethod
    def is_number(data):
        """
        判断给定的数据是否为数字
        :param data:
        :return:
        """
        return isinstance(data, (int, float, complex))
        # try:
        #     float(data)
        #     return True
        # except (TypeError, ValueError):
        #     pass
        #
        # try:
        #     import unicodedata
        #     unicodedata.numeric(data)
        #     return True
        # except (TypeError, ValueError):
        #     pass
        #
        # return False

    pass

    @staticmethod
    def get_type(data):
        """
        获取目标对象的数据类型
        使用方法：`if ObjectHelper.get_type(entity_dict_or_list) is dict:`等
        :param data:
        :return:
        """
        return type(data)

    pass

    @staticmethod
    def get_length(data):
        """
        获取目标对象的长度
        :param data:
        :return:
        """
        return len(data)

    pass

    @staticmethod
    def is_instance(object_data, class_data):
        """

        :param object_data:
        :param class_data:
        :return:
        """
        return isinstance(object_data, class_data)

    pass

    @staticmethod
    def get_summary(object_data):
        """
        获取目标对象的摘要信息
        :param object_data:
        :return:
        """
        summary = DataSummary(object_data)
        return summary

    pass

    @staticmethod
    def has_member(object_data, member_name):
        """
        判断目标对象是否包含指定名称的成员
        (如果是判断集合内是否存在某成员，请使用 CollectionHelper.is_contains() 方法。)
        :param object_data:
        :param member_name:
        :return:
        """

        return member_name in object_data

    pass
