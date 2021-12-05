from builtins import *


class ObjectHelper:
    @staticmethod
    def is_empty(data):
        result = False

        if data is None:
            result = True
        else:
            _type = type(data)
            if _type is str and data == "":
                result = True

            if _type is bool and data is False:
                result = True

            if _type is list and data == []:
                result = True

            if (_type is set or _type is dict) and data == {}:
                result = True

            if _type is tuple and data == ():
                result = True

            if ObjectHelper.is_number(data) and data == 0:
                result = True

        return result

    @staticmethod
    def is_exist(data):
        if ObjectHelper.is_empty(data):
            return False
        else:
            return True

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

    @staticmethod
    def is_number(data):
        try:
            float(data)
            return True
        except (TypeError, ValueError):
            pass

        try:
            import unicodedata
            unicodedata.numeric(data)
            return True
        except (TypeError, ValueError):
            pass

        return False

    @staticmethod
    def get_type(data):
        """
        获取目标对象的数据类型
        :param data:
        :return:
        """
        return type(data)

    @staticmethod
    def get_length(data):
        """
        获取目标对象的长度
        :param data:
        :return:
        """
        return len(data)

    @staticmethod
    def is_instance(object_data, class_data):
        """

        :param object_data:
        :param class_data:
        :return:
        """
        return isinstance(object_data, class_data)
