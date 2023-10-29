"""
 * @file   : test_FileHelper.py
 * @time   : 13:13
 * @date   : 2022/3/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os.path

from BasicLibrary.data.randomHelper import RandomHelper
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.enums import RandomEnum, ImageTypeEnum
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.ioHelper import IOHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper


def test_get_file_base_name():
    file_name = "test_FileHelper.py"
    actual = FileHelper.get_base_name(file_name)
    expected = "test_FileHelper.py"
    assert actual == expected

    file_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), ".test\\utils\\test_FileHelper.py")
    actual = FileHelper.get_base_name(file_name)
    expected = "test_FileHelper.py"
    assert actual == expected

def test_get_file_base_name_no_extension():
    file_name = "test_FileHelper.py"
    actual = FileHelper.get_base_name_no_extension(file_name)
    expected = "test_FileHelper"
    assert actual == expected

    file_name = "test_FileHelper"
    actual = FileHelper.get_base_name_no_extension(file_name)
    expected = "test_FileHelper"
    assert actual == expected
pass

def test_get_file_extension_name():
    file_name = "test_FileHelper.py"
    actual = FileHelper.get_extension_name(file_name)
    expected = ".py"
    assert actual == expected

    file_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), ".test\\utils\\test_FileHelper.py")
    actual = FileHelper.get_extension_name(file_name)
    expected = ".py"
    assert actual == expected

    file_name = ".env"
    actual = FileHelper.get_extension_name(file_name)
    expected = ""
    assert actual == expected



def test_get_path_name():
    file_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\\utils\\test_FileHelper.py")
    actual = FileHelper.get_path_name(file_name)
    expected = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\\utils")
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
    source_file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\aa.txt")
    target_dir_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target\ABB")
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

    source_file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\aa.txt")
    middle_dir_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target\ABB")
    FileHelper.copy(source_file_full_name, middle_dir_full_name)
    middle_file_full_name = PathHelper.combine(middle_dir_full_name, "aa.txt")
    actual = os.path.isfile(middle_file_full_name)
    expected = True
    assert actual == expected

    random_string = RandomHelper.create()
    last_dir_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target")
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


"""
用于 load_line 回调使用的全局型变量
"""
file_content = ""


def test_load_line():
    file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\source\aa.txt")
    FileHelper.load_with_line(file_full_name, __line_callback)
    actual = file_content
    expected = "1. 第一行\n2. 第二行\n3. 第三行\n4. 第四行"
    assert actual == expected


def __line_callback(line_content):
    global file_content
    file_content = file_content + line_content


def test_store():
    new_content = RandomHelper.create(6, RandomEnum.AllLetters)
    file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(), r".test\_res\target\abcde.txt")
    FileHelper.store(file_full_name, new_content)
    file_all_content = FileHelper.load(file_full_name)

    actual = StringHelper.is_contains(file_all_content, new_content)
    expected = True
    assert actual == expected


def test_is_exist1():
    root_path = ProjectHelper.get_root_physical_path()

    file_full_name = PathHelper.combine(root_path, ".test/_res/_README.md")
    actual = FileHelper.is_exist(file_full_name)
    expected = True
    assert actual == expected


def test_is_exist2():
    root_path = ProjectHelper.get_root_physical_path()

    file_full_name = PathHelper.combine(root_path, ".test/_res/_fox-mail.md")
    actual = FileHelper.is_exist(file_full_name)
    expected = False
    assert actual == expected


def test_rename():
    root_path = ProjectHelper.get_root_physical_path()
    file_name_old = RandomHelper.create() + ".txt"
    file_full_name_old = PathHelper.combine(root_path, ".test\\_res\\", file_name_old)
    FileHelper.store(file_full_name_old, "123")
    file_name_new = RandomHelper.create() + ".txt"
    file_full_name_new = PathHelper.combine(root_path, ".test\\_res\\", file_name_new)
    FileHelper.rename(file_full_name_old, file_name_new)
    actual = FileHelper.is_exist(file_full_name_new)
    FileHelper.remove(file_full_name_new)
    expected = True
    assert actual == expected
pass

def test_get_image_type_name1():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testpng.png")
    actual = FileHelper.get_image_type_name(file_full_name)
    expected = "png"
    assert actual == expected
pass

def test_get_image_type_name2():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testjpg.jpg")
    actual = FileHelper.get_image_type_name(file_full_name)
    expected = "jpeg"
    assert actual == expected
pass

def test_is_image_type1():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testjpg.jpg")

    actual = FileHelper.is_image_type(file_full_name)
    expected = True
    assert actual == expected
pass


def test_is_image_type2():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testtxt.txt")

    actual = FileHelper.is_image_type(file_full_name)
    expected = False
    assert actual == expected
pass


def test_is_image_type3():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testpng.png")

    actual = FileHelper.is_image_type(file_full_name)
    expected = True
    assert actual == expected
pass


def test_is_image_type4():
    file_path = ProjectHelper.get_root_physical_path()
    file_full_name = PathHelper.combine(file_path,r".test\_res\images\testwebp.webp")

    actual = FileHelper.is_image_type(file_full_name)
    expected = True
    assert actual == expected
pass

# TODO:xiedali@20231029 应该加入对不存在文件的判断
# def test_is_image_type5():
#     file_path = ProjectHelper.get_root_physical_path()
#     file_full_name = PathHelper.combine(file_path,r".test\_res\images\nofile.no")
#
#     actual = FileHelper.is_image_type(file_full_name)
#     expected = True
#     assert actual == expected
# pass
