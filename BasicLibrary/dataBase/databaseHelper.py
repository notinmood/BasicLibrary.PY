from datetime import datetime, date

from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.data.objectHelper import ObjectHelper


class DatabaseHelper:
    """
    本模块，为各关系型数据库共用。
    其他非共用的功能，分别放入各种数据库驱动的Helper中，比如MongoDB/Helper，MySql/Helper
    """

    @classmethod
    def build_where_clause(cls, condition_dict):
        """
        构建Where语句
        :param condition_dict: 包含在Where内的过滤条件实体
        :return:
        """
        result = ""
        last_key = ""
        result = cls.__build_where_clause(condition_dict, last_key)

        result = StringHelper.remove_head(result, " ")
        result = StringHelper.remove_head(result, "AND")
        return result

    # TODO 类似$gt等更多的查找条件的处理
    @classmethod
    def __build_where_clause(cls, condition_dict, last_key):
        result = ""
        if condition_dict:
            for key in condition_dict:
                need_operator = False
                if StringHelper.is_contains(key, "$") is False:
                    last_key = key
                    need_operator = True
                pass

                if key == "$gte":
                    operator = " >= "
                pass

                if key == "$gt":
                    operator = " > "
                pass

                if key == "$lte":
                    operator = " <= "
                pass

                if key == "$lt":
                    operator = " < "
                pass

                if key == "$like":
                    operator = " like "
                pass

                value = condition_dict[key]
                if type(value) is dict:
                    result += cls.__build_where_clause(value, last_key)
                else:
                    value = cls.wrap_sql_value(value)

                    if need_operator:
                        result += " AND `{0}` = {1} ".format(last_key, value)
                    else:
                        result += " AND `{0}` {1} {2}".format(last_key, operator, value)
                    pass
                pass
            pass

        return result
        pass

    pass

    @classmethod
    def build_insert_clause(cls, table_name, entity_dict_or_list):
        """
        构建Insert语句
        :param entity_dict_or_list: 插入的信息实体(Key-Value类型的词典),或者多个实体的list集合
        :param table_name: 待操作的数据库表名称
        :return:
        """
        if ObjectHelper.get_type(entity_dict_or_list) is dict:
            return cls.__build_insert_clause_detail(table_name, entity_dict_or_list)
        else:
            if ObjectHelper.get_type(entity_dict_or_list) is list:
                result = ""
                for item in entity_dict_or_list:
                    single_sql = cls.__build_insert_clause_detail(table_name, item)
                    single_sql = StringHelper.remove_tail(single_sql, ";")
                    if result:
                        values_sql = StringHelper.get_after_content(single_sql, "VALUES")
                        result += "," + values_sql
                    else:
                        result = single_sql
                    pass
                pass

                result = result + ";"
                return result
            else:
                return ""
            pass
        pass

    pass

    @classmethod
    def __build_insert_clause_detail(cls, table_name, entity_dict):
        """
        构建Insert语句
        :param entity_dict: 插入的信息实体(Key-Value类型的词典)
        :param table_name: 待操作的数据库表名称
        :return:
        """
        keys = ""
        values = ""
        for key in entity_dict:
            keys += "`{0}`,".format(key)
            values += cls.wrap_sql_value(entity_dict[key]) + ","
        pass

        if StringHelper.is_end_with(keys, ","):
            keys = keys[:-1]
            values = values[:-1]
        pass

        sql = "INSERT INTO `{0}` ({1}) VALUES ({2});".format(table_name, keys, values)
        return sql

    pass

    @classmethod
    def build_delete_clause(cls, table_name, condition_dict):
        """
        构建删除语句
        :param condition_dict: 包含在Where内的过滤条件实体
        :param table_name: 待操作的数据库的表名称
        :return:
        """
        sql = "DELETE FROM `{0}` ".format(table_name)
        if ObjectHelper.is_exist(condition_dict):
            where = cls.build_where_clause(condition_dict)
            sql += " WHERE " + where + ";"
        pass

        return sql

    pass

    @classmethod
    def build_update_clause(cls, table_name, fixing_dict, condition_dict):
        """
        构建更新语句
        :param fixing_dict: 待更新的实体数据
        :param condition_dict: 包含在Where内的过滤条件实体
        :param table_name: 待操作的数据库的表名称
        :return:
        """
        set_clause = ""
        for key in fixing_dict:
            value = cls.wrap_sql_value(fixing_dict[key])
            set_clause += "`{0}`={1},".format(key, value)
        pass

        if StringHelper.is_end_with(set_clause, ","):
            set_clause = set_clause[:-1]
        pass

        sql = "UPDATE `{0}` SET {1}".format(table_name, set_clause)
        if ObjectHelper.is_exist(condition_dict):
            where = cls.build_where_clause(condition_dict)
            sql += " WHERE " + where + ";"
        pass

        return sql

    pass

    @classmethod
    def build_select_clause(cls, table_name, condition_dict, data_field_collection=None):
        """
        构建数据提取语句
        :param condition_dict: 包含在Where内的过滤条件实体
        :param table_name: 待操作的数据库的表名称
        :param data_field_collection: 待提取数据的字段列表 list或者 集合set信息
        :return:
        """
        if ObjectHelper.is_empty(data_field_collection):
            data_field_collection = "*"
        else:
            data_field_collection = StringHelper.implode(data_field_collection)
        pass

        sql = "SELECT {0} FROM `{1}` ".format(data_field_collection, table_name)
        if ObjectHelper.is_exist(condition_dict):
            where_clause = cls.build_where_clause(condition_dict)
            sql += " WHERE " + where_clause
        pass

        return sql

    pass

    @classmethod
    def wrap_sql_value(cls, data):
        """
        处理SQL数据值信息
        :param data:
        :return:
        """
        _type = type(data)

        if data is None or _type is str or _type is datetime or _type is date:
            return '"{0}"'.format(data)
        else:
            return "{0}".format(data)
        pass

    pass


pass
