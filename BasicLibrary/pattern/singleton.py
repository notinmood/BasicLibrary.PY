"""
 * @file   : singleton.py
 * @time   : 13:56
 * @date   : 2022/1/6
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


class Singleton(object):
    """
    单例装饰器
    使用方法:在目标类上加上@Singleton即可以实现单例效果
    """
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        pass

        return self._instance[self._cls]
