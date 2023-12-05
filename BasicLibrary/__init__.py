"""
 * @file   : __init__.py
 * @time   : 15:15
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.data.objectHelper import ObjectHelper
from BasicLibrary.environment.consoleHelper import ConsoleHelper

"""
本部分有两个功能，分别如下：
1. 文件最上部的 from BasicLibrary.data.objectHelper import ObjectHelper，实际上为第三方使用 ObjectHelper 引入了简短的方式，
现在第三方代码中直接使用 from BasicLibrary import ObjectHelper 导入 ObjectHelper 就可以了。

2. 下部的代码为类库中常用的功能在文件内做别名处理。（本包内的功能，以(不包含在类内部的)函数的方式对外提供。）
"""


def echo(data):
    ConsoleHelper.echo(data)


def is_empty(data):
    return ObjectHelper.is_empty(data)
