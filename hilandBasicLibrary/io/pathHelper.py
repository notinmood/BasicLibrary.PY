"""
 * @file   : pathHelper.py
 * @time   : 8:37
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from hilandBasicLibrary.projectHelper import ProjectHelper


class PathHelper:
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
    def ensure_path(path_name):
        """
        取保目录存在，如果不存在就创建
        :param path_name:
        :return:
        """
        if os.path.exists(path_name) is False:
            os.makedirs(path_name)
