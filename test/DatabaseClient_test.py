"""
 * @file   : DatabaseClient_test.py
 * @time   : 10:03
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.dataBase.DatabaseClient import DatabaseClient


def test_static_construct():
    actual = DatabaseClient.get_mate("hello")
    print(actual)

    result = actual.get_name()
    print(result)

    result = actual.table_name
    print(result)
    # HilandBasicLibrary.dataBase.MySql.Mate.Mate
