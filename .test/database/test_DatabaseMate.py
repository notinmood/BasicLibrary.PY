"""
 * @file   : test_DatabaseMate.py
 * @time   : 15:03
 * @date   : 2021/12/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.configHelper import ConfigHelper
from BasicLibrary.dataBase.databaseClient import DatabaseClient as client


def test_get_real_table_name():
    table_name = "user"
    mate = client.get_mate(table_name)
    actual = mate.get_real_table_name()

    prefix = ConfigHelper.get_item("db_mysql", "table_prefix")
    expected = prefix + table_name

    assert actual == expected


