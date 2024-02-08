"""
 * @file   : test_DynamicImporter.py
 * @time   : 15:29
 * @date   : 2024/2/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

from BasicLibrary.environment.dynamicImporter import DynamicImporter


def test_load_class1():
    """
    动态加载类
    :return:
    """
    module_name = r'_res.student'
    class_name = 'Student'

    student_class = DynamicImporter.load_class(module_name, class_name)

    actual = student_class.get_language()
    expected = '中文'
    assert actual == expected


pass


def test_load_class2():
    """
    动态加载类
    :return:
    """
    module_name = r'_res.cat'
    class_name = 'Cat'

    student_class = DynamicImporter.load_class(module_name, class_name, "猫咪", 2)

    actual = student_class.about_me()
    expected = '我是猫咪，我2岁了'
    assert actual == expected


pass


def test_load_function():
    """
    动态加载函数
    :return:
    """
    module_name = r'_res.resUtils'
    function_name = 'hi_name'
    func = DynamicImporter.load_function(module_name, function_name)
    actual = func("张三")
    expected = "Hi, 张三!"
    assert actual == expected


pass
