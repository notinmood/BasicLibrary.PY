"""
 * @file   : unitTest.py
 * @time   : 16:57
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.dataBase.databaseMisc import DatabaseMisc


class UnitTest:
    def __init__(self, table_name):
        self._new_table_name = table_name + "__my_dupl"
        DatabaseMisc.duplicate_table(table_name, self._new_table_name, -1)

    def __del__(self):
        DatabaseMisc.drop_table(self._new_table_name)

