"""
 * @file   : test_ExcelShadowUsing.py
 * @time   : 11:08
 * @date   : 2023/6/16
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.io.fileHelper import FileHelper
from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.office.excelShadowUsing import ExcelShadowUsing
from BasicLibrary.projectHelper import ProjectHelper


def test_shadow_generated_and_removed():
    root_path = ProjectHelper.get_root_physical_path()
    source_file_full_name = r'.test/_res/source/myExcel.xlsx'
    source_file_full_name = PathHelper.combine(root_path, source_file_full_name)

    file_shadow_outer = None
    with (ExcelShadowUsing(source_file_full_name)) as excel_shadow:
        file_shadow_outer = excel_shadow.filename
        # 验证影子文件确实已经生成了
        actual = FileHelper.is_exist(file_shadow_outer)
        expected = True
        assert actual == expected
    pass

    # 验证影子文件在使用完成后，就自动销毁了
    actual = FileHelper.is_exist(file_shadow_outer)
    expected = False
    assert actual == expected


pass
