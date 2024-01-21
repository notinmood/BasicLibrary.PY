"""
 * @file   : base64Helper.py
 * @time   : 21:51
 * @date   : 2024/1/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64
from os import PathLike


class Base64Helper(object):
    """
    Base64编码解码辅助类
    """

    @staticmethod
    def encode_string(original_data: str, encoding="utf-8") -> bytes:
        """

        :param original_data:
        :param encoding:
        :return:
        """
        return base64.b64encode(original_data.encode(encoding))

    @staticmethod
    def decode_string(encoded_data: bytes, encoding="utf-8") -> str:
        """

        :param encoded_data:
        :param encoding:
        :return:
        """
        return base64.b64decode(encoded_data).decode(encoding)

    @staticmethod
    def encode_bytes(original_bytes: bytes):
        """
        对普通的字节串进行base64编码。
        :param original_bytes:
        :return:
        """
        return base64.b64encode(original_bytes)

    @staticmethod
    def decode_bytes(encoded_bytes: bytes):
        """
        对base64编码的字节串进行解码。
        :param encoded_bytes:
        :return:
        """
        return base64.b64decode(encoded_bytes)

    pass

    @staticmethod
    def encode_file(in_file_full_name: PathLike, out_file_full_name: PathLike):
        """
        对给定的文件进行base64编码，并保存到另一个文件中。
        :param in_file_full_name:
        :param out_file_full_name:
        :return:
        """
        with open(in_file_full_name, "rb") as in_file:
            with open(out_file_full_name, "wb") as out_file:
                base64.encode(in_file, out_file)
            pass
        pass

    @staticmethod
    def decode_file(in_file_full_name: PathLike, out_file_full_name: PathLike):
        """
        对给定的文件进行base64解码，并保存到另一个文件中。
        :param in_file_full_name:
        :param out_file_full_name:
        :return:
        """
        with open(in_file_full_name, "rb") as in_file:
            with open(out_file_full_name, "wb") as out_file:
                base64.decode(in_file, out_file)
            pass
        pass


pass
