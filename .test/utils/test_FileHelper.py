"""
 * @file   : test_FileHelper.py
 * @time   : 13:13
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.io.fileHelper import FileHelper


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

    file_full_name = "../_res/myContent.txt"
    actual = FileHelper.load(file_full_name)
    expected = ""
    assert actual == expected


