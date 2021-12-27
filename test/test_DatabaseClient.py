"""
 * @file   : test_DatabaseClient.py
 * @time   : 10:03
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseClient import DatabaseClient
from hilandBasicLibrary.data.stringHelper import StringHelper
from hilandBasicLibrary.configHelper import ConfigHelper


def test_get_mate():
    mate = DatabaseClient.get_mate("hello")
    actual = mate.__str__()
    expected = "mate in  DatabaseMate: hilandBasicLibrary.dataBase.MySql.mate"
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


# def test_ddl_create_table():
#     mate = DatabaseClient.get_mate("my_user")
#     sql = """CREATE TABLE `dp_ss_my_user__test` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(255) CHARACTER SET utf8 DEFAULT '',
#   `email` varchar(255) CHARACTER SET utf8 DEFAULT '',
#   `birthday` datetime DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1"""
#     mate.directly_exec(sql)





def test_s():
    sql = 'INSERT INTO `tmp_user__dupl` (`id`,`name`,`birthday`,`postcode`) VALUES (1,"zhangsan","2021-12-24 09:07:05",266000),(4,"lisi","2021-12-15 09:07:26",277521);'
    mate = DatabaseClient.get_mate("user")
    mate.directly_exec(sql)
