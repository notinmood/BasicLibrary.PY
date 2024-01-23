import os
import re
import sys

from BasicLibrary.io.dirHelper import DirHelper
from BasicLibrary.io.fileHelper import FileHelper


class IOHelper:
    """

    """

    @staticmethod
    def get_illegal_chars_in_file_system(include_separator=True):
        """
        文件系统（文件目录或文件名称）内不能使用的字符
        :param include_separator: 是否包含目录分割符号 "\\" 和 "/"
        :return:
        """
        normal = ["?", "*", '"', ":", "<", ">", "|"]
        if include_separator:
            normal.append("\\")
            normal.append("/")
        pass

        return normal

    pass

    @classmethod
    def get_file_system_safe_name(cls, filename: os.PathLike | str, safe_char="_", include_path_separator=True):
        """
        在文件系统内获取安全可用的名称
        :param filename:
        :param safe_char: 非法字符的替代字符
        :param include_path_separator: 是否可以包含 路径分隔符（此参数目前暂时未做判断）
        :return:
        """
        # chars = cls.get_illegal_chars_in_file_system(include_path_separator)
        # for c in chars:
        #     filename = filename.replace(c, safe_char)

        # noinspection all
        include_path_separator = include_path_separator

        # 目前采用以下方法，可以清除更多非法字符
        filename = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9_.]+', safe_char, filename)

        return filename

    pass

    @staticmethod
    def get_using_memory(data):
        """
        获取对象占用的内存大小（单位为字节）
        :param data:
        :return:
        """
        return sys.getsizeof(data)

    pass

    @staticmethod
    def remove(path: os.PathLike | str):
        if os.path.isfile(path):
            FileHelper.remove(path)
        else:
            DirHelper.remove(path)
        pass

    pass


pass
