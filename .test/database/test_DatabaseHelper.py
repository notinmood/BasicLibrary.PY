"""
 * @file   : test_DatabaseHelper.py
 * @time   : 9:04
 * @date   : 2021/12/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.dataBase.databaseHelper import DatabaseHelper


def test_build_insert_clause():
    _entity_dict = {"a": "A", "b": "B", "c": 1}
    actual = DatabaseHelper.build_insert_clause("my_table", _entity_dict)
    expected = 'INSERT INTO `my_table` (`a`,`b`,`c`) VALUES ("A","B",1);'
    assert actual == expected

    _entity_dict = {"a": "A", "b": "B", "c": 1}
    _entity_list = [_entity_dict]
    actual = DatabaseHelper.build_insert_clause("my_table", _entity_list)
    expected = 'INSERT INTO `my_table` (`a`,`b`,`c`) VALUES ("A","B",1);'
    assert actual == expected

    _entity_dict1 = {"a": "A", "b": "B", "c": 1}
    _entity_dict2 = {"a": "X", "b": "Y", "c": 1}
    _entity_list = [_entity_dict1, _entity_dict2]
    actual = DatabaseHelper.build_insert_clause("my_table", _entity_list)
    expected = 'INSERT INTO `my_table` (`a`,`b`,`c`) VALUES ("A","B",1), ("X","Y",1);'
    assert actual == expected


def test_build_where_clause():
    _entity_dict = {"a": "A", "b": "B", "c": 1}
    actual = DatabaseHelper.build_where_clause(_entity_dict)
    expected = ' `a` = "A"  AND `b` = "B"  AND `c` = 1 '
    assert actual == expected


def test_build_delete_clause():
    condition = {"a": "A", "b": "B", "c": 1}
    actual = DatabaseHelper.build_delete_clause("my_table", condition)
    expected = 'DELETE FROM `my_table`  WHERE  `a` = "A"  AND `b` = "B"  AND `c` = 1 ;'
    assert actual == expected


def test_build_update_clause():
    fixing_data = {"x": "XX", "y": "YY"}
    condition_data = {"a": "A", "b": 1}
    actual = DatabaseHelper.build_update_clause("my_table", fixing_data, condition_data)
    expected = 'UPDATE `my_table` SET `x`="XX",`y`="YY" WHERE  `a` = "A"  AND `b` = 1 ;'
    assert actual == expected


def test_build_select_clause():
    condition_data = {"a": "A", "b": 1}
    actual = DatabaseHelper.build_select_clause("my_table", condition_data)
    expected = 'SELECT * FROM `my_table`  WHERE  `a` = "A"  AND `b` = 1 '
    assert actual == expected
