import threading
from timeit import default_timer

import pymysql

from hilandBasicLibrary.configHelper import ConfigHelper as ch
from hilandBasicLibrary.data.dictHelper import DictHelper
from hilandBasicLibrary.data.objectHelper import ObjectHelper
from hilandBasicLibrary.data.stringHelper import StringHelper
from hilandBasicLibrary.dataBase.databaseEnum import FetchMode, LikeMatchMode
from hilandBasicLibrary.dataBase.databaseHelper import DatabaseHelper
from hilandBasicLibrary.dataBase.databaseMate import DatabaseMate
from hilandBasicLibrary.dataBase.MySql.pool import Pool
from hilandBasicLibrary.environment.consoleHelper import ConsoleHelper

# TODO find_in find_or 尚未处理
lock = threading.Lock()


class Mate(DatabaseMate):
    def __init__(self, table_name, prefix_name=None):
        """

        :param table_name:
        :param prefix_name:
        """
        self._log_time = True
        self._commit = True
        self._log_label = '总用时'

        if prefix_name is None:
            prefix_name = ch.get_item("db_mysql", "table_prefix")

        if prefix_name:
            self._table_name = prefix_name + table_name
        else:
            self._table_name = table_name

        self.conn = None
        self.cursor = None

    def get_cursor(self):
        if self.cursor is None:
            self.__connect()
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return self.cursor

    def __connect(self):
        connections_pool = Pool()
        self.conn = connections_pool.get_conn()
        return self.conn

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def __enter__(self):

        # 如果需要记录时间
        if self._log_time is True:
            self._start = default_timer()

        # 在进入的时候自动获取连接和cursor
        conn = self.__connect()
        conn.autocommit = False
        self.get_cursor()

        return self

    def __exit__(self, *exc_info):

        # 提交事务
        if self._commit:
            self.conn.commit()
        # 在退出的时候自动关闭连接和cursor
        self.cursor.close()
        self.conn.close()

        if self._log_time is True:
            diff = default_timer() - self._start
            print('-- %s: %.6f 秒' % (self._log_label, diff))

    def __str__(self):
        return "mate in  DatabaseMate: " + __name__

    def get_real_table_name(self):
        """
        获取数据库表真正的名称(如果有数据库表名前缀，则包含前缀在内的完整数据库表名)
        :return:
        """
        return self._table_name

    def find_one(self, condition_dict, data_field={}):
        sql = DatabaseHelper.build_select_clause(self._table_name, condition_dict, data_field)
        return self.directly_query(sql, None, FetchMode.ONE)

    def find_many(self, condition_dict, data_field={}):
        sql = DatabaseHelper.build_select_clause(self._table_name, condition_dict, data_field)
        return self.directly_query(sql, None, FetchMode.MANY)

    def find_like(self, field, value, match_mode=LikeMatchMode.BOTH, data_field={}):
        """
        相识性查找
        :param field: 待匹配的字段
        :param value: 待匹配的值
        :param match_mode: 匹配模式，共三种 --before匹配前端相识；after匹配后端相识；both匹配中间相识
        :param data_field:
        :return:
        """
        data = dict()
        if match_mode == LikeMatchMode.BEFORE:
            match_value = value + '%'
        else:
            if match_mode == LikeMatchMode.AFTER:
                match_value = '%' + value
            else:
                match_value = '%' + value + '%'

        data = {field: {"$like": match_value}}

        return self.find_many(data, data_field)

    def find_between(self, field, value1, value2, include_border=True, data_field={}):
        """获取俩个值中间的数据"""
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$gte": value1, "$lte": value2}
        else:
            condition_dict[field] = {"$gt": value1, "$lt": value2}

        res = self.find_many(condition_dict, data_field)
        return res

    def find_more(self, field, value, include_border=True, data_field={}):
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$gte": value}
        else:
            condition_dict[field] = {"$gt": value}

        res = self.find_many(condition_dict, data_field)
        return res

    def find_less(self, field, value, include_border=True, data_field={}):
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$lte": value}
        else:
            condition_dict[field] = {"$lt": value}

        res = self.find_many(condition_dict, data_field)
        return res

    def query_count(self, condition_dict={}):
        """
        获取符合条件的行数
        :param condition_dict:
        :return:
        """
        sql = " SELECT count(1) as result FROM `{0}` ".format(self._table_name)
        where = DatabaseHelper.build_where_clause(condition_dict)
        if where:
            sql += " WHERE {0};".format(where)
        result = self.directly_query(sql)
        if result:
            return result["result"]
        else:
            return None

    def insert_one(self, entity_dict):
        sql = DatabaseHelper.build_insert_clause(self._table_name, entity_dict)
        return self.edit(sql, None)

    def insert_one_non_duplication(self, entity_dict, condition_dict=None):
        """
        跟collection内既有数据不重复的插入新数据（如果重复则跳过不插入）
        :param entity_dict: 待插入的document数据
        :param condition_dict: 是否重复的过滤条件，默认为None时取值data
        :return:
        """
        if ObjectHelper.is_empty(entity_dict):
            return None

        if condition_dict is None:
            condition_dict = entity_dict

        is_existing = self.find_one(condition_dict)
        if is_existing is None:
            return self.insert_one(entity_dict)
        else:
            return None

    def insert_many(self, entity_dict_list):
        row_count = 0
        need_execute_count = 0
        # TODO:配置到ini文件内
        execute_count_once = 100
        sql = ""
        for item in entity_dict_list:
            single_sql = DatabaseHelper.build_insert_clause(self._table_name, item)
            single_sql = StringHelper.remove_tail(single_sql, ";")
            if need_execute_count == 0:
                sql = single_sql
            else:
                temp = StringHelper.get_after_content(single_sql, "VALUES")
                sql += "," + temp

            need_execute_count = need_execute_count + 1

            if (need_execute_count >= execute_count_once) or item == entity_dict_list[-1]:
                row_count += self.edit(sql, None)
                need_execute_count = 0
                sql = ""

        return row_count

        # # 原来单行执行，但效率太低（一个晚上只能插入几万条数据）
        # row_count = 0
        # for item in entity_dict_list:
        #     sql = DatabaseHelper.build_insert_clause(item, self.table_name)
        #     row_count += self.__edit(sql, None, False)
        #
        # self.close()
        # return row_count

    def insert_many_non_duplication(self, entity_dict_list, condition_dict=None):
        """
        不重复的插入多行数据
        （目前实现的版本功能是，先查询数据库内是否有符合条件filter_condition的数据，如果有（哪怕只有一条），那么全部的新数据都不插入了；
        如果数据库内没有符合条件的记录，那么就插入新的全部数据data_list）
        :param entity_dict_list:
        :param condition_dict:
        :return:
        """
        if condition_dict is None:
            condition_dict = entity_dict_list

        exist_count = self.query_count(condition_dict)

        if exist_count and exist_count > 0:
            # do nothing;
            res = None
        else:
            res = self.insert_many(entity_dict_list)

        return res

    def update_one(self, fixing_dict, condition_dict):
        sql = DatabaseHelper.build_update_clause(self._table_name, fixing_dict, condition_dict)
        sql = StringHelper.remove_tail(sql, ";") + " LIMIT 1 ;"
        return self.edit(sql)

    def update_many(self, fixing_dict, condition_dict):
        sql = DatabaseHelper.build_update_clause(self._table_name, fixing_dict, condition_dict)
        return self.edit(sql)

    def interact_one(self, entity_dict, condition_dict=None, is_exist_update=True):
        """
        跟数据库服务器进行数据交互，如果设定条件的记录存在就更新；如果不存在就插入。
        :param entity_dict:
        :param condition_dict:
        :param is_exist_update: 在MySql下此参数不可使用
        :return:
        """
        if condition_dict is None:
            condition_dict = entity_dict

        data_existing = self.find_one(condition_dict)

        if data_existing:
            return self.update_one(entity_dict, condition_dict)
        else:
            return self.insert_one(entity_dict)

    def delete_one(self, condition_dict):
        sql = DatabaseHelper.build_delete_clause(self._table_name, condition_dict)
        sql = StringHelper.remove_tail(sql, ";") + " LIMIT 1 ;"

        return self.edit(sql)

    def delete_many(self, condition_dict):
        sql = DatabaseHelper.build_delete_clause(self._table_name, condition_dict)
        return self.edit(sql)

    # -----获取某字段中的最大值、最小值-------------------------------------------------
    def get_max(self, field_name, condition_dict=None):
        sql = "select MAX({0}) as result from `{1}`".format(field_name, self._table_name)
        where = DatabaseHelper.build_where_clause(condition_dict)
        if where:
            sql += " WHERE {0};".format(where)
        result = self.directly_query(sql)
        if result:
            return result["result"]
        else:
            return None

    def get_min(self, field_name, condition_dict=None):
        sql = "select MIN({0}) as result from `{1}`".format(field_name, self._table_name)
        where = DatabaseHelper.build_where_clause(condition_dict)
        if where:
            sql += " WHERE {0};".format(where)
        result = self.directly_query(sql)
        if result:
            return result["result"]
        else:
            return None

    def directly_exec(self, sql, params=None, auto_close=True):
        try:
            return self.__exec_detail(sql, params)
        except pymysql.ProgrammingError:
            print("数据库连接错误，重试中...")
            self.__connect()
            return self.__exec_detail(sql, params)

    def __exec_detail(self, sql, params):
        cursor = self.get_cursor()
        count = 0
        try:
            lock.acquire()
            count = cursor.execute(sql, params)
            self.conn.commit()
            lock.release()
        except Exception as e:
            print(e)
        return count

    def directly_query(self, sql, params=None, fetch_mode=FetchMode.ONE):
        try:
            return self.__query_detail(sql, params, fetch_mode)
        except pymysql.ProgrammingError:
            ConsoleHelper.echo("数据库连接错误，重试中...")
            self.__connect()
            return self.__query_detail(sql, params, fetch_mode)

    def __query_detail(self, sql, params=None, fetch_mode=FetchMode.ONE):
        cursor = self.get_cursor()
        result = None

        lock.acquire()

        cursor.execute(sql, params)
        if fetch_mode == FetchMode.ONE:
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        lock.release()

        return result


