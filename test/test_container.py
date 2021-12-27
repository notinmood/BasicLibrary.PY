"""
 * @file   : test_container.py
 * @time   : 14:31
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from pprint import pprint

from hilandBasicLibrary.data.container import Container


def test_get_dict():
    my_dict_a = Container.get_dict("a")
    my_dict_b = Container.get_dict("b")
    assert my_dict_a == my_dict_b

    my_dict_a['k-a'] = "v-a"

    print("")
    pprint("显示数据：")
    print(Container.get_dict("a"))
    assert my_dict_a != my_dict_b
