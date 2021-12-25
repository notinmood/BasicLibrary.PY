import configparser
import os
import dotenv

from hilandBasicLibrary.projectHelper import ProjectHelper as ph

from hilandBasicLibrary.data.dictHelper import DictHelper


class ConfigHelper:
    """
    读取配置文件的逻辑，默认读取项目根目录下的 _projectConfig.ini 和 .env两个文件
    1、.env的优先级高于_ProjectConfig.ini
    2、.env文件不得嵌入vcs中. 如果有env的样例或设置指导，请使用 .env.default文件，这个文件可以嵌入vcs
    3、.ini文件是可以按照 section/node的方式进行二级设置的，但.env只能设置一级。
        那么妥协的方式是将.ini文件中section/node按照 section.node的方式作为.env的key进行使用
    """
    @staticmethod
    def __build_parser():
        cp = configparser.ConfigParser()
        root_path = ph.get_root_physical_path()

        file = os.path.join(root_path, "_projectConfig.ini")
        cp.read(file, encoding='utf-8')

        return cp

    @classmethod
    def get_section(cls, section_name):
        cp = cls.__build_parser()
        section = cp.options(section_name)
        return section

    @classmethod
    def get_item(cls, section_name, item_name, default_value=None):
        cp = cls.__build_parser()

        try:
            item_value = cp.get(section_name, item_name)
        except:
            item_value = default_value

        if item_value is None:
            item_value = default_value
        else:
            if default_value is not None:
                item_type = type(default_value)
                item_value = item_type(item_value)

        """
        环境文件.env 内的配置信息，优先级最高
        """
        env_dict = dotenv.dotenv_values()

        if section_name:
            item_name = "{0}.{1}".format(section_name, item_name)

        item_value = DictHelper.get_value(env_dict, item_name, item_value)

        return item_value
