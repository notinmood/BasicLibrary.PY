"""
 * @file   : test_DatabaseMisc.py
 * @time   : 17:24
 * @date   : 2021/12/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.stringHelper import StringHelper
from hilandBasicLibrary.dataBase.databaseClient import DatabaseClient

"""
测试前，请确保数据库内有如下文件内的表和数据：
1. _database_demo_data.sql
"""


def test_is_exist_table():
    ddl = DatabaseClient.get_ddl()
    actual = ddl.is_exist_table("user")
    expected = True
    assert actual == expected

    actual = ddl.is_exist_table("user2_my__")
    expected = False
    assert actual == expected


def test_ddl_get_table_definition():
    ddl = DatabaseClient.get_ddl()
    definition = ddl.ddl_get_table_definition("user")
    prefix = "CREATE TABLE"

    actual = StringHelper.is_start_with(definition, prefix)
    expected = True
    assert actual == expected


def test_duplicate_and_drop_table():
    table_name = "user"
    new_table_name = "user_aa__"
    ddl = DatabaseClient.get_ddl()

    ddl.duplicate_table(table_name, new_table_name, -1)
    actual = ddl.is_exist_table(new_table_name)
    expected = True
    assert actual == expected

    ddl.drop_table(new_table_name, False)
    actual = ddl.is_exist_table(new_table_name)
    expected = True
    assert actual == expected

    ddl.drop_table(new_table_name, True)
    actual = ddl.is_exist_table(new_table_name)
    expected = False
    assert actual == expected


def test_drop_table():
    ddl = DatabaseClient.get_ddl()
    ddl.drop_table("user__dupl", True)


def test_get_content_sql():
    ddl = DatabaseClient.get_ddl()
    result = ddl.get_content_sql("user")
    print()
    print(result)
