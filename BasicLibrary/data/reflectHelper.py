"""
 * @file   : reflectHelper.py
 * @time   : 9:46
 * @date   : 2021/12/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import inspect


class ReflectHelper:
    """
    返回对本类型(或类型内方法)直接调用者的信息
    """

    @staticmethod
    def get_current_method_name():
        """
        获取当前运行的方法名称
        :return:
        """
        result = inspect.stack()[1].function
        if result == "<module>":
            return None
        else:
            return result
        pass

    pass

    @staticmethod
    def get_current_file_name():
        """
        获取当前运行的文件名称
        :return:
        """
        result = inspect.stack()[1].filename
        return result

    pass


pass
