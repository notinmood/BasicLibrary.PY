"""
 * @file   : dirHelper.py
 * @time   : 12:28
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os


class DirHelper:
    @classmethod
    def get_files(cls, dir_path, include_sub_dir=True):
        """
        获取某目录下的文件名称
        :param dir_path:
        :param include_sub_dir: 是否包含子目录（缺省是True，包含）
        :return:
        """
        result = []
        cls.__list_dir(dir_path, result, include_sub_dir)
        return result

    @classmethod
    def __list_dir(cls, path, list_name, include_sub_dir=True):  # 传入存储的list
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                if include_sub_dir is True:
                    cls.__list_dir(file_path, list_name)
            else:
                list_name.append(file_path)