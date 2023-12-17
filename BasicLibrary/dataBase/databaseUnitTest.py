"""
 * @file   : databaseUnitTest.py
 * @time   : 16:57
 * @date   : 2021/12/27
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.dataBase.databaseClient import DatabaseClient


class DatabaseUnitTest:
    """

    """

    def __init__(self, table_name, duplicate_row_count=-1, auto_dispose=True):
        """

        :param table_name:
        :param duplicate_row_count:
        :param auto_dispose: 是否自动销毁创建的各种资源
        """
        self.auto_dispose = auto_dispose
        self.new_table_name = table_name + "__my_dupl__"
        self.mate = DatabaseClient.get_mate(self.new_table_name)
        self.ddl = DatabaseClient.get_ddl()

        self.ddl.duplicate_table(table_name, self.new_table_name, duplicate_row_count)

    def __del__(self):
        """
        在析构函数里面，销毁创建的各种资源
        :return:
        """
        if self.auto_dispose:
            self.dispose()
        pass

    pass

    def dispose(self):
        """
        销毁创建的各种资源
        :return:
        """
        self.ddl.drop_table(self.new_table_name)

    pass


pass
