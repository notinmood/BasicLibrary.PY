from hilandBasicLibrary.model.dataCompare import DataSummary


class DictHelper:
    @staticmethod
    def is_contains_key(whole_dict, key_name):
        if key_name in whole_dict:
            return True
        else:
            return False

    @classmethod
    def get_value(cls, whole_dict, key_name, default_value=None):
        if cls.is_contains_key(whole_dict, key_name):
            return whole_dict[key_name]
        else:
            return default_value

    @classmethod
    def is_contains_value(cls, whole_dict, value):
        for key in whole_dict:
            if whole_dict[key] == value:
                return True

        return False

    @classmethod
    def get_summary(cls, dict_data):
        summary = DataSummary(dict_data)
        return summary
