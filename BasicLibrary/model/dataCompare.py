"""
 * @file   : dataCompare.py
 * @time   : 17:03
 * @date   : 2021/12/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.collectionHelper import CollectionHelper


class DataSummary:
    """

    """

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
        pass

    def compare(self, comparing_data):
        if isinstance(comparing_data, DataSummary):
            if self.length != comparing_data.length:
                return False
            pass

            if self.type != comparing_data.type:
                return False
            pass

            return True
        else:
            return False
        pass


class DataCompare:
    @classmethod
    def compare_entity_single(cls, main_entity, secondary_entity):
        """
        单向比较实体数据
        (从main_entity内遍历每个item,去secondary_entity内匹配，是否存在及相同;
        而不关注 secondary_entity 内含有的item是否在 main_entity 内存在.)
        :param any main_entity:
        :param any secondary_entity:
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
