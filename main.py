# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
from shutil import rmtree

from HilandBasicLibrary.io.PathHelper import PathHelper
from HilandBasicLibrary.data.StringHelper import StringHelper
from _ProjectHelper import ProjectHelper


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pass
# print_hi('PyCharm')
# print(PathHelper.get_current_path())

# physical_root = ProjectHelper.get_root_physical_path()
# display_data = StringHelper.format("当前项目的根目录为：{0}", physical_root)
# print(display_data)
#
# target_dir = "dist"
# target_dir = PathHelper.combine(physical_root, target_dir)
# display_data = StringHelper.format("删除目录{0}下的所有内容", target_dir)
# print(display_data)
# rmtree(target_dir)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
