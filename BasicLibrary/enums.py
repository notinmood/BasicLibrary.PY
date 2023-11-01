"""
 * @file   : enums.py
 * @time   : 19:59
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from enum import Enum
from BasicLibrary.data.enumBase import EnumBase

"""
说明：如果要使用枚举上的某些静态快捷方法，需要继承EnumBase；
否则，直接继承Enum即可。
"""


class RandomEnum(Enum):
    """

    """
    LowerLetters = "ascii_lowercase"
    UpperLetters = "ascii_uppercase"
    AllLetters = "ascii_letters"
    Digits = "digits"
    Punctuation = "punctuation"
    All = "all"


pass


class OSNameEnum(Enum):
    """

    """
    Windows = "Windows"
    Linux = "Linux"
    Other = "Other"


pass


class ImageTypeEnum(EnumBase):
    """
    图像类型枚举
    """
    RGB = "rgb"  # SGI 图像库文件
    GIF = "gif"  # ‘gif’ GIF 87a 和 89a 文件
    PBM = "pbm"  # ‘pbm’ 便携式位图文件
    PGM = "pgm"  # ‘pgm’ 便携式灰度图文件
    PPM = "ppm"  # ‘ppm’ 便携式像素表文件
    TIFF = "tiff"  # ‘tiff’ TIFF 文件
    RAST = "rast"  # ‘rast’ Sun 光栅文件
    XBM = "xbm"  # ‘xbm’ X 位图文件
    JPEG = "jpeg"  # ‘jpeg’ JFIF 或 Exif 格式的 JPEG 数据
    BMP = "bmp"  # ‘bmp’ BMP 文件
    PNG = "png"  # ‘png’ 便携式网络图像
    WEBP = "webp"  # ‘webp’ WebP 文件
    EXR = "exr"  # ‘exr’ OpenEXR 文件


pass
