"""
 * @file   : test_FileHelper.py
 * @time   : 13:13
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from hilandBasicLibrary.data.randomHelper import RandomHelper
from hilandBasicLibrary.io.fileHelper import FileHelper
from hilandBasicLibrary.io.ioHelper import IOHelper
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


def test_remove():
    source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\aa.txt"
    target_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\ABB"
    FileHelper.copy(source_file_full_name, target_dir_full_name)
    target_file_full_name = PathHelper.combine(target_dir_full_name, "aa.txt")
    actual = os.path.isfile(target_file_full_name)
    expected = True
    assert actual == expected

    FileHelper.remove(target_file_full_name)
    actual = os.path.isfile(target_file_full_name)
    expected = False
    assert actual == expected


def test_move():
    # 1. 创建一个中间文件。
    # 2. 然后中间文件上进行测试（将这个中间文件move到一个新目录）。
    # 3. 最后再删除新目录下的文件作为善后工作。
    # 其中第二步是本单元测试的标的

    source_file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\aa.txt"
    middle_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\ABB"
    FileHelper.copy(source_file_full_name, middle_dir_full_name)
    middle_file_full_name = PathHelper.combine(middle_dir_full_name, "aa.txt")
    actual = os.path.isfile(middle_file_full_name)
    expected = True
    assert actual == expected

    random_string = RandomHelper.create()
    last_dir_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target"
    last_dir_full_name = PathHelper.combine(last_dir_full_name, random_string)
    FileHelper.move(middle_file_full_name, last_dir_full_name)
    actual = os.path.isfile(middle_file_full_name)
    expected = False
    assert actual == expected

    # 善后，删除目录
    IOHelper.remove(last_dir_full_name)
    actual = PathHelper.determine_is_exist(last_dir_full_name)
    expected = False
    assert actual == expected


file_content = ""


def test_load_line():
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\source\aa.txt"
    FileHelper.load_with_line(file_full_name, __line_callback)
    actual = file_content
    expected = "1. 第一行\n2. 第二行\n3. 第三行\n4. 第四行"
    assert actual == expected


def __line_callback(line_content):
    global file_content
    file_content = file_content + line_content


def test_store():
    content = "qingdao"
    file_full_name = r"E:\myworkspace\BasicLibrary.PY\.test\_res\target\abcde.txt"
    FileHelper.store(file_full_name, content)
    actual = 0
    expected = 0
    assert actual == expected
