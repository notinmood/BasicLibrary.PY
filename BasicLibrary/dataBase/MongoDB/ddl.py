"""
 * @file   : ddl.py
 * @time   : 23:19
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.dataBase.databaseDDL import DatabaseDDL

"""
TODO:这个文件需要处理 collection 从哪里来需要优化思路
"""


class DDL(DatabaseDDL):
    """

        """

    def add_fields(self, fields_name_value_dict, condition_dict={}):
        """

        :param fields_name_value_dict: 需要添加的字段名称与值的字典
        :param condition_dict:
        :return:
        """
        # self.collection.update_many(condition_dict, {"$set": fields_name_value_dict})
        pass

    def remove_fields(self, fields_name_list, condition_dict={}):
        """
        移除字段
        :param fields_name_list: 需要移除的字段名称信息（数据类型可以是list，set，dict）
        :param condition_dict:
        :return:
        """
        # fields_dict = {}
        # _type = type(fields_name_list)
        #
        # if _type == dict:
        #     fields_dict = fields_name_list
        #
        # if _type == list or _type == set:
        #     for x in fields_name_list:
        #         fields_dict[x] = ""

        # self.collection.update_many(condition_dict, {"$unset": fields_dict})
        pass

    def rename_fields(self, fields_old_new_name_dict, condition_dict={}):
        # self.collection.update_many(condition_dict, {"$rename": fields_old_new_name_dict})
        pass
