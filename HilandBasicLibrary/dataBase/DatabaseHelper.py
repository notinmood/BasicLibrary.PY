from datetime import datetime, date
from builtins import *

from hiland.data import StringHelper, ObjectHelper

"""
    本模块，为各关系型数据库共用。
    其他非共用的功能，分别放入各种的Helper中，比如MongoDBHelper，MsSqlHelper
"""


def build_where_clause(condition_dict):
    result = ""
    last_key = ""
    result = __build_where_clause(condition_dict, result, last_key)

    result = StringHelper.remove_head(result, " ")
    result = StringHelper.remove_head(result, "AND")
    return result


# TODO 类似$gt等更多的查找条件的处理
def __build_where_clause(condition_dict, result, last_key):
    result = ""
    if condition_dict:
        for key in condition_dict:
            need_operator = False
            if StringHelper.is_contains(key, "$") is False:
                last_key = key
                need_operator = True

            if key == "$gte":
                operator = " >= "

            if key == "$gt":
                operator = " > "

            if key == "$lte":
                operator = " <= "

            if key == "$lt":
                operator = " < "

            if key == "$like":
                operator = " like "

            value = condition_dict[key]
            if type(value) is dict:
                result += __build_where_clause(value, result, last_key)
            else:
                value = wrap_sql_value(value)

                if need_operator:
                    result += " AND `{0}` = {1} ".format(last_key, value)
                else:
                    result += " AND `{0}` {1} {2}".format(last_key, operator, value)

    return result


def build_insert_clause(entity_dict, table_name):
    keys = ""
    values = ""
    for key in entity_dict:
        keys += "`{0}`,".format(key)
        values += wrap_sql_value(entity_dict[key]) + ","

    if StringHelper.is_end_with(keys, ","):
        keys = keys[:-1]
        values = values[:-1]

    sql = "INSERT INTO `{0}` ({1}) VALUES ({2});".format(table_name, keys, values)
    return sql


def build_delete_clause(condition_dict, table_name):
    sql = "DELETE FROM `{0}` ".format(table_name)
    if ObjectHelper.is_exist(condition_dict):
        where = build_where_clause(condition_dict)
        sql += " WHERE " + where + ";"
    return sql


def build_update_clause(fixing_dict, condition_dict, table_name):
    set_clause = ""
    for key in fixing_dict:
        value = wrap_sql_value(fixing_dict[key])
        set_clause += "`{0}`={1},".format(key, value)

    if StringHelper.is_end_with(set_clause, ","):
        set_clause = set_clause[:-1]

    sql = "UPDATE `{0}` SET {1}".format(table_name, set_clause)
    if ObjectHelper.is_exist(condition_dict):
        where = build_where_clause(condition_dict)
        sql += " WHERE " + where + ";"
    return sql


def build_select_clause(condition_dict, table_name, data_field_collection={}):
    if is_empty(data_field_collection):
        data_field_collection = "*"
    else:
        data_field_collection = StringHelper.implode(data_field_collection)

    sql = "SELECT {0} FROM `{1}` ".format(data_field_collection, table_name)
    if ObjectHelper.is_exist(condition_dict):
        where_clause = build_where_clause(condition_dict)
        sql += " WHERE " + where_clause

    return sql


def wrap_sql_value(data):
    _type = type(data)
    if ObjectHelper.is_nan(data):
        data = None

    if data is None or _type is str or _type is datetime or _type is date:
        return '"{0}"'.format(data)
    else:
        return "{0}".format(data)


if __name__ == '__main__':
    _entity_dict = {"a": "A", "b": "B", "c": 1}
    _sql = build_insert_clause(_entity_dict, "my_table")
    print(_sql)

    # _dict = {"a": "A", "b": "B", "c": {"$gt": 50, "$lt": 80}}
    # aa = convert_dict_data_to_sql_where(_dict)
    # print(aa)
