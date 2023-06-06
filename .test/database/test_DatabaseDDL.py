"""
 * @file   : test_DatabaseMisc.py
 * @time   : 17:24
 * @date   : 2021/12/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.dataBase.databaseClient import DatabaseClient

"""
测试前，请确保数据库内有如下文件内的表和数据：
（具体查看本级目录下的README.md文件）
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
    definition = ddl.get_table_definition("user")
    prefix = "CREATE TABLE"

    actual = StringHelper.is_start_with(definition, prefix)
    expected = True
    assert actual == expected


def test_duplicate_and_drop_table():
    table_name = "user"
    new_table_name = "user__dupl__"
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
    ddl.drop_table("user__dupl__", True)


def test_get_content_sql():
    ddl = DatabaseClient.get_ddl()
    actual = ddl.get_content_sql("user")
    expected = 'INSERT INTO `tmp_user` (`id`,`name`,`birthday`,`email`,`class`,`score`) VALUES (1,"zhangsan","2021-12-24 09:07:05","266000@sina.com","一",66), (2,"lisi","2021-12-15 09:07:26","277521@qq.com","三",93), (3,"zhangsan","2021-12-24 09:07:05","aa@qq.com","二",88), (4,"hah","2021-12-22 10:07:47","wps@foxmail.com","一",97);'
    assert actual == expected

    ddl = DatabaseClient.get_ddl()
    actual = ddl.get_content_sql("user", 0)
    expected = ''
    assert actual == expected

    ddl = DatabaseClient.get_ddl()
    actual = ddl.get_content_sql("user", 1)
    expected = 'INSERT INTO `tmp_user` (`id`,`name`,`birthday`,`email`,`class`,`score`) VALUES (1,"zhangsan","2021-12-24 09:07:05","266000@sina.com","一",66);'
    assert actual == expected
