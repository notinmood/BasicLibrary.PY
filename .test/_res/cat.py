"""
 * @file   : cat.py
 * @time   : 15:51
 * @date   : 2024/2/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _res.animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        """
        构造器
        :param name: 名字
        :param age: 年龄
        """
        super().__init__(name, age)
