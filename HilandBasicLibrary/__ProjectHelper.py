import os

'''项目使用的时候，请将本文件复制到项目根目录下，由'__ProjectHelper.py' 改名为'_ProjectHelper.py' '''


def get_root_path():
    _rootPath = os.path.dirname(os.path.abspath(__file__))
    return _rootPath
