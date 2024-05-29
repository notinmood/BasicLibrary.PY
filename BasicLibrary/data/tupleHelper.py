"""
 * @file   : tupleHelper.py
 * @time   : 下午10:58
 * @date   : 2024/5/29
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.collectionHelper import CollectionHelper
from BasicLibrary.data.stringHelper import StringHelper


class TupleHelper:
    @staticmethod
    def recognize_tuple(collection_value: str | list[str] | tuple[str, ...]):
        """
        将给定的字符串或列表转换为元组
        如果给定的参数是字符串，则会先用逗号分隔符分割字符串，然后再转换为元组
        如果给定的参数是列表，则直接转换为元组
        如果给定的参数是元组，则直接返回元组
        :param collection_value:
        :return:
        """
        return CollectionHelper.format(collection_value, tuple)

    pass


pass
