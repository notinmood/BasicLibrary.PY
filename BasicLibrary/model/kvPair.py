"""
 * @file   : kvPair.py
 * @time   : 10:42
 * @date   : 2021/12/30
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from datetime import datetime, date


class KVPair:
    """

    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def convert_to_dict_item(self, use_double_quotation=True):
        """
        转换成字典的 item
        :param use_double_quotation: 是否使用双引号标识key和value(True(默认值),使用双引号；False,使用单引号。)
        :return:
        """
        value = self.value
        value_type = type(value)
        if value_type is str or value_type is date or value_type is datetime:
            if use_double_quotation:
                return '"{0}":"{1}"'.format(self.key, value)
            else:
                return "'{0}':'{1}'".format(self.key, value)
        else:
            if use_double_quotation:
                return '"{0}":{1}'.format(self.key, value)
            else:
                return "'{0}':{1}".format(self.key, value)
