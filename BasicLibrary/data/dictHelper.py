from BasicLibrary.model.dataCompare import DataSummary


# +--------------------------------------------------------------------------
# |::说明：|
# |·······|
# +--------------------------------------------------------------------------

class DictHelper:
    @staticmethod
    def is_contains_key(whole_dict, key_name):
        """
        字典内是否包含某键
        :param whole_dict:
        :param key_name:
        :return:
        """
        if key_name in whole_dict:
            return True
        else:
            return False
        pass

    pass

    @classmethod
    def get_value(cls, whole_dict, key_name, default_value=None):
        """
        通过 key 获取字典内的某值
        :param whole_dict:
        :param key_name:
        :param default_value:
        :return:
        """
        if cls.is_contains_key(whole_dict, key_name):
            return whole_dict[key_name]
        else:
            return default_value
        pass

    pass

    @classmethod
    def is_contains_value(cls, whole_dict, value):
        """
        判断字典内是否包含某值
        :param whole_dict:
        :param value:
        :return:
        """
        for key in whole_dict:
            if whole_dict[key] == value:
                return True
            pass
        pass

        return False

    pass

    @classmethod
    def get_summary(cls, dict_data):
        """
        获取字典的摘要信息
        :param dict_data:
        :return:
        """
        summary = DataSummary(dict_data)
        return summary

    pass

    @staticmethod
    def merge(*args):
        """
        将多部字典合并为一部字典
        :param dict args:
        :return:
        """
        result = {}
        for item in args:
            result.update(item)
        pass

        return result

    pass


pass
