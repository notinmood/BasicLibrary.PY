import inspect
import sys


class ConsoleHelper:
    @staticmethod
    def echo(data):
        """
        本方法调用系统内部的print方法。本方法的目的是为了平滑PHP的使用体验。
        :param data:
        :return:
        """
        print(data)

    @staticmethod
    def get_new_line_symbol():
        """
        获取换行标志
        TODO:需要判断不同OS
        TODO:需要判断是cli还是web
        :return:
        """
        return "\n"

    @staticmethod
    def get_console_args():
        """
        获取控制台上输入的所有参数(包括命令本身和传递给命令的参数)
        :return:
        """
        return sys.argv

    @staticmethod
    def get_console_arg(index=1):
        """
        获取控制台上输入的某个参数(默认取第一个参数(因为第0个是命令本身)，也就是除命令名称外的第一个真实的参数)
        :param index:
        :return:
        """
        args_len = len(sys.argv)
        if args_len > index:
            arg_value = sys.argv[index]
            return arg_value
        else:
            return None

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
