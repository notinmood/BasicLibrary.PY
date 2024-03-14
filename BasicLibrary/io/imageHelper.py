"""
 * @file   : imageMate.py
 * @time   : 11:46
 * @date   : 2023/10/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import base64
import imghdr
from os import PathLike

from BasicLibrary.data.enumHelper import EnumHelper
from BasicLibrary.enums import ImageTypeEnum

from pathlib import Path

from PIL import Image


class ImageHelper:
    @staticmethod
    def get_base64(image_file_full_name: PathLike | str):
        """
        获取图片的base64编码
        :param image_file_full_name:
        :return:
        """
        with open(image_file_full_name, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        pass

        return image_data

    pass

    @classmethod
    def is_image_type(cls, file, h=None):
        file_type = cls.__what(file, h)

        return EnumHelper.is_exist_value(ImageTypeEnum, file_type)

    pass

    @staticmethod
    def get_size(image_full_path: str | Path) -> tuple[int, int]:
        """
        获取图片的尺寸，返回一个元组:（width, height）
        :param image_full_path:
        :return:一个元组:（width, height）
        """
        image = Image.open(image_full_path)
        return image.size

    pass

    @classmethod
    def get_format(cls, image_full_path: str | Path) -> str | None:
        """
        获取图片的格式（如果是非图片格式，返回None）
        :param image_full_path:
        :return:
        """
        if cls.is_image_type(image_full_path):
            image = Image.open(image_full_path)
            return image.format.lower()
        pass

        return None

    pass

    @classmethod
    def get_image_type_name(cls, file_full_name: str | Path):
        """
        获取图片的类型名称（如果是非图片格式，返回None）（get_format的别名）
        :param file_full_name:
        :return:
        """
        return cls.get_format(file_full_name)

    pass

    @classmethod
    def what(cls, file_full_name: str | Path):
        """
        获取图片的类型名称（如果是非图片格式，返回None）（get_format的别名）
        :param file_full_name:
        :return:
        """
        return cls.get_format(file_full_name)

    @staticmethod
    def __test_jpeg(h, f):
        """

        :param h:
        :param f:
        :return:
        ▌参考资料：
        https://blog.51cto.com/u_15127617/3265040
        https://bugs.python.org/issue28591
        """
        # 以下是为了屏蔽对变量f的warning
        _f = f

        if h[6:10] in (b'JFIF', b'Exif') or h[:2] == b'\xff\xd8':
            return 'jpeg'

        return None

    @classmethod
    def __what(cls, file, h=None):
        """
        修正 imghdr库对 jpeg格式判定的bug
        :param file:
        :param h:
        :return:
        """
        imghdr.tests.insert(0, cls.__test_jpeg)
        return imghdr.what(file, h)

    pass


pass
