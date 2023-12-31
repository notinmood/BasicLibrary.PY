"""
 * @file   : test_DirHelper.py
 * @time   : 19:37
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path
from os import path

from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.io.dirHelper import DirHelper
from BasicLibrary.io.ioHelper import IOHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper


def test_remove():
    root_path = ProjectHelper.get_root_physical_path()
    dir_base_name = RandomHelper.create(10)
    dir_full_name = PathHelper.combine(root_path, ".test", "_res", "target", dir_base_name)
    DirHelper.ensure_exist(dir_full_name)
    actual = os.path.isdir(dir_full_name)
    expected = True
    assert actual == expected

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


def test_get_sub_dirs():
    root_path = ProjectHelper.get_root_physical_path()
    local_path = ".test/_res/目录结构测试基础设施"
    target_dir = PathHelper.combine(root_path, local_path)

    actual = DirHelper.get_sub_dirs(target_dir)
    expected = [PathHelper.combine(root_path, local_path, "目录A"),
                PathHelper.combine(root_path, local_path, "目录B"),
                PathHelper.combine(root_path, local_path, "目录C")]
    assert actual == expected


pass


def test_is_exist1():
    root_path = ProjectHelper.get_root_physical_path()
    dir_full_name = path.join(root_path, ".test/_res/target")
    actual = DirHelper.is_dir(dir_full_name)
    expected = True
    assert actual == expected


pass


def test_is_exist2():
    root_path = ProjectHelper.get_root_physical_path()
    dir_full_name = path.join(root_path, ".test/_res/target_xx")
    actual = DirHelper.is_dir(dir_full_name)
    expected = False
    assert actual == expected


pass


def test_is_exist3():
    root_path = ProjectHelper.get_root_physical_path()
    dir_full_name = path.join(root_path, ".test/_res/target/ww.pp")
    actual = DirHelper.is_dir(dir_full_name)
    expected = False
    assert actual == expected


pass
