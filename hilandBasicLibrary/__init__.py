"""
 * @file   : __init__.py
 * @time   : 15:15
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.objectHelper import ObjectHelper
from hilandBasicLibrary.environment.consoleHelper import ConsoleHelper

"""
常用的功能在本子包内做别名处理。
本包内的功能，以函数的方式提供（不包含在类内部）。
"""


def echo(data):
    ConsoleHelper.echo(data)


def is_empty(data):
    return ObjectHelper.is_empty(data)
