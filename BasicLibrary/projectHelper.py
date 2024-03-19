"""
 * @file   : projectHelper.py
 * @time   : 19:59
 * @date   : 2022/3/11
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from _projectHelper import ProjectHelper as PH


class ProjectHelper:
    """
    向外暴露的接口
    通过调用项目根目录下的 _projectHelper.py 文件内的逻辑而实现
    （所以在每个项目建立的时候，都要将“__projectHelper.py”复制到项目的根目录下，并改名“_projectHelper.py”）
    """

    @staticmethod
    def get_root_physical_path():
        """
        获取项目的物理根目录
        :return:
        """
        return PH.get_root_physical_path()
