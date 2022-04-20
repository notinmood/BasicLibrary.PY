"""
 * @file   : envHelper.py
 * @time   : 18:23
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import os
import platform

from hilandBasicLibrary.enums import OSNameEnum


class EnvHelper:
    """

    """

    @classmethod
    def determine_is_windows(cls):
        return cls.get_os_name() == OSNameEnum.Windows

    @staticmethod
    def get_os_name():
        """
        获取服务器操作系统的类型名称（Windows、Linux）
        :return:操作系统的类型名称（Windows、Linux）
        """
        os_name_string = platform.system()
        match os_name_string:
            case "Windows":
                return OSNameEnum.Windows
            case "Linux":
                return OSNameEnum.Linux
            case _:
                return OSNameEnum.Other

    @staticmethod
    def get_path_separator():
        """
        获取跟 os 相关的路径分隔符（Windows下用 “\\”;linux 下用 "/"）
        :return:
        """
        return os.path.sep
