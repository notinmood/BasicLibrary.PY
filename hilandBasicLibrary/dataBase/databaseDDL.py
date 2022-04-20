"""
 * @file   : databaseDDL.py
 * @time   : 20:17
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class DatabaseDDL(object):
    """

    """
    def duplicate_table(self, original_table_name, new_table_name="", include_data_row_count=0):
        """
        复制数据表
        :param original_table_name:
        :param new_table_name:
        :param include_data_row_count:复制数据的行数(缺省0，表示不复制数据行;-1表示复制所有行)
        :return:
        """
        pass

    def drop_table(self, table_name, both_struct_and_data=True):
        """
        删除数据表
        :param table_name:
        :param both_struct_and_data: 是否同时删除表结构和数据(true(缺省值)全部删除;false仅删除数据，保留表结构)
        :return:
        """
        pass

    def get_content_sql(self, table_name, row_count=-1):
        """
        获取数据表数据内容的插入sql语句
        :param row_count:复制数据的行数(-1表示所有的行数，0-n表示具体行数)
        :param table_name:
        :return:
        """
        pass

    def is_exist_table(self, table_name):
        """
        判断某个表是否存在
        :param table_name:
        :return:
        """
        pass

    def add_fields(self, fields_name_value_dict, condition={}):
        """
        :param fields_name_value_dict: 需要添加的字段名称与值的字典
        :param condition:
        :return:
        """
        pass

    def remove_fields(self, fields_name_list, condition={}):
        """
        移除字段
        :param fields_name_list: 需要移除的字段名称信息（数据类型可以是list，set，dict）
        :param condition:
        :return:
        """
        pass

    def rename_fields(self, fields_old_new_name_dict, condition={}):
        pass

    def get_table_definition(self, table_name=None):
        """
        获取表的定义语句
        :param table_name: 数据库表的名称,如果为None的话就直接从mate的构造函数中取数据库表名称
        :return:
        """
        pass
