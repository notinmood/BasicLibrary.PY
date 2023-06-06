"""
 * @file   : ddl.py
 * @time   : 20:20
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.dictHelper import DictHelper
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.dataBase.databaseClient import DatabaseClient
from BasicLibrary.dataBase.databaseDDL import DatabaseDDL
from BasicLibrary.dataBase.databaseEnum import BatchMode
from BasicLibrary.dataBase.databaseHelper import DatabaseHelper


class DDL(DatabaseDDL):
    """

    """

    def duplicate_table(self, original_table_name, new_table_name="", include_data_row_count=0,
                        drop_table_if_exist=True):
        """
        复制数据表
        :param drop_table_if_exist: 目标表如果存在，是否要先删除(True，删除目标表（缺省值）；False，保留目标表)
        :param original_table_name:
        :param new_table_name:
        :param include_data_row_count:复制数据的行数(缺省0，表示不复制数据行;-1表示复制所有行)
        :return:
        """
        if StringHelper.is_empty(new_table_name):
            new_table_name = original_table_name + "__dupl"

        if drop_table_if_exist:
            self.drop_table(new_table_name, True)

        """
        在ddl_get_table_definition方法内完成了目标数据表是否已经存在的判断
        """
        create_sql = self.get_table_definition(original_table_name)

        # TODO:需要使用正则表达式替换
        create_sql = str.replace(create_sql, original_table_name, new_table_name)

        mate = DatabaseClient.get_mate(original_table_name)
        mate.directly_exec(create_sql)

        insert_sql = self.get_content_sql(original_table_name, include_data_row_count)
        insert_sql = str.replace(insert_sql, original_table_name, new_table_name)
        if insert_sql:
            mate.directly_exec(insert_sql)

    def drop_table(self, table_name, both_struct_and_data=True):
        mate = DatabaseClient.get_mate(table_name)
        real_table_name = mate.get_real_table_name()
        is_exist = self.is_exist_table(table_name)

        """
        在不存在的表上，执行删除操作，系统会报错。因此本处需要做出是否存在的判断。
        """
        if is_exist:
            if both_struct_and_data:
                sql = "drop table `{0}`".format(real_table_name)
            else:
                sql = "truncate table `{0}`".format(real_table_name)

            mate.directly_exec(sql)

    def get_content_sql(self, table_name, row_count=-1):
        """
        获取数据表数据内容的插入sql语句
        :param row_count:复制数据的行数(-1表示所有的行数，0-n表示具体行数)
        :param table_name:
        :return:
        """
        mate = DatabaseClient.get_mate(table_name)
        real_table_name = mate.get_real_table_name()

        if row_count < 0:
            select_sql = "SELECT * FROM `{0}`".format(real_table_name)

            # TODO:需要改成参数调用的方式
            # select_sql = "SELECT * FROM %s"
            # rows = mate.directly_query(select_sql, [real_table_name], FetchMode.MANY)
        else:
            select_sql = "SELECT * FROM `{0}` LIMIT {1}".format(real_table_name, row_count)

        rows = mate.directly_query(select_sql, None, BatchMode.MANY)

        result = ""
        if rows:
            result = DatabaseHelper.build_insert_clause(real_table_name, rows)

        return result

    def is_exist_table(self, table_name):
        """
        判断某个表是否存在
        :param table_name:
        :return:
        """

        mate = DatabaseClient.get_mate(table_name)
        real_table_name = mate.get_real_table_name()
        sql = "SHOW TABLES like '{0}';".format(real_table_name)
        result = mate.directly_query(sql)

        if result is None:
            return False
        else:
            return DictHelper.is_contains_value(result, real_table_name)

    def get_table_definition(self, table_name):
        """
        获取表的定义语句
        :param table_name: 数据库表的名称
        :return:
        """
        mate = DatabaseClient.get_mate(table_name)
        real_table_name = mate.get_real_table_name()

        sql = "show create table `{0}`".format(real_table_name)
        result = mate.directly_query(sql)

        result = DictHelper.get_value(result, "Create Table")
        # TODO: 需要加入大小写字母判断
        result = str.replace(result, "CREATE TABLE", "CREATE TABLE if not exists")
        return result
