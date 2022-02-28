"""
 * @file   : pathHelper.py
 * @time   : 8:37
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path


class PathHelper:
    @staticmethod
    def combine(*args):
        """
        将给定的各个部分，组装成一个标准路径
        :param args:
        :return:
        """
        return os.path.join(*args)

    @staticmethod
    def get_file_base_name(path):
        """
        获取给定路径的文件名称部分
        :param path:
        :return:
        """
        return os.path.basename(path)

    @staticmethod
    def get_dir_name(path):
        """
        获取给定路径的目录部分
        :param str path:
        :return:
        """
        return os.path.dirname(path)

    @staticmethod
    def get_current_path():
        """
        获取当前程序的运行路径
        :return:
        """
        return os.getcwd()
