from _projectHelper import ProjectHelper as helper


class ProjectHelper:
    """
    向外暴露的接口
    通过调用项目根目录下的 _ProjectHelper.py 内的逻辑而实现
    """

    @staticmethod
    def get_root_physical_path():
        """
        获取项目的物理根目录
        :return:
        """
        return helper.get_root_physical_path()
