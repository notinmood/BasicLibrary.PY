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

from BasicLibrary.io.pathHelper import PathHelper


class FileHelper:
    """

    """

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
    def load(file_full_name: str) -> object:
        """

        :param file_full_name:
        :return:
        """
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
        :param function line_callback: 在每行上进行回调的函数，类似：line_callback(line),其中参数 line 为读出的每行的内容
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
    def create(cls, file_full_name, content=""):
        """
        在目标位置创建文件
        :param str content: 待保存内容
        :param str file_full_name:待创建文件的全路径名称
        :return:
        """
        cls.store(file_full_name, content)

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
    def remove(file_full_name):
        """
        删除文件
        :param file_full_name:
        :return:
        """
        if os.path.exists(file_full_name):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(file_full_name)
            # os.unlink(path)

    @classmethod
    def delete(cls, file_full_name):
        """
        删除文件（remove方法的别名）
        :param file_full_name:
        :return:
        """
        cls.remove(file_full_name)

    @staticmethod
    def copy(source_file_full_name, target_dir_full_name, target_file_base_name=""):
        """
        复制文件
        :param source_file_full_name:带全路径的源文件
        :param target_dir_full_name:目标文件夹
        :param target_file_base_name:复制后的文件名称（默认空，表示使用源文件的名称）
        :return:
        """
        if os.path.isfile(source_file_full_name):
            file_path_name, file_base_name = os.path.split(source_file_full_name)  # 分离文件名和路径
            if not os.path.exists(target_dir_full_name):
                os.makedirs(target_dir_full_name)  # 创建路径

            if target_file_base_name == "":
                target_file_base_name = file_base_name

            target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

            shutil.copy(source_file_full_name, target_file_full_name)  # 复制文件

    @classmethod
    def move(cls, source_file_full_name, target_dir_full_name, target_file_base_name=""):
        """
        移动文件
        :param source_file_full_name:
        :param target_dir_full_name:
        :param target_file_base_name:
        :return:
        """
        cls.copy(source_file_full_name, target_dir_full_name, target_file_base_name)
        cls.remove(source_file_full_name)

    @classmethod
    def is_exist(cls, file_full_name):
        """
        判断为文件是否存在
        :param file_full_name: 带全路径的文件名称
        :return:
        """
        return os.path.isfile(file_full_name)

    @classmethod
    def rename(cls, old_file_full_name, new_file_name):
        """

        :param old_file_full_name: 旧有的带路径的文件全名称
        :param new_file_name: 要改名的新的名称（不带文件路径）
        :return:
        """
        file_path = cls.get_path_name(old_file_full_name)
        new_file_full_name = PathHelper.combine(file_path, new_file_name)
        os.rename(old_file_full_name, new_file_full_name)

