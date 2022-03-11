"""
 * @file   : test_DirHelper.py
 * @time   : 19:37
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.dirHelper import DirHelper
from hilandBasicLibrary.io.ioHelper import IOHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.projectHelper import ProjectHelper


def test_remove():
    dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\sSlzdeVX"
    DirHelper.remove(dir_full_name)

    actual = os.path.isdir(dir_full_name)
    expected = False
    assert actual == expected


def test_ensure_exist():
    root_path = ProjectHelper.get_root_physical_path()
    middle_dir = ".test/_res/target"
    random_string = RandomHelper.create()
    target_dir = PathHelper.combine(root_path, middle_dir, random_string)

    PathHelper.ensure_exist(target_dir)
    actual = PathHelper.determine_is_exist(target_dir)
    expected = True
    assert actual == expected

    # 善后，删除掉这个目录
    IOHelper.remove(target_dir)
    actual = PathHelper.determine_is_exist(target_dir)
    expected = False
    assert actual == expected
