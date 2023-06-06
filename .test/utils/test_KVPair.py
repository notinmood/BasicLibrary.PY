"""
 * @file   : test_KVPair.py
 * @time   : 11:04
 * @date   : 2021/12/30
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.model.kvPair import KVPair


def test_convert_to_dict_item():
    kvp = KVPair("name", "zhangsan")
    actual = kvp.convert_to_dict_item()
    expected = '"name":"zhangsan"'
    assert actual == expected

    kvp = KVPair("age", 19)
    actual = kvp.convert_to_dict_item()
    expected = '"age":19'
    assert actual == expected

    kvp = KVPair("passed", True)
    actual = kvp.convert_to_dict_item()
    expected = '"passed":True'
    assert actual == expected

    kvp = KVPair("name", "zhangsan")
    actual = kvp.convert_to_dict_item(False)
    expected = "'name':'zhangsan'"
    assert actual == expected

    kvp = KVPair("age", 19)
    actual = kvp.convert_to_dict_item(False)
    expected = "'age':19"
    assert actual == expected

    kvp = KVPair("passed", True)
    actual = kvp.convert_to_dict_item(False)
    expected = "'passed':True"
    assert actual == expected
