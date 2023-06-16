"""
 * @file   : usingCopiedExcel.py
 * @time   : 10:32
 * @date   : 2022/3/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.io.fileShadowUsing import FileShadowUsing
from BasicLibrary.office.excelBookMate import ExcelBookMate


class ExcelShadowUsing(FileShadowUsing):
    """
    在 with *** as ***： 语句内使用，as 后返回的是一个 ExcelBookMate 对象
    """

    def __init__(self, excel_file_full_name):
        super().__init__(excel_file_full_name)
        self.excel = ExcelBookMate(super().file_shadow_full_name)

    def __enter__(self):
        return self.excel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.excel.close()
        super().__exit__(exc_type, exc_val, exc_tb)
