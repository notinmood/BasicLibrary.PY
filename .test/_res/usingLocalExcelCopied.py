"""
 * @file   : usingCopiedExcel.py
 * @time   : 10:32
 * @date   : 2022/3/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.office.excelShadowUsing import ExcelShadowUsing
from BasicLibrary.projectHelper import ProjectHelper


class UsingLocalExcelCopied(ExcelShadowUsing):
    """
    辅助验证Excel操作功能的，具体的Excel文件的影子
    """

    def __init__(self):
        source_file_full_name = PathHelper.combine(ProjectHelper.get_root_physical_path(),
                                                   r".test\_res\source\myExcel.xlsx")
        super().__init__(source_file_full_name)

    pass


pass
