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

from os import PathLike
from typing import Callable

import chardet

from BasicLibrary.data.listHelper import ListHelper
from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.enums import RandomEnum
from BasicLibrary.io.imageHelper import ImageHelper
from BasicLibrary.io.pathHelper import PathHelper


class FileHelper:
    """
    文件操作工具类
    为了统一使用体验，本类将os.path和pathlib、shutil等模块中的方法进行了静态封装
    """

    @staticmethod
    def get_base_name(file_name: PathLike | str) -> str:
        """
        获取给定路径的文件名称部分(带扩展名)
        :param file_name:可以是文件的全名称也可以是部分名称
        :return:
        """
        return os.path.basename(file_name)

    @classmethod
    def get_base_name_no_extension(cls, file_name: PathLike | str) -> str:
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
    def get_extension_name(file_name: PathLike | str) -> str:
        """
        获取文件的扩展名(带符号“.”)
        :param file_name:可以是文件的全名称也可以是基本名称
        :return:
        """
        return pathlib.Path(file_name).suffix

    @staticmethod
    def get_path_name(file_name: PathLike | str) -> str:
        """
        获取文件的路径部分
        :param file_name:
        :return:
        """
        filepath, _ = os.path.split(file_name)
        return filepath

    @classmethod
    def load(cls, file_full_name: PathLike | str, encoding: str = "") -> bytes | str:
        """
        读取文件内容
        :param encoding:
        :param file_full_name:
        :return:
        """
        if not encoding:
            encoding = cls.get_encoding(file_full_name)
        pass

        with open(file_full_name, "r", encoding=encoding) as file_pointer:
            data = file_pointer.read()
        pass

        return data

    @classmethod
    def get(cls, file_full_name: PathLike | str, encoding: str = "") -> bytes | str:
        """
        读取文件内容（load方法的别名）
        :param encoding:
        :param file_full_name:
        :return:
        """
        return cls.load(file_full_name, encoding)

    @classmethod
    def load_with_lines(cls, file_full_name: PathLike | str) -> list[str]:
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
    def load_with_line(cls, file_full_name: PathLike | str, line_callback: callable) -> None:
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
    def create(cls, file_full_name: PathLike | str, content: str = ""):
        """
        在目标位置创建文件(store方法的别名)
        :param str content: 待保存内容
        :param str file_full_name:待创建文件的全路径名称
        :return:
        """
        cls.store(file_full_name, content)

    @classmethod
    def save(cls, file_full_name: PathLike | str, content: str = "", is_append=False, file_encoding=None):
        """
        在目标位置创建文件(store方法的别名)
        :param file_encoding:
        :param is_append: 新内容如是附加在原内容的后面，还是替代掉原内容（默认是替换）
        :param str content: 待保存的内容
        :param str file_full_name:待创建文件的全路径名称
        :return:
        """
        cls.store(file_full_name, content, is_append, file_encoding)

    @classmethod
    def append(cls, file_full_name: PathLike | str, content: str = ""):
        """
        向目标文件的末尾追加内容
        :param file_full_name:待追加内容文件的全路径名称
        :param content:待追加的内容
        :return:
        """
        cls.store(file_full_name, content, is_append=True)

    pass

    @classmethod
    def store(cls, file_full_name: PathLike | str, content, is_append=False, file_encoding=None):
        """
        保存文件在磁盘中
        :param file_encoding:
        :param str file_full_name:待保存文件的全路径名称
        :param content:待保存内容
        :param bool is_append: 新内容如是附加在原内容的后面，还是替代掉原内容（默认是替换）
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
    def remove(file_full_name: PathLike | str):
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
    def delete(cls, file_full_name: PathLike | str):
        """
        删除文件（remove方法的别名）
        :param file_full_name:
        :return:
        """
        cls.remove(file_full_name)

    @staticmethod
    def copy(source_file_full_name: PathLike | str, target_dir_full_name: PathLike | str,
             target_file_base_name: str = ""):
        """
        复制文件
        :param source_file_full_name:带全路径的源文件
        :param target_dir_full_name:目标文件夹
        :param target_file_base_name:复制后的文件名称（默认空，表示使用源文件的名称）
        :return:
        """
        if os.path.isfile(source_file_full_name):
            _, file_base_name = os.path.split(source_file_full_name)  # 分离文件名和路径
            if not os.path.exists(target_dir_full_name):
                os.makedirs(target_dir_full_name)  # 创建路径
            pass

            if target_file_base_name == "":
                target_file_base_name = file_base_name
            pass

            target_file_full_name = PathHelper.combine(target_dir_full_name, target_file_base_name)

            shutil.copy(source_file_full_name, target_file_full_name)  # 复制文件
        pass

    pass

    @classmethod
    def move(cls, source_file_full_name: PathLike | str, dest_dir_full_name: PathLike | str,
             dest_file_base_name: str = ""):
        """
        移动文件
        :param source_file_full_name:
        :param dest_dir_full_name:
        :param dest_file_base_name:
        :return:
        """
        cls.copy(source_file_full_name, dest_dir_full_name, dest_file_base_name)
        cls.remove(source_file_full_name)
        # TODO:xiedali@2023-12-31 需要通过单元测试以下方法，然后代替上面的实现
        # if os.path.isfile(source_file_full_name):
        #     if not dest_file_base_name:
        #         dest_file_base_name = os.path.basename(source_file_full_name)
        #     pass
        #
        #     dest_file_full_name = PathHelper.combine(dest_dir_full_name, dest_file_base_name)
        #     os.rename(source_file_full_name, dest_file_full_name)
        # pass

    pass

    @classmethod
    def is_exist(cls, file_full_name: PathLike | str) -> bool:
        """
        判断为文件是否存在
        :param file_full_name: 带全路径的文件名称
        :return:
        """
        return os.path.isfile(file_full_name)

    pass

    @classmethod
    def is_file(cls, file_full_name: PathLike | str) -> bool:
        """
        判断为文件是否存在(is_exist的别名)
        :param file_full_name: 带全路径的文件名称
        :return:
        """
        return cls.is_exist(file_full_name)

    pass

    @classmethod
    def rename(cls, old_file_full_name: PathLike | str, new_file_base_name: str):
        """

        :param old_file_full_name: 旧有的带路径的文件全名称
        :param new_file_base_name: 要改名的新的名称（不带文件路径）
        :return:
        """
        # TODO:xiedali@20230608 需要加入一个当新文件存在时的处理策略的功能
        file_path = cls.get_path_name(old_file_full_name)
        new_file_full_name = PathHelper.combine(file_path, new_file_base_name)
        if cls.is_exist(new_file_full_name):
            new_file_full_name += f'({RandomHelper.create(8, RandomEnum.UpperLetters)})'
        pass

        os.rename(old_file_full_name, new_file_full_name)

    pass

    @staticmethod
    def get_image_type_name(file: PathLike | str):
        """
        获取图片类型名称
        :param file:
        :param h:
        :return:
        """
        return ImageHelper.get_image_type_name(file)

    pass

    @staticmethod
    def is_image_type(file_full_name: PathLike | str) -> bool:
        """
        判断是否为图片类型
        :param file_full_name:
        :return:
        """
        return ImageHelper.is_image_type(file_full_name)

    pass

    @classmethod
    def modify[P](cls, file_full_name: PathLike | str, func: Callable[[str, P], str], file_encoding=None,
                  **kwargs_for_func):
        """
        修改文件内容
        :param file_encoding: 文件的编码格式。如果不指定的话，那么系统自动判定
        :param func:对文件内容进行操作的函数，参数为文件原来的内容，返回值是修改后的内容
        :param file_full_name: 带全路径的文件名称
        :return:修改后的文件内容
        """
        if not file_encoding:
            file_encoding = cls.get_encoding(file_full_name)
        pass

        # content = ''
        # result_content = ''

        # 读取和写入文件
        with open(file_full_name, 'r', encoding=file_encoding) as r:
            content = r.read()
            # 对文件内容进行操作
            result_content = func(content, **kwargs_for_func)
        pass

        # 如果文件内容没有变化，那么直接返回
        if result_content == content:
            return result_content
        pass

        # 回写文件
        with open(file_full_name, 'w', encoding=file_encoding) as w:
            w.write(result_content)
        pass

        return result_content

    pass

    @classmethod
    def get_encoding(cls, file_full_name: PathLike | str):
        """
        获取文件编码格式（如果是中文本地语言区域的文件编码，统一返回为ANSI）
        :param file_full_name:
        :return:
        """
        if not file_full_name or not cls.is_exist(file_full_name):
            return 'utf-8'
        pass

        with open(file_full_name, 'rb') as f:
            text = f.read()

        file_encoding = chardet.detect(text)['encoding']
        if not file_encoding:
            return 'utf-8'
        pass

        file_encoding_little = StringHelper.lower_all_chars(file_encoding)
        if file_encoding_little in ('gb2312', 'gbk'):
            file_encoding = 'ANSI'
        pass

        return file_encoding

    pass

    @staticmethod
    def get_size(file_full_name: PathLike | str) -> int:
        """
        它以字节为单位返回指定路径的大小。如果文件不存在或无法访问，则引发OSError。
        :param file_full_name:
        :return:
        """
        return os.path.getsize(file_full_name)

    pass

    @staticmethod
    def is_match_extension_name(file_name: PathLike | str, extension_names=".*"):
        """
        检查文件名是否匹配指定的扩展名列表。
        :param file_name:全名称或者基本名称
        :param extension_names:文件的扩展名列表，多个扩展名用逗号或者分号分隔
        :return:
        """
        extension_names= StringHelper.replace(extension_names, ",", ";")
        extension_names = StringHelper.lower_all_chars(extension_names)
        file_name = StringHelper.lower_all_chars(file_name)
        extension_name_list = StringHelper.explode(extension_names, ";")
        extension_name_list_fixed = []
        for _item in extension_name_list:
            if not _item.startswith("."):
                _item = "." + _item
            pass
            extension_name_list_fixed.append(_item)
        pass

        # if extension_name_list_fixed.__contains__(".*"):
        #     return True
        # pass

        if ListHelper.has(extension_name_list_fixed, ".*"):
            return True
        pass

        return file_name.endswith(tuple(extension_name_list_fixed))

    pass


pass
