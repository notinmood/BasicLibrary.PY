from builtins import *


class DictHelper:
    @staticmethod
    def contain_key(whole_dict, key_name):
        if key_name in whole_dict:
            return True
        else:
            return False
