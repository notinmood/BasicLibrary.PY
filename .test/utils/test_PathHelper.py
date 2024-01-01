"""
 * @file   : test_PathHelper.py
 * @time   : 8:46
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.environment.envHelper import EnvHelper
from BasicLibrary.io.pathHelper import PathHelper


def test_combine():
    p1 = "M"
    p2 = "aa"
    p3 = "bb"
    p4 = "cc"

    actual = PathHelper.combine(p1, p2, p3, p4)
    expected = "M\\aa\\bb\\cc"
    assert actual == expected


def test_get_root_path():
    actual = PathHelper.get_root_path()
    expected = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    assert actual == expected


def test_get_dir_name1():
    actual = PathHelper.get_dir_name()

    root = PathHelper.get_root_path()
    expected = "{}\\.test\\utils".format(root)
    assert actual == expected


def test_get_dir_name2():
    data = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils\\test_PathHelper.py"
    actual = PathHelper.get_dir_name(data)
    expected = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils"
    assert actual == expected

    actual = PathHelper.get_dir_name(data, 2)
    expected = "E:\\myworkspace\\BasicLibrary.PY\\.test"
    assert actual == expected

    actual = PathHelper.get_dir_name(data, 4)
    expected = "E:\\myworkspace"
    assert actual == expected


def test_real_path():
    file_name = "E:/myworkspace/BasicLibrary.PY\\.test\\utils\\test_FileHelper.py"
    actual = PathHelper.get_formatted_path(file_name)
    expected = StringHelper.replace(file_name, "/", EnvHelper.get_path_separator())
    expected = StringHelper.replace(expected, "\\", EnvHelper.get_path_separator())
    assert actual == expected


def test_get_current_physical_path():
    actual = PathHelper.get_current_physical_path()
    expected = os.path.join(PathHelper.get_root_path(), ".test\\utils")
    assert actual == expected


pass
