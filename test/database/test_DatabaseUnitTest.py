"""
 * @file   : test_DatabaseUnitTest.py
 * @time   : 21:34
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseClient import DatabaseClient
from hilandBasicLibrary.dataBase.databaseUnitTest import DatabaseUnitTest

"""
测试前，请确保数据库内有如下文件内的表和数据：
（具体查看本级目录下的README.md文件）
"""


def test_is_exist_table():
    table_name = "user"

    _user = DatabaseUnitTest(table_name=table_name, duplicate_row_count=2, auto_dispose=False)
    new_table_name = _user.new_table_name
    actual = _user.ddl.is_exist_table(new_table_name)
    expected = True
    assert actual == expected
    _user.dispose()
    actual = _user.ddl.is_exist_table(new_table_name)
    expected = False
    assert actual == expected


def test_insert():
    table_name = "user"

    _user = DatabaseUnitTest(table_name=table_name, duplicate_row_count=2, auto_dispose=False)
    new_table_name = _user.new_table_name

    entity = {'a': "www"}
    print(entity)

    # actual = _user.ddl.is_exist_table(new_table_name)
    # expected = True
    # assert actual == expected
    # _user.dispose()
    # actual = _user.ddl.is_exist_table(new_table_name)
    # expected = False
    # assert actual == expected
