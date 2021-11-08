import configparser
import os
from builtins import *

from hiland import ProjectHelper as ph


def build_parser():
    cp = configparser.ConfigParser()
    root_path = ph.get_project_root_path()

    file = os.path.join(root_path, "_ProjectConfig.ini")
    cp.read(file, encoding='utf-8')

    return cp


def get_config_section(section_name):
    cp = build_parser()
    section = cp.options(section_name)
    return section


def get_config_item(section_name, item_name, default_value=None):
    cp = build_parser()
    item_value = cp.get(section_name, item_name)
    if item_value is None:
        item_value = default_value
    else:
        if default_value is not None:
            item_type = type(default_value)
            item_value = item_type(item_value)

    return item_value


if __name__ == '__main__':
    _section = get_config_section("db_mongodb")
    print(type(_section))
    print(_section)

    item = get_config_item("db_mongodb", "host")
    print(item)

    item = get_config_item("project_data", "console_information_display_level", 8)
    print(type(item))
    print(item)
