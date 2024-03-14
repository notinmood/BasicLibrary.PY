"""
 * @file   : pathHelper.py
 * @time   : 8:37
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import inspect
import os.path
from os import PathLike

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

    pass

    @classmethod
    def get_dir_name(cls, path: PathLike | str = None, up_level=1):
        """
        获取给定路径的目录部分
        :param int up_level: 求向上多少级的目录。如果不指定本参数，那么
            将获取当前主动调用方文件所在的目录。
        :param str|PathLike path: 给定的目录结构。如果不指定本参数，那么
            将从当前主动调用方文件所在的目录开始向上查找。
        :return:
        """
        if path is None:
            path = inspect.stack()[1].filename
        pass

        for _ in range(0, up_level):
            path = os.path.dirname(path)
        pass

        return path

    pass

    @staticmethod
    def get_root_path():
        """
        获取当前程序的运行路径
        :return:
        """
        return ProjectHelper.get_root_physical_path()

    pass

    @staticmethod
    def get_current_physical_path():
        """
        获取主动调用本方法的模块的物理路径
        :return:
        """
        return os.path.abspath(os.path.dirname(inspect.stack()[1].filename))

    pass

    @staticmethod
    def ensure_exist(path: PathLike | str):
        """
        取保目录存在，如果不存在就创建
        :param path:
        :return:
        """
        if os.path.exists(path) is False:
            os.makedirs(path)
        pass

    pass

    @staticmethod
    def determine_is_exist(path: PathLike | str):
        """
        判断给定的路径是否存在
        :param path:
        :return:
        """
        return os.path.exists(path)

    pass

    @staticmethod
    def get_formatted_path(path: PathLike | str):
        """
        获取跟 os 相关的格式化的路径（Windows下用 “\\”;linux 下用 "/"）
        :param path:
        :return:
        """
        return os.path.realpath(path)

    pass

    @staticmethod
    def get_path_separator():
        """
        获取跟 os 相关的路径分隔符（Windows下用 “\\”;linux 下用 "/"）
        :return:
        """
        return EnvHelper.get_path_separator()

    pass

    @staticmethod
    def get_disk_name(path: str | PathLike):
        """
        获取给定路径的磁盘名称（在没有驱动器概念的系统上，本函数将返回空字符串。）
        :param path:
        :return:
        """
        return os.path.splitdrive(path)[0]

    pass


pass
