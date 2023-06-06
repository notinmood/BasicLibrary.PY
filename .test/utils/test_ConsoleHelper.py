"""
 * @file   : test_ConsoleHelper.py
 * @time   : 8:34
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary import ConsoleHelper


def test_aa():
    ConsoleHelper.echo(1234)
    actual = 0
    expected = 0
    assert actual == expected


def test_get_console_args():
    print(__file__)

    # print(os.getcwd())
    # actual = ConsoleHelper.get_console_args()
    # expected = []
    # assert actual == expected
