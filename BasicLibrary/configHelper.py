import configparser
import os
import dotenv

from BasicLibrary.io.pathHelper import PathHelper
from BasicLibrary.projectHelper import ProjectHelper
from BasicLibrary.model.container import Container
from BasicLibrary.data.dictHelper import DictHelper


class ConfigHelper:
    """
    读取配置文件的逻辑，默认读取项目根目录下的 _projectConfig.ini 和 .env两个文件
    1、.env的优先级高于 _ProjectConfig.ini
    2、.env文件不得嵌入 vcs 中. 如果有 env 的样例或设置指导，请使用 .env.default文件，这个文件可以嵌入 vcs
    3、.ini文件是可以按照 section/node 的方式进行二级设置的，但.env只能设置一级。
        那么妥协的方式是将 .ini 文件中 section/node 按照 section.node的方式作为 .env 的 key 进行使用
    """

    @classmethod
    def get_section(cls, section_name):
        """
        获取 section 组
        :param section_name:
        :return:
        """
        config_ini_parser = cls.__build_ini_parser()
        section = config_ini_parser.options(section_name)
        return section

    @classmethod
    def get_item(cls, section_name, item_name, default_value=None):
        """
        获取 node 节点
        :param section_name:
        :param item_name:
        :param default_value:
        :return:
        """

        """
        1. 读取 _projectConfig.ini 文件
        """
        config_ini_parser = cls.__build_ini_parser()

        try:
            item_value = config_ini_parser.get(section_name, item_name)
        except:
            item_value = default_value

        """
        2. 读取环境文件.env 内的配置信息，优先级最高
        """
        config_env_parser = cls.__build_env_parser()

        if section_name:
            item_name = "{0}.{1}".format(section_name, item_name)

        item_value = DictHelper.get_value(config_env_parser, item_name, item_value)

        """
        转换数据类型为目标类型
        """
        if item_value is None:
            item_value = default_value
        else:
            if default_value is not None:
                item_type = type(default_value)
                item_value = item_type(item_value)
            pass
        pass

        return item_value

    @staticmethod
    def __build_ini_parser():
        config_ini_key = "__config_ini_parser__"
        config_ini_parser = Container.get_item(config_ini_key)

        if config_ini_parser is None:
            config_ini_parser = configparser.ConfigParser()
            root_path = ProjectHelper.get_root_physical_path()

            file = os.path.join(root_path, "_projectConfig.ini")
            config_ini_parser.read(file, encoding='utf-8')

            Container.set_item(config_ini_key, config_ini_parser)
        pass

        return config_ini_parser

    @staticmethod
    def __build_env_parser():
        env_parser_key = "__env_parser__"
        env_parser = Container.get_item(env_parser_key)

        if env_parser is None:
            root = ProjectHelper.get_root_physical_path()
            env_path = PathHelper.combine(root, '.env')
            env_parser = dotenv.dotenv_values(env_path)
            Container.set_item(env_parser_key, env_parser)
        pass

        return env_parser
