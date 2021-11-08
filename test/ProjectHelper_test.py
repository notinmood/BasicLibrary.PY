"""
 * @file   : ProjectHelper_test.py
 * @time   : 22:16
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from HilandBasicLibrary.ProjectHelper import *


def test_get_root_physical_path():
    """
    这个目录是否正确需要手工验证
    :return:
    """
    actual = ProjectHelper.get_root_physical_path();
    expected = ""
    print("当前项目的物理根目录为{}".format(actual))
    assert actual != expected
