from builtins import *

from hiland.dataBase import MongoDBHelper as mh, DatabaseMate


class Mate(DatabaseMate.Mate):
    """ 各种query 中的数据 data 和 mongodb 文档中的一样"""

    def __init__(self, collection_name, database_name='', host='', port=0):
        self.collection = mh.get_using_collection(collection_name, database_name, host, port)

    def interact_one(self, entity_dict, condition_dict=None, is_exist_update=True):
        if condition_dict is None:
            condition_dict = entity_dict

        data_existing = mh.find_one(self.collection, condition_dict)

        if data_existing:
            if is_exist_update:
                return self.collection.update_one(condition_dict, {"$set": entity_dict})
            else:
                return self.collection.replace_one(data_existing, entity_dict)
        else:
            return self.collection.insert_one(entity_dict)

    def insert_one(self, entity_dict):
        res = mh.insert_one(self.collection, entity_dict)
        return res

    def insert_one_non_duplication(self, entity_dict, condition_dict=None):
        """
        跟collection内既有数据不重复的插入新数据（如果重复则跳过不插入）
        :param entity_dict: 待插入的document数据
        :param condition_dict: 是否重复的过滤条件，默认为None时取值data
        :return:
        """
        if condition_dict is None:
            condition_dict = entity_dict

        is_existing = mh.find_one(self.collection, condition_dict)
        if is_existing is None:
            return mh.insert_one(self.collection, entity_dict)
        else:
            return None

    def insert_many(self, data_list):
        res = mh.insert_many(self.collection, data_list)
        return res

    def insert_many_non_duplication(self, data_list, condition_dict=None):
        """
        不重复的插入多行数据
        （目前实现的版本功能是，先查询数据库内是否有符合条件filter_condition的数据，如果有（哪怕只有一条），那么全部的新数据都不插入了；
        如果数据库内没有符合条件的记录，那么就插入新的全部数据data_list）
        :param data_list:
        :param condition_dict:
        :return:
        """
        if condition_dict is None:
            condition_dict = data_list

        exist_count = self.query_count(condition_dict)

        if exist_count and exist_count > 0:
            # do nothing;
            res = None
        else:
            res = mh.insert_many(self.collection, data_list)

        return res

    #  ========================= Query Documents Start =========

    def find_one(self, condition_dict, data_field={}):
        res = mh.find_one(self.collection, condition_dict, data_field)
        return res

    def find_many(self, condition_dict, data_field={}):
        """ 有多个键值的话就是 AND 的关系"""
        res = mh.find_many(self.collection, condition_dict, data_field)

        return list(res)

    # def find_all(self, data={}, data_field={}):
    #     """select * from table"""
    #     res = mh.find_many(self.collection, data, data_field)
    #     return res

    def find_in(self, field, item_list, data_field={}):
        """SELECT * FROM inventory WHERE status in ("A", "D")"""
        data = dict()
        data[field] = {"$in": item_list}
        res = self.find_many(self.collection, data, data_field)
        return res

    def find_or(self, data_list, data_field={}):
        """db.inventory.find(
    {"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})

        SELECT * FROM inventory WHERE status = "A" OR qty < 30
        """
        data = dict()
        data["$or"] = data_list
        res = self.find_many(self.collection, data, data_field)
        return res

    def find_between(self, field, value1, value2, include_border=True, data_field={}):
        """获取俩个值中间的数据"""
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$gte": value1, "$lte": value2}
        else:
            condition_dict[field] = {"$gt": value1, "$lt": value2}

        res = self.find_many(self.collection, condition_dict, data_field)
        return res

    def find_more(self, field, value, include_border=True, data_field={}):
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$gte": value}
        else:
            condition_dict[field] = {"$gt": value}
        res = self.find_many(self.collection, condition_dict, data_field)
        return res

    def find_less(self, field, value, include_border=True, data_field={}):
        condition_dict = dict()
        if include_border:
            condition_dict[field] = {"$lte": value}
        else:
            condition_dict[field] = {"$lt": value}
        res = self.find_many(self.collection, condition_dict, data_field)
        return res

    def find_like(self, field, value, match_mode='both', data_field={}):
        """
        相识性查找
        :param field: 待匹配的字段
        :param value: 待匹配的值
        :param match_mode: 匹配模式，共三种 --before匹配前端相识；after匹配后端相识；both匹配中间相识
        :param data_field:
        :return:
        """
        condition_dict = dict()
        if match_mode == 'before':
            match_value = value + '.*'
        else:
            if match_mode == 'after':
                match_value = '.*' + value
            else:
                match_value = '.*' + value + '.*'

        condition_dict[field] = {'$regex': match_value}
        res = self.find_many(self.collection, condition_dict, data_field)

        return res

    def query_count(self, condition_dict={}):
        res = self.collection.count_documents(condition_dict)
        return res

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
        res = mh.delete_one(self.collection, condition_dict)
        return res

    def delete_many(self, condition_dict):
        """ 删除查到的多个数据 data 是一个字典 """
        res = mh.delete_many(self.collection, condition_dict)
        return res

    # --------改变表的结构--------------------------
    def alter_add_fields(self, fields_name_value_dict, condition_dict={}):
        """

        :param fields_name_value_dict: 需要添加的字段名称与值的字典
        :param condition_dict:
        :return:
        """
        self.collection.update_many(condition_dict, {"$set": fields_name_value_dict})

    def alter_remove_fields(self, fields_name_list, condition_dict={}):
        """
        移除字段
        :param fields_name_list: 需要移除的字段名称信息（数据类型可以是list，set，dict）
        :param condition_dict:
        :return:
        """
        fields_dict = {}
        _type = type(fields_name_list)

        if _type == dict:
            fields_dict = fields_name_list

        if _type == list or _type == set:
            for x in fields_name_list:
                fields_dict[x] = ""

        self.collection.update_many(condition_dict, {"$unset": fields_dict})

    def alter_rename_fields(self, fields_old_new_name_dict, condition_dict={}):
        self.collection.update_many(condition_dict, {"$rename": fields_old_new_name_dict})

    # -----获取某字段中的最大值、最小值-------------------------------------------------
    def get_max(self, field_name, condition_dict=None):
        return self.__get_terminal_value(field_name, condition_dict, "MAX")

    def get_min(self, field_name, condition_dict=None):
        return self.__get_terminal_value(field_name, condition_dict, "MIN")

    def __get_terminal_value(self, field_name, condition_dict=None, terminal_type="MAX"):
        field_name = "$" + field_name
        if terminal_type.lower() == "max":
            terminal_type = "$max"
        else:
            terminal_type = "$min"

        agg_expression = [{"$group": {"_id": "id", "result": {terminal_type: field_name}}}]
        if condition_dict != "" and condition_dict is not None:
            agg_expression.insert(0, {"$match": condition_dict})

        _temp_cursor = self.collection.aggregate(agg_expression)

        _list = list(_temp_cursor)

        if _list is not None and len(_list) > 0:
            _first = _list[0]
            return _first["result"]
        else:
            return None


if __name__ == '__main__':
    # person = DataPersonClient()
    person = Mate("person")
    _data = {
        "weixin": [
            {
                "name": "开源优测",
                "uid": "DeepTest",
                "desc": "分享开源测试技术"
            },
            {
                "name": "开源优测_demo",
                "uid": "DeepTest_demo",
                "desc": "分享开源测试技术_demo"
            }
        ],
        "web": [
            {
                "url": "www.testingunion.com",
                "name": "开源优测社区",
                "desc": "分享各类开源测试技巧"
            },
            {
                "url": "www.testingunion.com_demo",
                "name": "开源优测社区_demo",
                "desc": "分享各类开源测试技巧_demo"
            }
        ]
    }

    # for k, v in _data.items():
    #     for item in v:
    #         person.insert_one(item)

    f = person.find_like("name", "开源", {"name"})
    print(list(f))

    _condition = {'name': '开源优测'}
    count = person.query_count(_condition)
    print(count)
