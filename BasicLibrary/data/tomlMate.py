"""
 * @file   : utils.py
 * @time   : 11:56
 * @date   : 2024/3/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

import tomlkit
from BasicLibrary.io.fileHelper import FileHelper
from tomlkit import TOMLDocument


class TomlMate(object):
    def __init__(self, toml_file_full_name):
        """
        初始化
        :param toml_file_full_name: toml文件的全路径文件名
        """
        self.toml_file_full_name = toml_file_full_name

        if not os.path.isfile(toml_file_full_name):
            FileHelper.create(toml_file_full_name)
        pass

        with open(toml_file_full_name, 'r', encoding="utf-8") as file:
            toml_doc = tomlkit.load(file)
        pass

        self.toml_doc: TOMLDocument = toml_doc

    def get(self, node_name_with_path: str, path_seperator="/"):
        """

        :param node_name_with_path:
        :param path_seperator:
        :return:
        """
        node_path_list = node_name_with_path.split(path_seperator)

        source = self.toml_doc
        for _item in node_path_list:
            result = source.get(_item)
            if result is None:
                return None
            else:
                source = result
            pass
        pass

        return source

    pass

    def set(self, node_name_with_path: str, node_value, path_seperator="/", auto_save=True):
        """

        :param node_name_with_path:
        :param node_value:
        :param path_seperator:
        :param auto_save:
        :return:
        """
        node_path_list = node_name_with_path.split(path_seperator)

        source = self.toml_doc
        parent = self.toml_doc

        for _item in node_path_list:
            result = source.get(_item)
            if result is None:
                # TODO:xiedali@2024/03/29 如果不存在就创建这节点
                ...
            else:
                parent = source
                source = result
            pass
        pass

        parent[node_path_list[-1]] = node_value

        if auto_save:
            self.save()
        pass

    pass

    def save(self):
        """

        :return:
        """
        with open(self.toml_file_full_name, "w", encoding="utf-8") as f:
            f.write(self.toml_doc.as_string())
        pass

    pass


pass
