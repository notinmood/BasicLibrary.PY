import os
from builtins import *


def get_illegal_chars_in_file_system(include_seperator=True):
    """
    文件系统（文件目录或文件名称）内不使用的字符
    :param include_seperator: 是否包含目录分割符号 "\\" 和 "/"
    :return:
    """
    normal = ["?", "*", '"', ":", "<", ">", "|"]
    if include_seperator:
        normal.append("\\")
        normal.append("/")

    return normal


def get_safe_filename(filename, safe_char="_", include_seperator=True):
    chars = get_illegal_chars_in_file_system(include_seperator)
    for c in chars:
        filename = filename.replace(c, safe_char)

    return filename


def get_files(dir_path, include_sub_dir=True):
    """
    获取某目录下的文件名称
    :param dir_path:
    :param include_sub_dir: 是否包含子目录（缺省是True，包含）
    :return:
    """
    result = []
    __list_dir(dir_path, result, include_sub_dir)
    return result


def __list_dir(path, list_name, include_sub_dir=True):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            if include_sub_dir is True:
                __list_dir(file_path, list_name)
        else:
            list_name.append(file_path)


def get_file_short_name(file_full_name):
    filepath, filename = os.path.split(file_full_name)
    return filename


def get_file_ext_name(file_full_name):
    a, extension = os.path.splitext(file_full_name)
    return extension


def get_file_path_name(file_full_name):
    filepath, filename = os.path.split(file_full_name)
    return filepath


def ensure_path(path_name):
    """
    取保目录存在，如果不存在就创建
    :param path_name:
    :return:
    """
    if os.path.exists(path_name) is False:
        os.makedirs(path_name)


def load_file(file_full_name):
    with open(file_full_name, "r", encoding='utf-8') as file_pointer:
        data = file_pointer.read()
    return data


def load_file_with_lines(file_full_name):
    """
    按照行的方式读取文件，返回行信息的list
    :param file_full_name:
    :return: 行信息的list
    """
    with open(file_full_name, "r", encoding='utf-8') as file_pointer:
        data = file_pointer.readlines()
    return data


def load_file_with_line(file_full_name, line_callback):
    """
    按行读取文件，每读取一行进行一次处理（调用line_callback）,对大文件尤其有效
    :param file_full_name:
    :param line_callback: 在每行上进行回调的函数
    :return:
    """
    with open(file_full_name, "r", encoding='utf-8') as file_pointer:
        while True:
            line = file_pointer.readline()
            if line:
                line_callback(line)
            else:
                break


def store_file(file_full_name, content, is_append=True):
    """
    保存文件在磁盘中
    :param file_full_name:待保存文件的全路径名称
    :param content:待保存内容
    :param is_append: 新内容如是附加在原内容的后面，还是替代掉原内容（默认是附加在原内容后面）
    :return:
    """
    path_name = get_file_path_name(file_full_name)
    ensure_path(path_name)
    if is_append:
        mode = 'a+'
    else:
        mode = 'w+'

    with open(file_full_name, mode, encoding='utf-8') as file_pointer:
        file_pointer.write(content)


if __name__ == '__main__':
    _tt = get_illegal_chars_in_file_system()
    print(_tt)

    _filename = "我是一:个好|人吗?"
    _filename = get_safe_filename(_filename)
    print(_filename)
