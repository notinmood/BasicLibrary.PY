"""
 * @file   : test_FileHelper.py
 * @time   : 13:13
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.pathHelper import PathHelper
from hilandBasicLibrary.projectHelper import ProjectHelper


def test_get_file_base_name():
    file_name = "test_FileHelper.py"
    actual = FileHelper.get_base_name(file_name)
    expected = "test_FileHelper.py"
    assert actual == expected

    file_name = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils\\test_FileHelper.py"
    actual = FileHelper.get_base_name(file_name)
    expected = "test_FileHelper.py"
    assert actual == expected


def test_get_file_extension_name():
    file_name = "test_FileHelper.py"
    actual = FileHelper.get_extension_name(file_name)
    expected = ".py"
    assert actual == expected

    file_name = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils\\test_FileHelper.py"
    actual = FileHelper.get_extension_name(file_name)
    expected = ".py"
    assert actual == expected

    file_name = ".env"
    actual = FileHelper.get_extension_name(file_name)
    expected = ""
    assert actual == expected


def test_get_path_name():
    file_name = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils\\test_FileHelper.py"
    actual = FileHelper.get_path_name(file_name)
    expected = "E:\\myworkspace\\BasicLibrary.PY\\.test\\utils"
    assert actual == expected

    file_name = "test_FileHelper.py"
    actual = FileHelper.get_path_name(file_name)
    expected = ""
    assert actual == expected


def test_load():
    root_path = ProjectHelper.get_root_physical_path()
    file_name = ".test\\_res\\myContent.txt"
    file_full_name = PathHelper.combine(root_path, file_name)
    actual = FileHelper.load(file_full_name)
    expected = '第一行内容\n第二行信息\n"第三行数据"\n\n5th. data'
    assert actual == expected


def test_copy():
    root_path = ProjectHelper.get_root_physical_path()
    file_name = ".test\\_res\\source\\aa.txt"
    source = PathHelper.combine(root_path, file_name)

    target_dir = PathHelper.combine(root_path, ".test\\_res\\target")
    target_base_name = "ww.pp"
    FileHelper.copy(source, target_dir, target_base_name)

    target_file = PathHelper.combine(target_dir, target_base_name)
    actual = PathHelper.determine_is_exist(target_file)
    expected = True
    assert actual == expected
