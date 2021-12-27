"""
 * @file   : test_DatabaseMisc.py
 * @time   : 17:24
 * @date   : 2021/12/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseMisc import DatabaseMisc as misc


def test_create_table_duplicate():
    misc.duplicate_table("user", "", -1)


def test_drop_table():
    misc.drop_table("user__dupl", True)


def test_get_content_sql():
    result = misc.get_content_sql("user")
    print()
    print(result)
