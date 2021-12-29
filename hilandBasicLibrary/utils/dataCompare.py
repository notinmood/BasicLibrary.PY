"""
 * @file   : dataCompare.py
 * @time   : 17:03
 * @date   : 2021/12/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from hilandBasicLibrary.data.collectionHelper import CollectionHelper


class DataSummary:
    def __init__(self, target=None, target_length=0, target_type=None):
        """
        初始化的时候，提供target_data 或者提供其他data_xxx系列数据,二者选一
        :param target:
        :param target_length:
        :param target_type:
        """
        if target:
            self.length = len(target)
            self.type = type(target)
        else:
            self.length = target_length
            self.type = target_type

    def compare(self, comparing_data):
        if isinstance(comparing_data, DataSummary):
            if self.length != comparing_data.length:
                return False
            if self.type != comparing_data.type:
                return False

            return True
        else:
            return False


class DataCompare:
    @classmethod
    def compare_entity(cls, main_entity, secondary_entity):
        """
        比较实体数据(左侧视角)
        TODO:这个方法名需要重新命名一个清晰明了的名字
        :param dict main_entity:
        :param dict secondary_entity:
        :return:
        """
        no_matched = ""
        main_type = type(main_entity)

        for key in main_entity:
            if main_type is dict:
                is_matched = CollectionHelper.is_contains(secondary_entity, key, main_entity[key])
            else:
                is_matched = CollectionHelper.is_contains(secondary_entity, key)

            if not is_matched:
                if main_type is dict:
                    main_value = main_entity[key]
                    secondary_value = secondary_entity.get(key)
                    no_matched += "{0}|{1}|{2}||".format(key, main_value, secondary_value)
                else:
                    no_matched += "{0}||".format(key)

        return no_matched
