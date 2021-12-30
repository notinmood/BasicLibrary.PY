"""
 * @file   : test_DataCompare.py
 * @time   : 18:29
 * @date   : 2021/12/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.utils.dataCompare import *


def test_data_summary():
    _dict = {"a": "AA", "b": "BB", "c": "CC"}
    summary1 = DataSummary(_dict)
    summary2 = DataSummary(target_length=3, target_type=dict)

    # assert summary1.compare(summary2)
    actual = summary1.compare(summary2)
    expected = True
    assert actual == expected


def test_compare_entity():
    entity1 = {"a": "AA", "b": "BB", "c": "CC"}
    entity2 = {"a": "AA", "b": "BB", "c": "CC", "d": "DD"}
    actual = DataCompare.compare_entity_single(entity1, entity2)
    expected = ""
    assert actual == expected

    entity1 = {"a": "AA", "b": "BB", "c": "CC"}
    entity2 = {"a": "AA", "b": "BB", "c": "CC", "d": "DD"}
    actual = DataCompare.compare_entity_single(entity2, entity1)
    expected = "d|DD|None||"
    assert actual == expected

    entity1 = {"a", "b", "c"}
    entity2 = {"a", "b", "c", "d"}
    actual = DataCompare.compare_entity_single(entity1, entity2)
    expected = ""
    assert actual == expected

    entity1 = {"a", "b", "c", "d"}
    entity2 = {"a", "b", "c"}
    actual = DataCompare.compare_entity_single(entity1, entity2)
    expected = "d||"
    assert actual == expected

    entity1 = ["a", "b", "c", "d"]
    entity2 = ["a", "b", "c"]
    actual = DataCompare.compare_entity_single(entity1, entity2)
    expected = "d||"
    assert actual == expected

    entity1 = ["a", "b", "c", "d"]
    entity2 = {"a", "b", "c"}
    actual = DataCompare.compare_entity_single(entity1, entity2)
    expected = "d||"
    assert actual == expected
