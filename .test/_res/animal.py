"""
 * @file   : animal.py
 * @time   : 15:52
 * @date   : 2024/2/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Animal:
    def __init__(self, name, age):
        """
        构造器
        :param name: 名字
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def about_me(self):
        """
        自我介绍
        :return:
        """
        return f"我是{self.name}，我{self.age}岁了"


pass
