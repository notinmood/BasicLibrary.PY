"""
 * @file   : test_FileHelper.py
 * @time   : 13:13
 * @date   : 2023/6/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.fileShadowUsing import FileShadowUsing
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper


def test_shadow_generated_and_removed():
    root_path = ProjectHelper.get_root_physical_path()
    source_file_full_name = r'.test/_res/myContent.txt'
    source_file_full_name = PathHelper.combine(root_path, source_file_full_name)

    file_shadow_outer = ""
    with (FileShadowUsing(source_file_full_name)) as file_shadow:
        file_shadow_outer = file_shadow
        # 验证影子文件确实已经生成了
        actual = FileHelper.is_exist(file_shadow)
        expected = True
        assert actual == expected
    pass

    # 验证影子文件在使用完成后，就自动销毁了
    actual = FileHelper.is_exist(file_shadow_outer)
    expected = False
    assert actual == expected


pass


def test_func_name(*args):
    actual = True
    expected = True
    assert actual == expected


pass
