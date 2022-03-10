import os
import sys
from builtins import *


class IOHelper:
    @staticmethod
    def get_illegal_chars_in_file_system(include_separator=True):
        """
        文件系统（文件目录或文件名称）内不使用的字符
        :param include_separator: 是否包含目录分割符号 "\\" 和 "/"
        :return:
        """
        normal = ["?", "*", '"', ":", "<", ">", "|"]
        if include_separator:
            normal.append("\\")
            normal.append("/")

        return normal

    @classmethod
    def get_safe_file_system_name(cls, filename, safe_char="_", include_separator=True):
        """
        在文件系统内获取安全可用的名称
        :param filename:
        :param safe_char:
        :param include_separator:
        :return:
        """
        chars = cls.get_illegal_chars_in_file_system(include_separator)
        for c in chars:
            filename = filename.replace(c, safe_char)

        return filename

    @staticmethod
    def get_using_memory(data):
        """
        获取对象占用的内存大小（单位为字节）
        :param data:
        :return:
        """
        return sys.getsizeof(data)
