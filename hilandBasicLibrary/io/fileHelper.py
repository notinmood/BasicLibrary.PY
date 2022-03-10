"""
 * @file   : fileHelper.py
 * @time   : 12:27
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os
import pathlib
import shutil
import sys

from hilandBasicLibrary.io.pathHelper import PathHelper


class FileHelper:

    @staticmethod
    def get_base_name(file_name):
        """
        获取给定路径的文件名称部分(带扩展名)
        :param file_name:可用是文件的全名称也可以是部分名称
        :return:
        """
        return os.path.basename(file_name)

    @staticmethod
    def get_extension_name(file_name):
        """
        获取文件的扩展名(带符号“.”)
        :param file_name:可用是文件的全名称也可以是部分名称
        :return:
        """
        return pathlib.Path(file_name).suffix

    @staticmethod
    def get_path_name(file_name):
        """
        获取文件的路径部分
        :param file_name:
        :return:
        """
        filepath, filename = os.path.split(file_name)
        return filepath

    @staticmethod
    def load(file_full_name):
        with open(file_full_name, "r", encoding='utf-8') as file_pointer:
            data = file_pointer.read()
        return data

    @staticmethod
    def load_with_lines(file_full_name):
        """
        按照行的方式读取文件，返回行信息的list
        :param file_full_name:
        :return: 行信息的list
        """
        with open(file_full_name, "r", encoding='utf-8') as file_pointer:
            data = file_pointer.readlines()
        return data

    @staticmethod
    def load_with_line(file_full_name, line_callback):
        """
        按行读取文件，每读取一行进行一次处理（调用line_callback）,对大文件尤其有效
        :param str file_full_name:
        :param function line_callback: 在每行上进行回调的函数
        :return:
        """
        with open(file_full_name, "r", encoding='utf-8') as file_pointer:
            while True:
                line = file_pointer.readline()
                if line:
                    line_callback(line)
                else:
                    break

    @classmethod
    def store(cls, file_full_name, content, is_append=True):
        """
        保存文件在磁盘中
        :param str file_full_name:待保存文件的全路径名称
        :param content:待保存内容
        :param bool is_append: 新内容如是附加在原内容的后面，还是替代掉原内容（默认是附加在原内容后面）
        :return:
        """
        path_name = cls.get_path_name(file_full_name)
        PathHelper.ensure_exist(path_name)
        if is_append:
            mode = 'a+'
        else:
            mode = 'w+'

        with open(file_full_name, mode, encoding='utf-8') as file_pointer:
            file_pointer.write(content)

    @staticmethod
    def copy(source_file_full_name, target_dir_name, target_file_base_name=""):
        """
        复制文件
        :param source_file_full_name:带全路径的源文件
        :param target_dir_name:目标文件夹
        :param target_file_base_name:复制后的文件名称（默认空，表示使用源文件的名称）
        :return:
        """
        if os.path.isfile(source_file_full_name):
            file_path_name, file_base_name = os.path.split(source_file_full_name)  # 分离文件名和路径
            if not os.path.exists(target_dir_name):
                os.makedirs(target_dir_name)  # 创建路径

            if target_file_base_name == "":
                target_file_base_name = file_base_name

            target_file_full_name = PathHelper.combine(target_dir_name, target_file_base_name)

            shutil.copy(source_file_full_name, target_file_full_name)  # 复制文件
