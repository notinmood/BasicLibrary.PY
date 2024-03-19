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
from typing import Callable

from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.enums import RandomEnum
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.pathHelper import PathHelper


class DirHelper:
    """
    目录操作助手
    """

    @classmethod
    def get_files(cls, dir_full_path: PathLike | str, include_sub_dir=True, extension_names=".*") -> list[str]:
        """
        获取某目录下的带完整路径的文件全名称
        :param extension_names: 文件扩展名，多个扩展名之间用逗号（或者分号）分隔。默认为".*"（所有文件）
        :param dir_full_path:
        :param include_sub_dir: 是否包含子目录（缺省是True，包含）
        :return:
        """
        result = []
        cls.__list_dir(dir_full_path, result, include_sub_dir, extension_names)
        return result

    pass

    @classmethod
    def __list_dir(cls, dir_full_path: PathLike | str, list_name, include_sub_dir=True, extension_names=".*"):
        for item in os.listdir(dir_full_path):
            item_full_path = os.path.join(dir_full_path, item)
            if os.path.isdir(item_full_path):
                if include_sub_dir is True:
                    cls.__list_dir(item_full_path, list_name, include_sub_dir, extension_names)
                pass
            else:
                if FileHelper.is_match_extension_name(item_full_path, extension_names):
                    list_name.append(item_full_path)
                pass
            pass
        pass

    pass

    @classmethod
    def get_sub_dirs(cls, dir_full_path: PathLike | str) -> list[str]:
        dirs: list = []
        for item in os.listdir(dir_full_path):
            item_full_path = os.path.join(dir_full_path, item)
            if os.path.isdir(item_full_path):
                dirs.append(item_full_path)
            pass
        pass

        return dirs

    @staticmethod
    def ensure_exist(dir_full_path: PathLike | str):
        """
        确保目录存在，如果不存在就创建
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    pass

    @classmethod
    def is_exist(cls, dir_full_path: PathLike | str) -> bool:
        """
        判断为文件夹是否存在
        :param dir_full_path: 带全路径的文件夹名称
        :return:
        """
        return os.path.isdir(dir_full_path)

    pass

    @classmethod
    def is_dir(cls, dir_full_path: PathLike | str) -> bool:
        """
        判断为文件夹是否存在(is_exist的别名)
        :param dir_full_path: 带全路径的文件夹名称
        :return:
        """
        return cls.is_exist(dir_full_path)

    pass

    @classmethod
    def make(cls, dir_full_path: PathLike | str):
        """
        创建目录
        :param dir_full_path:
        :return:
        """
        PathHelper.ensure_exist(dir_full_path)

    pass

    @classmethod
    def rename(cls, parent_dir_full_name: PathLike | str, old_dir_base_name: PathLike | str,
               new_dir_base_name: PathLike | str, **kwargs):
        """
        给指定文件夹下的某个子文件夹重新命名（即将 parent-path-full-name/subA改名为parent-path-full-name/subB）
        :param parent_dir_full_name: 父文件夹的完整路径
        :param old_dir_base_name: 旧有的文件夹基本名称
        :param new_dir_base_name: 要改名的新文件夹基本名称
        :return:
        """
        old_dir_full_name = os.path.join(parent_dir_full_name, old_dir_base_name)
        new_dir_full_name = os.path.join(parent_dir_full_name, new_dir_base_name)
        cls.move(old_dir_full_name, new_dir_full_name, **kwargs)

    pass

    @classmethod
    def move(cls, source_dir_full_name: PathLike | str, dest_dir_full_name: PathLike | str, **kwargs) -> None:
        """
        移动目录(如果原目录不存在，本方法不会执行任何动作)
        :param source_dir_full_name: 原目录的全名称
        :param dest_dir_full_name: 新目录的全名称
        :return:
        """
        # 以下是为了消除ide参数未使用的警告而做的PolyFill
        # noinspection all
        kwargs = kwargs

        if not cls.is_exist(source_dir_full_name):
            return
        pass

        # TODO:xiedali@20230608 需要加入一个目标文件夹已经存在时的处理策略的功能
        if cls.is_exist(dest_dir_full_name):
            # object_has_existed_deal_strategy = kwargs.get('ObjectHasExistedDealStrategy',
            #                                               ObjectHasExistedDealStrategyEnum.RenameNew)

            # if object_has_existed_deal_strategy == ObjectHasExistedDealStrategyEnum.RenameNew:
            #     new_dir_full_name += f'({RandomHelper.create(8, RandomEnum.UpperLetters)})'
            # pass

            dest_dir_full_name += f'({RandomHelper.create(8, RandomEnum.UpperLetters)})'
        pass

        os.rename(source_dir_full_name, dest_dir_full_name)

    pass

    @staticmethod
    def remove(dir_full_name: PathLike | str):
        """
        删除目录(如果目录不存在，本方法不会执行任何动作)
        :param dir_full_name:
        :return:
        """
        if os.path.isdir(dir_full_name):
            shutil.rmtree(dir_full_name)
        pass

    pass

    @staticmethod
    def walk_files[** P](dir_full_name: PathLike | str, deal_file_func: Callable[[str, str, P], None], *args, **kwargs):
        """
        遍历目录下的文件
        :param dir_full_name:
        :param deal_file_func:处理每一个文件使用的函数。（参数分别为文件的基本名称和文件所在的全路径,以及*args和**kwargs）
        :return:
        """
        for dir_full_path, dir_names, file_names in os.walk(dir_full_name):
            for file_base_name in file_names:
                deal_file_func(file_base_name, dir_full_path, *args, **kwargs)
            pass
        pass

    pass

    @staticmethod
    def change_working_dir(target_dir: str | PathLike) -> str:
        """
        改变当前工作目录
        :param target_dir:
        :return:
        """
        os.chdir(target_dir)
        return os.getcwd()

    pass

    @staticmethod
    def get_working_dir() -> str:
        """
        获取当前工作目录
        :return:
        """
        return os.getcwd()

    pass


pass
