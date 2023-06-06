"""
 * @file   : test_DatabaseUnitTest.py
 * @time   : 21:34
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.dataBase.databaseUnitTest import DatabaseUnitTest
from BasicLibrary.model.dataCompare import DataSummary, DataCompare

"""
测试前，请确保数据库内有如下文件内的表和数据：
（具体查看本级目录下的README.md文件）
"""


def test_is_exist_table():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name, duplicate_row_count=2, auto_dispose=False)

    new_table_name = biz.new_table_name
    actual = biz.ddl.is_exist_table(new_table_name)
    expected = True
    assert actual == expected

    biz.dispose()
    actual = biz.ddl.is_exist_table(new_table_name)
    expected = False
    assert actual == expected


def test_find_one():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    condition = {"class": "一"}
    result = biz.mate.find_one(condition)

    actual = DataSummary(result)
    expected = DataSummary(target_length=6, target_type=dict)
    assert actual.compare(expected)


def test_find_many():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    condition = {"class": "一"}
    result = biz.mate.find_many(condition)

    actual = DataSummary(result)
    expected = DataSummary(target_length=2, target_type=list)
    # print(result)
    assert actual.compare(expected)


def test_find_more():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    result = biz.mate.find_more("id", 2)
    actual = DataSummary(result)
    expected = DataSummary(target_length=3, target_type=list)
    assert actual.compare(expected)


def test_insert_one():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    entity = {"id": 20, 'name': "赵六", "birthday": "2010-12-12", "class": "二", "score": 92, "email": "rr@ss.com"}

    biz.mate.insert_one(entity)
    selected = biz.mate.find_one({"id": 20})

    actual = selected["name"]
    expected = "赵六"
    assert actual == expected

    actual = DataCompare.compare_entity_single(entity, selected)
    expected = "birthday|2010-12-12|2010-12-12 00:00:00||"
    assert actual == expected


# TODO:
def test_insert_many():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    entity1 = {"id": 20, 'name': "赵六", "birthday": "2010-12-12", "class": "二", "score": 92, "email": "rr@ss.com"}
    entity2 = {"id": 21, 'name': "赵7", "birthday": "2011-12-12", "class": "三", "score": 91, "email": "ddd@ss.com"}
    entities = [entity1, entity2]

    biz.mate.insert_many(entities)
    # selected = biz.mate.find_many({"id": 20})
    #
    # actual = selected["name"]
    # expected = "赵六"
    # assert actual == expected
    #
    # actual = DataCompare.compare_entity_single(model, selected)
    # expected = "birthday|2010-12-12|2010-12-12 00:00:00||"
    # assert actual == expected


def test_update_one():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    fixing_data = {"name": "张三"}
    condition_data = {"name": "zhangsan"}
    biz.mate.update_one(fixing_data, condition_data)
    condition1 = {"id": 1}
    item1 = biz.mate.find_one(condition1)
    assert item1["name"] == "张三"

    condition1 = {"id": 3}
    item1 = biz.mate.find_one(condition1)
    assert item1["name"] == "zhangsan"


def test_update_many():
    table_name = "user"
    biz = DatabaseUnitTest(table_name=table_name)

    fixing_data = {"name": "张三"}
    condition_data = {"name": "zhangsan"}
    biz.mate.update_many(fixing_data, condition_data)
    condition1 = {"id": 1}
    item1 = biz.mate.find_one(condition1)
    assert item1["name"] == "张三"

    condition1 = {"id": 3}
    item1 = biz.mate.find_one(condition1)
    assert item1["name"] == "张三"
