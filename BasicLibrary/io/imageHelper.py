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

from BasicLibrary.data.enumHelper import EnumHelper
from BasicLibrary.enums import ImageTypeEnum


class ImageHelper:

    @staticmethod
    def test_jpeg(h, f):
        """

        :param h:
        :param f:
        :return:
        ▌参考资料：
        https://blog.51cto.com/u_15127617/3265040
        https://bugs.python.org/issue28591
        """
        # 以下是为了屏蔽对变量f的warning
        # noinspection all
        f = f

        if h[6:10] in (b'JFIF', b'Exif') or h[:2] == b'\xff\xd8':
            return 'jpeg'

        return None

    pass

    @classmethod
    def what(cls, file, h=None):
        """
        修正 imghdr库对 jpeg格式判定的bug
        :param file:
        :param h:
        :return:
        """
        imghdr.tests.insert(0, cls.test_jpeg)
        return imghdr.what(file, h)

    pass

    @classmethod
    def get_image_type_name(cls, file, h=None):
        return cls.what(file, h)

    pass

    @classmethod
    def is_image_type(cls, file, h=None):
        file_type = cls.what(file, h)

        return EnumHelper.is_exist_value(ImageTypeEnum, file_type)

    pass

    @staticmethod
    def get_base64(image_file_full_name: str):
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


pass
