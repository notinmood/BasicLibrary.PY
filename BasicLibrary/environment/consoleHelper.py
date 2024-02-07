"""
 * @file   : **.py
 * @time   : 16:26
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import sys

from BasicLibrary.environment.envHelper import EnvHelper


class ConsoleHelper:
    """
    本类提供一些与系统交互的函数。
    """

    @staticmethod
    def echo(data):
        """
        本方法调用系统内部的 print 方法。
        本方法的目的是为了平滑 PHP 的使用体验。
        :param data:
        :return:
        """
        print(data)

    @classmethod
    def echo_line(cls, data):
        """
        本方法是换行后，调用系统内部的 print 方法。
        本方法的目的是为了平滑 PHP 的使用体验。
        :param data:
        :return:
        """
        print(cls.get_new_line_symbol())
        print(data)
        pass

    @staticmethod
    def get_new_line_symbol():
        """
        获取换行标志
        TODO:需要判断是 cli 还是 web
        :return:
        """
        if EnvHelper.determine_is_windows():
            return "\r\n"
        pass

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
        pass

        return None
