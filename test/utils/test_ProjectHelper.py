"""
 * @file   : test_ProjectHelper.py
 * @time   : 22:16
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

from hilandBasicLibrary.projectHelper import *


def test_get_root_physical_path():
    """
    验证项目的根目录
    :return:
    """
    actual = ProjectHelper.get_root_physical_path()
    expected = os.path.dirname(os.path.dirname(os.getcwd()))
    print("本地获取到的物理根目录为{}".format(expected))
    print("类库获取到的物理根目录为{}".format(actual))
    assert actual == expected
