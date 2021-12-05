class ConsoleHelper:
    @staticmethod
    def echo(data):
        """
        本方法调用系统内部的print方法。本方法的目的是为了平滑PHP的使用体验。
        :param data:
        :return:
        """
        print(data)

# from builtins import *
#
# from hiland import ConfigHelper
#
#
# def __get_display_level_in_config():
#     display_level = ConfigHelper.get_config_item("project_data", "console_information_display_level", 10)
#     return display_level
#
#
# def __display(content, level):
#     display_level = __get_display_level_in_config()
#     if display_level <= level:
#         print(content)
#
#
# def information(content):
#     __display(content, 100)
#
#
# def debug(content):
#     __display(content, 10)
#
#
# def error(content):
#     __display(content, 0)
#
#
# def display(data):
#     _type = type(data)
#     _len = len(data)
#     print("目标数据类型为{}，长度为{}".format(_type, _len))
#
#     if _type is list or _type is dict or _type is set:
#         for item in data:
#             print(item)
#     else:
#         print(data)
