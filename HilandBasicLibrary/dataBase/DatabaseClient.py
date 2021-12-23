from builtins import *
from builtins import __import__

from HilandBasicLibrary.ConfigHelper import ConfigHelper as ch
from HilandBasicLibrary.data.DictHelper import DictHelper


class _MateContainer(object):
    mate_dict = {}


class DatabaseClient:
    @classmethod
    def __get_db_type_name(cls):
        type_name = ch.get_config_item("db_type", "type_name", "MySql")
        return type_name

    @classmethod
    def get_mate(cls, table_name):
        """
        这是向外暴露的主要接口
        获取跟数据库（表信息）交互的对象
        :param table_name:
        :return:
        """
        if DictHelper.is_contains_key(_MateContainer.mate_dict, table_name):
            return _MateContainer.mate_dict[table_name]
        else:
            type_name = cls.__get_db_type_name()
            package_name = "HilandBasicLibrary.dataBase.{0}.Mate".format(type_name)
            module = __import__(package_name, fromlist=["Mate"])

            # print(module)

            # module = getattr(module, type_name)
            #
            mate = module.Mate(table_name)
            _MateContainer.mate_dict[table_name] = mate

            return mate

# if __name__ == '__main__':
#     print(__MateContainer.mate_dict)
#     __MateContainer.mate_dict['a'] = 'AA'
#     __MateContainer.mate_dict['b'] = 'BB'
#     print(__MateContainer.mate_dict)
#
#     result = DictHelper.contain_key(__MateContainer.mate_dict, 'c')
#     print(result)
#     result = DictHelper.contain_key(__MateContainer.mate_dict, 'b')
#     print(result)
#     # print(AAA)
#     # print(AAA())

# _mate = get_mate("dp_demo")
# _mate.hello("Mr.Xie")

# _result = _mate.find_one({"class": "一", "age": {"$gt": 20}})
# print(_result)
#
# _result = _mate.find_many({"class": "一"})
# print(_result)

# _entity_data = {"name": "宋8", "age": 28, "class": "三"}
# _result = _mate.insert_one(_entity_data)
# print(_result)

# _entity_list = [{"name": "宋10", "age": 28, "class": "三"}, {"name": "宋11", "age": 28, "class": "三"}, {"name": "宋12", "age": 28, "class": "三"}]
# _result = _mate.insert_many(_entity_list)
# print(_result)

# _condition = {"name": "宋8"}
# _result = _mate.delete_many(_condition)
# print(_result)

# _condition = {"name": "宋8"}
# _result = _mate.delete_one(_condition)
# print(_result)

# _condition = {"name": "宋10"}
# _fixing = {"age": 32}
# _result = _mate.update_many(_fixing, _condition)
# print(_result)

# _condition = {"name": "宋10"}
# _fixing = {"age": 32}
# _result = _mate.update_one(_fixing, _condition)
# print(_result)

# _condition = {"name": "宋10"}
# _condition = {}
# _result = _mate.query_count(_condition)
# print(_result)

# _condition = {"name": "宋30"}
# _entity = {"name": "宋30", "age": 28, "class": "三"}
# _result = _mate.insert_one_non_duplication(_entity, _condition)
# print(_result)

# _condition = {"name": "宋31"}
# _entity = [{"name": "宋31", "age": 28, "class": "三"}, {"name": "宋32", "age": 29, "class": "三"}]
# _result = _mate.insert_many_non_duplication(_entity, _condition)
# print(_result)

# _result = _mate.get_max("age", {"name": "宋12"})
# print(_result)
#
# _result = _mate.get_min("age")
# print(_result)
#
# _result = _mate.get_min("age", {"name": "宋10"})
# print(_result)

# _result = _mate.find_like("name", "宋1", "before")
# print(_result)
#
# _result = _mate.find_like("name", "五", "after")
# print(_result)
#
# _result = _mate.find_like("name", "五")
# print(_result)

# _result = _mate.find_more("age", 25)
# print(_result)
# _result = _mate.find_less("age", 25)
# print(_result)
# _result = _mate.find_between("age", 25, 29)
# print(_result)

# type_name = __get_db_type_name() + "Mate"
# module = __import__(type_name)
# _mate = module.Mate
# _mate.hello("China")
