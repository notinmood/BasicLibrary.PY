"""
 * @file   : dirHelper.py
 * @time   : 12:28
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os
import shutil

from os import PathLike
from BasicLibrary.io.pathHelper import PathHelper


class DirHelper:
    """

    """

    @classmethod
    def get_files(cls, dir_full_path: PathLike, include_sub_dir=True):
        """
        获取某目录下的带完整路径的文件全名称
        :param dir_full_path:
        :param include_sub_dir: 是否包含子目录（缺省是True，包含）
        :return:
        """
        result = []
        cls.__list_dir(dir_full_path, result, include_sub_dir)
        return result

    pass

    @classmethod
    def __list_dir(cls, dir_full_path: PathLike, list_name, include_sub_dir=True):  # 传入存储的list
        for item in os.listdir(dir_full_path):
            item_full_path = os.path.join(dir_full_path, item)
            if os.path.isdir(item_full_path):
                if include_sub_dir is True:
                    cls.__list_dir(item_full_path, list_name)
                pass
            else:
                list_name.append(item_full_path)
            pass
        pass

    pass

    @classmethod
    def get_sub_dirs(cls, dir_full_path: PathLike) -> list:
        dirs: list = []
        for item in os.listdir(dir_full_path):
            item_full_path = os.path.join(dir_full_path, item)
            if os.path.isdir(item_full_path):
                dirs.append(item_full_path)
            pass
        pass

        return dirs

    @staticmethod
    def ensure_exist(dir_full_path: PathLike):
        """
        确保目录存在，如果不存在就创建
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    pass

    @classmethod
    def make(cls, dir_full_path: PathLike):
        """
        创建目录
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    pass

    @staticmethod
    def remove(dir_full_name: PathLike):
        if os.path.isdir(dir_full_name):
            shutil.rmtree(dir_full_name)
        pass

    pass

    @staticmethod
    def walk_files(dir_full_name: PathLike, deal_file_func: callable, *args, **kwargs):
        """
        遍历目录下的文件
        :param dir_full_name:
        :param deal_file_func:处理每一个文件使用的函数。（两个参数分别为文件的基本名称和文件所在的全路径）
        :return:
        """
        for dir_full_path, dir_names, file_names in os.walk(dir_full_name):
            for file_base_name in file_names:
                deal_file_func(file_base_name, dir_full_path, *args, **kwargs)
            pass
        pass

    pass


pass
