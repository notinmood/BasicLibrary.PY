"""
 * @file   : test_DirHelper.py
 * @time   : 19:37
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.projectHelper import ProjectHelper


def test_ensure_exist():
    root_path = ProjectHelper.get_root_physical_path()
    target_dir = ".test/_res/target"
    random_string = RandomHelper.create()
    target_dir = PathHelper.combine(root_path, target_dir, random_string)

    PathHelper.ensure_exist(target_dir)
    actual = PathHelper.determine_is_exist(target_dir)
    expected = True
    assert actual == expected
