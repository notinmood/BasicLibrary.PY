"""
 * @file   : DatabaseClient_test.py
 * @time   : 10:03
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.DatabaseClient import DatabaseClient
from hilandBasicLibrary.data.StringHelper import StringHelper
from hilandBasicLibrary.ConfigHelper import ConfigHelper


def test_static_construct():
    mate = DatabaseClient.get_mate("hello")
    actual = mate.__str__()
    expected = "mate in  DatabaseMate: hilandBasicLibrary.dataBase.MySql.Mate"
    assert actual == expected

    actual = mate.get_real_table_name()
    expected = "hello"
    prefix = ConfigHelper.get_item("db_mysql", "table_prefix")
    expected = prefix + expected
    assert actual == expected


def test_ddl_create_table():
    mate = DatabaseClient.get_mate("my_user")
    sql = """CREATE TABLE `dp_ss_my_user__test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 DEFAULT '',
  `email` varchar(255) CHARACTER SET utf8 DEFAULT '',
  `birthday` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1"""
    mate.directly_exec(sql)


def test_ddl_get_table_definition():
    mate = DatabaseClient.get_mate("user")
    definition = mate.ddl_get_table_definition()
    prefix = "CREATE TABLE"

    actual = StringHelper.is_start_with(definition, prefix)
    expected = True
    assert actual == expected
