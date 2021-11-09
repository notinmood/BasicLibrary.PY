from builtins import *


class DictHelper:
    @staticmethod
    def is_contains_key(whole_dict, key_name):
        if key_name in whole_dict:
            return True
        else:
            return False
