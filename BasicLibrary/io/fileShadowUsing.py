"""
 * @file   : fileShadowUsing.py
 * @time   : 9:56
 * @date   : 2023/6/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from os import PathLike

from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.pathHelper import PathHelper


class FileShadowUsing:
    """
    在不影响原始文件的情形下，对文件的影子进行操作，操作完成后默认销毁影子文件（可以在初始化的时候，设置保留影子文件）。
    在 with *** as ***： 语句内使用，as 后返回的是影子文件的文件全名称。
    """

    @property
    def file_shadow_full_name(self):
        return self._file_shadow_full_name

    pass

    def __init__(self, file_full_name:PathLike | str, is_auto_destroy=True):
        """
        通过给定的原始文件，生成一个影子文件。
        :param file_full_name: 原始文件的文件全名称。
        :param is_auto_destroy: 是否自动销毁影子文件。
        """
        self._file_shadow_full_name = self.__generate_file_shadow(file_full_name)
        self._is_auto_destroy = is_auto_destroy
    pass

    def __enter__(self):
        return self._file_shadow_full_name

    pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._is_auto_destroy:
            FileHelper.remove(self._file_shadow_full_name)
        pass
    pass

    @staticmethod
    def __generate_file_shadow(source_file_full_name:PathLike | str):
        target_dir_full_name = PathHelper.get_dir_name(source_file_full_name)
        target_file_ext_name = FileHelper.get_extension_name(source_file_full_name)
        target_file_base_name = RandomHelper.create() + target_file_ext_name
        FileHelper.copy(source_file_full_name, target_dir_full_name, target_file_base_name)

        target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)
        return target_file_full_name

    pass


pass
