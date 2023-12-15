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

import chardet

from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.enums import RandomEnum
from BasicLibrary.io.imageHelper import ImageHelper

from BasicLibrary.io.pathHelper import PathHelper


class FileHelper:
    """

    """

    @staticmethod
    def get_base_name(file_name: str) -> str:
        """
        获取给定路径的文件名称部分(带扩展名)
        :param file_name:可以是文件的全名称也可以是部分名称
        :return:
        """
        return os.path.basename(file_name)

    @classmethod
    def get_base_name_no_extension(cls, file_name: str) -> str:
        """
        获取给定路径的文件名称部分(不带扩展名)
        :param file_name:
        :return:
        """
        base_name = cls.get_base_name(file_name)
        extension_name = cls.get_extension_name(file_name)
        return StringHelper.replace(base_name, extension_name, "")

    pass

    @staticmethod
    def get_extension_name(file_name: str) -> str:
        """
        获取文件的扩展名(带符号“.”)
        :param file_name:可以是文件的全名称也可以是基本名称
        :return:
        """
        return pathlib.Path(file_name).suffix

    @staticmethod
    def get_path_name(file_name: str) -> str:
        """
        获取文件的路径部分
        :param file_name:
        :return:
        """
        filepath, filename = os.path.split(file_name)
        return filepath

    @classmethod
    def load(cls, file_full_name: str) -> object:
        """

        :param file_full_name:
        :return:
        """
        file_encoding = cls.get_encoding(file_full_name)

        with open(file_full_name, "r", encoding=file_encoding) as file_pointer:
            data = file_pointer.read()
        pass

        return data

    @classmethod
    def load_with_lines(cls, file_full_name: str) -> str:
        """
        按照行的方式读取文件，返回行信息的list
        :param file_full_name:
        :return: 行信息的list
        """
        file_encoding = cls.get_encoding(file_full_name)

        with open(file_full_name, "r", encoding=file_encoding) as file_pointer:
            data = file_pointer.readlines()
        pass

        return data

    @classmethod
    def load_with_line(cls, file_full_name: str, line_callback: callable) -> None:
        """
        按行读取文件，每读取一行进行一次处理（调用line_callback）,对大文件尤其有效
        :param str file_full_name:
        :param function line_callback: 在每行上进行回调的函数，类似：line_callback(line),其中参数 line 为读出的每行的内容
        :return:
        """
        file_encoding = cls.get_encoding(file_full_name)
        with open(file_full_name, "r", encoding=file_encoding) as file_pointer:
            while True:
                line = file_pointer.readline()
                if line:
                    line_callback(line)
                else:
                    break
                pass
            pass
        pass

    @classmethod
    def create(cls, file_full_name: str, content: str = ""):
        """
        在目标位置创建文件
        :param str content: 待保存内容
        :param str file_full_name:待创建文件的全路径名称
        :return:
        """
        cls.store(file_full_name, content)

    @classmethod
    def store(cls, file_full_name, content, is_append=True, file_encoding=None):
        """
        保存文件在磁盘中
        :param str file_full_name:待保存文件的全路径名称
        :param content:待保存内容
        :param bool is_append: 新内容如是附加在原内容的后面，还是替代掉原内容（默认是附加在原内容后面）
        :return:
        """
        path_name = cls.get_path_name(file_full_name)
        PathHelper.ensure_exist(path_name)
        if not file_encoding:
            file_encoding = cls.get_encoding(file_full_name)
        pass

        if is_append:
            mode = 'a+'
        else:
            mode = 'w+'

        with open(file_full_name, mode, encoding=file_encoding) as file_pointer:
            file_pointer.write(content)
        pass

    @staticmethod
    def remove(file_full_name: str):
        """
        删除文件
        :param file_full_name:
        :return:
        """
        if os.path.exists(file_full_name):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(file_full_name)
            # os.unlink(path)
        pass

    @classmethod
    def delete(cls, file_full_name: str):
        """
        删除文件（remove方法的别名）
        :param file_full_name:
        :return:
        """
        cls.remove(file_full_name)

    @staticmethod
    def copy(source_file_full_name: str, target_dir_full_name: str, target_file_base_name: str = ""):
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
            pass

            if target_file_base_name == "":
                target_file_base_name = file_base_name
            pass

            target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

            shutil.copy(source_file_full_name, target_file_full_name)  # 复制文件

    @classmethod
    def move(cls, source_file_full_name: str, target_dir_full_name: str, target_file_base_name: str = ""):
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
    def is_exist(cls, file_full_name: str) -> bool:
        """
        判断为文件是否存在
        :param file_full_name: 带全路径的文件名称
        :return:
        """
        return os.path.isfile(file_full_name)

    @classmethod
    def rename(cls, old_file_full_name: str, new_file_name: str):
        """

        :param old_file_full_name: 旧有的带路径的文件全名称
        :param new_file_name: 要改名的新的名称（不带文件路径）
        :return:
        """
        # TODO:xiedali@20230608 需要加入一个当新文件存在时的处理策略的功能
        file_path = cls.get_path_name(old_file_full_name)
        new_file_full_name = PathHelper.combine(file_path, new_file_name)
        if cls.is_exist(new_file_full_name):
            new_file_full_name += f'({RandomHelper.create(8, RandomEnum.UpperLetters)})'
        pass

        os.rename(old_file_full_name, new_file_full_name)

    @staticmethod
    def get_image_type_name(file, h=None):
        return ImageHelper.get_image_type_name(file, h)

    pass

    @staticmethod
    def is_image_type(file_full_name: str) -> bool:
        return ImageHelper.is_image_type(file_full_name)

    pass

    @classmethod
    def modify(cls, file_full_name: str, func: callable, file_encoding=None):
        """
        修改文件名
        :param file_encoding: 文件的编码格式。如果不指定的话，那么系统自动判定
        :param func:对文件内容进行操作的函数，参数为文件的内容，返回值是修改后的内容
        :param file_full_name: 带全路径的文件名称
        :return:修改后的文件内容
        """
        if not file_encoding:
            file_encoding = cls.get_encoding(file_full_name)
        pass

        result_content = ''
        # 读取和写入文件
        with open(file_full_name, 'r', encoding=file_encoding) as r:
            content = r.read()
            # 对文件内容进行操作
            result_content = func(content)
            # 回写文件
            with open(file_full_name, 'w', encoding=file_encoding) as w:
                w.write(result_content)
            pass
        pass
        return result_content

    pass

    @staticmethod
    def get_encoding(file_full_name: str):
        with open(file_full_name, 'rb') as f:
            text = f.read()

        file_encoding = chardet.detect(text)['encoding']
        file_encoding_little = StringHelper.lower_all_chars(file_encoding)
        if file_encoding_little == 'gb2312' or 'gbk':
            file_encoding = 'ANSI'
        pass

        return file_encoding

    pass


pass
