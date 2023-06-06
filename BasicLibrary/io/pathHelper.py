"""
 * @file   : pathHelper.py
 * @time   : 8:37
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from BasicLibrary.environment.envHelper import EnvHelper
from BasicLibrary.projectHelper import ProjectHelper


class PathHelper:
    """

    """

    @staticmethod
    def combine(*args):
        """
        将给定的各个部分，组装成一个标准路径
        :param args:
        :return:
        """
        return os.path.join(*args)

    @classmethod
    def get_dir_name(cls, path, up_level=1):
        """
        获取给定路径的目录部分
        :param up_level: 求向上多少级的目录
        :param str path:
        :return:
        """
        for key in range(0, up_level):
            path = os.path.dirname(path)

        return path

    @staticmethod
    def get_root_path():
        """
        获取当前程序的运行路径
        :return:
        """
        return ProjectHelper.get_root_physical_path()

    @staticmethod
    def ensure_exist(path):
        """
        取保目录存在，如果不存在就创建
        :param path:
        :return:
        """
        if os.path.exists(path) is False:
            os.makedirs(path)

    @staticmethod
    def determine_is_exist(path):
        """
        判断给定的路径是否存在
        :param path:
        :return:
        """
        return os.path.exists(path)

    @staticmethod
    def get_formatted_path(path):
        """
        获取跟 os 相关的格式化的路径（Windows下用 “\\”;linux 下用 "/"）
        :param path:
        :return:
        """
        return os.path.realpath(path)

    @staticmethod
    def get_path_separator():
        """
        获取跟 os 相关的路径分隔符（Windows下用 “\\”;linux 下用 "/"）
        :return:
        """
        return EnvHelper.get_path_separator()


