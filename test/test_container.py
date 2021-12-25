"""
 * @file   : test_container.py
 * @time   : 14:31
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.container import Container
from hilandBasicLibrary.environment.consoleHelper import ConsoleHelper


def test_get_dict():
    my_dict_a = Container.get_dict("a")
    my_dict_b = Container.get_dict("b")
    assert my_dict_a == my_dict_b

    my_dict_a['k-a'] = "v-a"
    # assert my_dict_a == my_dict_b
    print(ConsoleHelper.get_new_line_symbol())
    print(Container.get_dict("a"))

