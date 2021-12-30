"""
 * @file   : test_DatabaseClient.py
 * @time   : 10:03
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import hilandBasicLibrary
from hilandBasicLibrary.configHelper import ConfigHelper
from hilandBasicLibrary.dataBase.databaseClient import DatabaseClient


def test_get_mate():
    mate = DatabaseClient.get_mate("hello")
    actual = type(mate)
    expected = hilandBasicLibrary.dataBase.MySql.mate.Mate
    assert actual == expected

    actual = mate.get_real_table_name()
    expected = "hello"
    prefix = ConfigHelper.get_item("db_mysql", "table_prefix")
    expected = prefix + expected
    assert actual == expected


def test_get_ddl():
    ddl = DatabaseClient.get_ddl()
    print(ddl)
    content = ddl.get_content_sql("user")
    print(content)

    ddl = DatabaseClient.get_ddl()
    print(ddl)
