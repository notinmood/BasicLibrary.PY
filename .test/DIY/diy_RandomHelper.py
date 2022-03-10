"""
 * @file   : diy_RandomHelper.py
 * @time   : 19:54
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.randomHelper import RandomHelper


def create():
    result = RandomHelper.create(10)
    print(result)


if __name__ == '__main__':
    create()
