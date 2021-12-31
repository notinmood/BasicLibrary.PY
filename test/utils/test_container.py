"""
 * @file   : test_container.py
 * @time   : 14:31
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from hilandBasicLibrary.model.container import Container


def test_get_dict():
    my_dict_a = Container.get_dict("a")
    my_dict_b = Container.get_dict("b")
    assert my_dict_a == my_dict_b

    my_dict_a['k-a'] = "v-a"
    assert my_dict_a != my_dict_b


def tests_get_item():
    key = "__wps__"
    item = Container.get_item(key)
    assert item is None

    value = "qingdao"
    Container.set_item(key, value)
    item2 = Container.get_item(key)
    assert item2 == value
