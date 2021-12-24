"""
 * @file   : DatabaseClient_test.py
 * @time   : 10:03
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.dataBase.DatabaseClient import DatabaseClient
from HilandBasicLibrary.data.StringHelper import StringHelper
from HilandBasicLibrary.ConfigHelper import ConfigHelper


def test_static_construct():
    actual = DatabaseClient.get_mate("hello")
    print(actual)

    result = actual.get_name()
    print(result)

    actual = actual.table_name
    expected = "hello"
    prefix = ConfigHelper.get_item("db_mysql", "table_prefix")
    expected = prefix + expected
    assert actual == expected


def test_ddl_get_table_definition():
    mate = DatabaseClient.get_mate("my_user")
    definition = mate.ddl_get_table_definition()
    prefix = "CREATE TABLE"

    actual = StringHelper.is_start_with(definition, prefix)
    expected = True
    assert actual == expected
