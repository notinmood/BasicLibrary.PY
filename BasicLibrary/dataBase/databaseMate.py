from BasicLibrary.dataBase.databaseEnum import BatchMode, LikeMatchMode


class DatabaseMate(object):
    """
    TODO： 各个继承的子类中，insert_one,insert_many的返回值类型和意义必须统一
    数据库交互器(跟数据库内数据交互的唯一接口)
    """

    def get_real_table_name(self):
        """
        获取数据库表真正的名称(如果有数据库表名前缀，则包含前缀在内的完整数据库表名)
        :return:
        """
        pass

    def interact_one(self, data_dict, condition_dict=None, is_exist_update=True):
        pass

    def insert_one(self, data_dict):
        pass

    def insert_one_non_duplication(self, data_dict, filter_condition=None):
        """
        跟 collection 内既有数据不重复的插入新数据（如果重复则跳过不插入）
        :param data_dict: 待插入的 document 数据
        :param filter_condition: 是否重复的过滤条件，默认为 None 时取值 data_dict
        :return:
        """
        pass

    def insert_many(self, data_dict_list):
        pass

    def insert_many_non_duplication(self, data_dict_list, filter_condition=None):
        """
        不重复的插入多行数据
        （目前实现的版本功能是，先查询数据库内是否有符合条件filter_condition的数据，如果有（哪怕只有一条），那么全部的新数据都不插入了；
        如果数据库内没有符合条件的记录，那么就插入新的全部数据data_list）
        :param data_dict_list:
        :param filter_condition:
        :return:
        """
        pass

    def update_one(self, fixing_dict, condition_dict):
        """
        更新一条记录
        :param dict fixing_dict: 更新后的对象
        :param dict condition_dict: 更新时的匹配条件
        :return int:更新的数据条数
        """
        pass

    def update_many(self, fixing_dict, condition_dict):
        pass

    #  ========================= Query Documents Start =========
    def find_one(self, condition_dict, data_field_collection=None):
        pass

    def find_many(self, condition_dict, data_field_collection=None):
        """ 有多个键值的话就是 AND 的关系"""
        pass

    def find_in(self, field, item_list, data_field_collection=None):
        """SELECT * FROM inventory WHERE status in ("A", "D")"""
        pass

    def find_or(self, data_list, data_field_collection=None):
        """
        """
        pass

    def find_between(self, field, value_left, value_right, include_border=True, data_field_collection=None):
        """
        获取两个值中间的数据
        :param field:
        :param value_left:
        :param value_right:
        :param include_border:
        :param data_field_collection:
        :return:
        """
        pass

    def find_more(self, field, value, include_border=True, data_field_collection=None):
        pass

    def find_less(self, field, value, include_border=True, data_field_collection=None):
        pass

    def find_like(self, field, value, match_mode=LikeMatchMode.BOTH, data_field_collection=None):
        """
        相识性查找
        :param field: 待匹配的字段
        :param value: 待匹配的值
        :param match_mode: 匹配模式，共三种 --before匹配前端相识；after匹配后端相识；both匹配中间相识
        :param data_field_collection:
        :return:
        """
        pass

    def find_count(self, condition={}):
        pass

    # # ==以下几个query方法尚未验证========================================================
    # def query_limit(self, query, num):
    #     """db.collection.find(<query>).limit(<number>) 获取指定数据"""
    #     res = query.limit(num)
    #
    #     return res
    #
    # def query_skip(self, query, num):
    #     res = query.skip(num)
    #     return res
    #
    # def query_sort(self, query, data):
    #     """db.orders.find().sort( { amount: -1 } ) 根据amount 降序排列"""
    #     res = query.sort(data)
    #     return res
    #
    # # ================================================================================

    def delete_one(self, condition_dict):
        """ 删除单行数据 如果有多个 则删除第一个"""
        pass

    def delete_many(self, condition_dict):
        """ 删除查到的多个数据 data 是一个字典 """
        pass

    # --------直接跟数据库交互(业务逻辑内不推荐使用)----
    def directly_exec(self, sql, params=None, auto_close=True):
        """
        直接在数据库上执行sql语句(不推荐在biz的业务逻辑中直接使用)
        :param sql:
        :param params:
        :param auto_close:
        :return:
        """
        pass

    def directly_query(self, sql, params=None, fetch_mode=BatchMode.ONE):
        """
        直接在数据库上查询sql语句(不推荐在biz的业务逻辑中直接使用)
        :param sql:
        :param params:
        :param fetch_mode:
        :return:
        """
        pass

    # --------改变表的结构--------------------------
    """
    改变表结构的语句已经迁移到databaseDLL.py中
    """

    # -----获取某字段中的最大值、最小值-------------------------------------------------
    def get_max(self, field_name, condition_dict=None):
        pass

    def get_min(self, field_name, condition_dict=None):
        pass
