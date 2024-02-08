"""
 * @file   : student.py
 * @time   : 14:49
 * @date   : 2022/1/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.pattern.singleton import Singleton


@Singleton
class Student(object):
    def __init__(self):
        pass

    def say_hello(self):
        print("hello" + self.__class__)

    @staticmethod
    def get_language() -> str:
        """
        获取学生的语言
        :return:
        """
        return "中文"

    pass

    def get_hi(self, your_name: str):
        """
        获取打招呼的信息
        :param your_name:
        :return:
        """
        return "你好" + your_name

    pass
