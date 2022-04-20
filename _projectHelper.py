import os

"""
项目使用的时候，请将本文件复制到项目根目录下，由'__projectHelper.py' 改名为'_projectHelper.py'
"""


class ProjectHelper:
    """

    """
    @staticmethod
    def get_root_physical_path():
        _rootPath = os.path.dirname(os.path.abspath(__file__))
        return _rootPath
