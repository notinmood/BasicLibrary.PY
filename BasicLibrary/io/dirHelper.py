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

from BasicLibrary.io.pathHelper import PathHelper


class DirHelper:
    """

    """

    @classmethod
    def get_files(cls, dir_full_path, include_sub_dir=True):
        """
        获取某目录下的带完整路径的文件全名称
        :param dir_full_path:
        :param include_sub_dir: 是否包含子目录（缺省是True，包含）
        :return:
        """
        result = []
        cls.__list_dir(dir_full_path, result, include_sub_dir)
        return result

    @classmethod
    def __list_dir(cls, dir_full_path, list_name, include_sub_dir=True):  # 传入存储的list
        for item in os.listdir(dir_full_path):
            item_full_path = os.path.join(dir_full_path, item)
            if os.path.isdir(item_full_path):
                if include_sub_dir is True:
                    cls.__list_dir(item_full_path, list_name)
            else:
                list_name.append(item_full_path)

    @staticmethod
    def ensure_exist(dir_full_path):
        """
        确保目录存在，如果不存在就创建
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    @classmethod
    def make(cls, dir_full_path):
        """
        创建目录
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    @staticmethod
    def remove(dir_full_name):
        if os.path.isdir(dir_full_name):
            shutil.rmtree(dir_full_name)
