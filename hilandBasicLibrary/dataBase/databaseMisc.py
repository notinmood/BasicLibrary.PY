"""
 * @file   : databaseMisc.py
 * @time   : 16:54
 * @date   : 2021/12/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseClient import DatabaseClient as client
from hilandBasicLibrary.data.stringHelper import StringHelper
from hilandBasicLibrary.dataBase.databaseEnum import FetchMode
from hilandBasicLibrary.dataBase.databaseHelper import DatabaseHelper


class DatabaseMisc:

    @staticmethod
    def create_table_duplicate(original_table_name, new_table_name="", include_data_row_count=0):
        """
        复制数据表
        :param original_table_name:
        :param new_table_name:
        :param include_data_row_count:复制数据的行数(缺省0，表示不复制数据行)
        :return:
        """
        mate = client.get_mate(original_table_name)
        create_sql = mate.ddl_get_table_definition()
        if StringHelper.is_empty(new_table_name):
            new_table_name = original_table_name + "__dupl"

        # TODO:需要使用正则表达式替换
        create_sql = str.replace(create_sql, original_table_name, new_table_name)
        mate.directly_exec(create_sql)
        # TODO:include_data为True到时候，导入数据

    @staticmethod
    def get_content_sql(table_name, row_count=-1):
        """
        获取数据表数据内容的插入sql语句
        :param row_count:复制数据的行数(-1表示所有的行数，0-n表示具体行数)
        :param table_name:
        :return:
        """
        mate = client.get_mate(table_name)
        real_table_name = mate.get_real_table_name()

        if row_count < 0:
            select_sql = "SELECT * FROM `{0}`".format(real_table_name)
            rows = mate.directly_query(select_sql, None, FetchMode.MANY)

            # TODO:需要改成参数调用的方式
            # select_sql = "SELECT * FROM %s"
            # rows = mate.directly_query(select_sql, [real_table_name], FetchMode.MANY)
        else:
            select_sql = "SELECT * FROM `{0}` LIMIT {1}".format(real_table_name, row_count)
            rows = mate.directly_query(select_sql, None, FetchMode.MANY)

        result = ""
        if rows:
            for item in rows:
                result += DatabaseHelper.build_insert_clause(item, real_table_name)

        return result

    @staticmethod
    def drop_table(table_name, both_struct_and_data=True):
        mate = client.get_mate(table_name)
        table_name = mate.get_real_table_name()
        sql = ""
        if both_struct_and_data:
            sql = "drop table `{0}`".format(table_name)
        else:
            sql = "truncate table `{0}`".format(table_name)

        mate.directly_exec(sql)
