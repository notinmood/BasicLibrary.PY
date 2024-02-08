"""
 * @file   : dynamicImporter.py
 * @time   : 15:21
 * @date   : 2024/2/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import importlib


class DynamicImporter:
    """
    动态导入模块
    """

    # +--------------------------------------------------------------------------
    # |::::TIPS::::| 本代码的使用说明
    # ---------------------------------------------------------------------------
    # 暂时用不到动态导入
    # +--------------------------------------------------------------------------

    @staticmethod
    def load_class(module_name: str, class_name: str, *args, **kwargs):
        """
        动态导入类（构建类型实例的时候如果需要初始化参数，请通过*args和**kwargs传入）
        :param module_name:可以是使用句号分割路径的模块名称，但不带.py后缀
        :param class_name:要动态加载的类型名称
        :return:
        """
        module = importlib.import_module(module_name)
        the_class = getattr(module, class_name)
        return the_class(*args, **kwargs)

    pass

    @staticmethod
    def load_function(module_name: str, function_name: str):
        """
        动态导入函数（本方法仅负责导入函数，具体调用请在客户程序中进行）
        注意：本方法仅负责导入直接保存在模块中的函数，不是类型中的方法；
        类型中的方法需要通过load_class方法导入类型，然后在类型实例上调用方法
        :param module_name:可以是使用句号分割路径的模块名称，但不带.py后缀
        :param function_name:要动态加载的函数名称
        :return:
        """
        module = importlib.import_module(module_name)
        return getattr(module, function_name)

    pass
