from BasicLibrary.data.dictHelper import *
from BasicLibrary.data.objectHelper import *


class Container(object):
    """

    """

    dicts = dict()

    @staticmethod
    def get_item(name, default_value=None):
        """
        获取在系统内全局静态使用的词典
        :param default_value:
        :param name: 如果参数为None，获取缺省的词典；如果指定名称，那么获取特定的词典（如果不存在，则新建一个）
        :return:
        """
        if ObjectHelper.is_empty(name):
            name = "__default__20210410__"
        pass

        if not DictHelper.is_contains_key(Container.dicts, name):
            Container.dicts[name] = default_value
        pass

        result = Container.dicts[name]
        return result

    @staticmethod
    def set_item(name, value):
        Container.dicts[name] = value

    @classmethod
    def get_dict(cls, name):
        """
        获取在系统内全局静态使用的词典
        :param name: 如果参数为None，获取缺省的词典；如果指定名称，那么获取特定的词典（如果不存在，则新建一个）
        :return:
        """
        default_value = dict()
        result = cls.get_item(name, default_value)

        if isinstance(result, dict):
            return result
        else:
            return None
        pass
