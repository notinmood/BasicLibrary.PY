"""
 * @file   : test_DatabaseHelper.py
 * @time   : 9:04
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseHelper import DatabaseHelper


def test_build_insert_clause():
    _entity_dict = {"a": "A", "b": "B", "c": 1}
    actual = DatabaseHelper.build_insert_clause(_entity_dict, "my_table")
    expected = 'INSERT INTO `my_table` (`a`,`b`,`c`) VALUES ("A","B",1);'
    assert actual == expected


def test_build_where_clause():
    _entity_dict = {"a": "A", "b": "B", "c": 1}
    actual = DatabaseHelper.build_where_clause(_entity_dict)
    expected = ' `a` = "A"  AND `b` = "B"  AND `c` = 1 '
    assert actual == expected
