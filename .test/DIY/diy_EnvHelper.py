"""
 * @file   : diy_EnvHelper.py
 * @time   : 18:53
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.environment.envHelper import EnvHelper


def get_os_name():
    os_name = EnvHelper.get_os_name()
    print(os_name)


def determine_is_windows():
    result = EnvHelper.determine_is_windows()
    print(result)


if __name__ == '__main__':
    get_os_name()  # Windows
    determine_is_windows()  # True
