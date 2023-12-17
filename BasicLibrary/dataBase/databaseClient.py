"""
 * @file   : databaseDDL.py
 * @time   : 20:17
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.configHelper import ConfigHelper as ch
from BasicLibrary.data.dictHelper import DictHelper
from BasicLibrary.dataBase.databaseDDL import DatabaseDDL
from BasicLibrary.dataBase.databaseMate import DatabaseMate
from BasicLibrary.model.container import Container


class DatabaseClient:
    """
    向外暴露的主要类型接口
    """

    @classmethod
    def __get_db_type_name(cls):
        type_name = ch.get_item("db_type", "type_name", "MySql")
        return type_name

    @classmethod
    def get_mate(cls, table_name):
        """
        这是向外暴露的主要方法接口
        获取跟数据库（表信息）交互的对象
        :param table_name:
        :return:
        """
        mate_dict = Container.get_dict("mate_dict")

        if DictHelper.is_contains_key(mate_dict, table_name):
            return mate_dict[table_name]
        else:
            type_name = cls.__get_db_type_name()
            package_name = "hilandBasicLibrary.dataBase.{0}.mate".format(type_name)
            module = __import__(package_name, fromlist=["Mate"])

            mate = module.Mate(table_name)
            mate_dict[table_name] = mate

            if isinstance(mate, DatabaseMate):
                return mate
            else:
                return None
            pass
        pass
    pass

    @classmethod
    def get_ddl(cls):
        """
        这是向外暴露的操作数据库结构的方法接口
        :return:
        """
        ddl_key = "__database_ddl__"
        ddl = Container.get_item(ddl_key)

        if ddl is None:
            ddl = cls.__get_ddl_detail()
            Container.set_item(ddl_key, ddl)
        pass

        if isinstance(ddl, DatabaseDDL):
            return ddl
        else:
            return None
    pass

    @classmethod
    def __get_ddl_detail(cls):
        type_name = cls.__get_db_type_name()
        package_name = "hilandBasicLibrary.dataBase.{0}.ddl".format(type_name)
        module = __import__(package_name, fromlist=["DDL"])
        ddl = module.DDL()
        return ddl
    pass

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
