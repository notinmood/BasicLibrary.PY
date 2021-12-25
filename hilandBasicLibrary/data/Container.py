from hilandBasicLibrary.data.DictHelper import *
from hilandBasicLibrary.data.ObjectHelper import *


class Container(object):
    dicts = dict()

    @staticmethod
    def get_dict(name=None):
        """
        获取在系统内全局静态使用的词典
        :param name: 如果参数为None，获取缺省的词典；如果指定名称，那么获取特定的词典（如果不存在，则新建一个）
        :return:
        """
        if ObjectHelper.is_empty(name):
            name = "__default__20210410"

        if not DictHelper.contain_key(Container.dicts, name):
            _dict = dict()
            Container.dicts[name] = _dict

        return Container.dicts[name]
