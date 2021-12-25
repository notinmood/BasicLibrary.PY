from hilandBasicLibrary.data.dictHelper import *
from hilandBasicLibrary.data.objectHelper import *


class Container(object):
    dicts = dict()

    @staticmethod
    def get_dict(name: object = None) -> object:
        """
        获取在系统内全局静态使用的词典
        :param name: 如果参数为None，获取缺省的词典；如果指定名称，那么获取特定的词典（如果不存在，则新建一个）
        :return:
        """
        if ObjectHelper.is_empty(name):
            name = "__default__20210410"

        if not DictHelper.is_contains_key(Container.dicts, name):
            _dict = dict()
            Container.dicts[name] = _dict

        result = Container.dicts[name]
        if isinstance(result, dict):
            return result
        else:
            return None
