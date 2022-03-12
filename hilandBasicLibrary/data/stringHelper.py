import re


class StringHelper:
    @staticmethod
    def add_padding(original_content, patten, padding, prefix=True):
        """
        在匹配的字符前（或者后）方添加新的字符
        :param original_content:
        :param patten:正则表达式的模式字符串
        :param padding:待填充进去的字符串
        :param prefix:是在匹配的字符串前还是后添加字符（默认是True在前添加）
        :return:
        """
        if prefix is True:
            padding_format = r'{}\1'.format(padding)
        else:
            padding_format = r'\1{}'.format(padding)

        result = re.sub("({})".format(patten), padding_format, original_content)
        return result

    @staticmethod
    def get_before_content(whole, separator):
        """
        在指定的字符串中获取分隔符前面的内容
        :param whole:待分割的字符串
        :param separator:分隔符
        :return:分隔符前面的子字符串
        """
        pos = str.find(whole, separator)
        if pos >= 0:
            return whole[0:pos]
        else:
            return whole

    @staticmethod
    def get_after_content(whole, separator):
        pos = str.find(whole, separator)
        if pos >= 0:
            pos += len(separator)
            result = whole[pos:]
            return result
        else:
            return whole

    @staticmethod
    def get_length(data):
        return len(data)

    @staticmethod
    def set_padding(original, all_length, padding_char='0', pad_at_before=True):
        """
        用字符填充前(或者后)端位置，获取固定长度的字符串
        :param original:
        :param all_length:
        :param padding_char:
        :param pad_at_before:
        :return:
        """
        original = str(original)
        current_length = len(original)
        result = ""
        if current_length >= all_length:
            result = original
        else:
            char_count = all_length - current_length
            if pad_at_before is True:
                result = padding_char * char_count + original
            else:
                result = original + padding_char * char_count

        return result

    @staticmethod
    def remove_head(whole, head=" "):
        if StringHelper.is_start_with(whole, head):
            return whole[len(head):]
        else:
            return whole

    @staticmethod
    def remove_tail(whole, tail=" "):
        if StringHelper.is_end_with(whole, tail):
            return whole[:-len(tail)]
        else:
            return whole

    @staticmethod
    def is_end_with(whole, padding):
        return str.endswith(whole, padding)

    @staticmethod
    def is_start_with(whole, padding):
        return str.startswith(whole, padding)

    @staticmethod
    def is_contains(whole, padding):
        """

        :param whole:
        :param padding:
        :return:
        """
        result = whole.find(padding) >= 0
        return result

    @staticmethod
    def is_empty(data):
        """

        :param data:
        :return:
        """
        if data is None or data == "":
            return True
        else:
            return False

    @staticmethod
    def implode(collection_data, separator=','):
        """
        将集合类型的各个元素聚合成用分隔符分割的字符串
        :param collection_data: 集合类型，可以是set，list
        :param separator:
        :return:
        """
        return separator.join(collection_data)

    @staticmethod
    def explode(string_data, separator=","):
        """
        将字符串类型按照分隔符分割成list
        :param string_data:
        :param separator:
        :return:
        """
        return string_data.split(separator)

    @staticmethod
    def format(original_with_placeholder, *args, **kwargs):
        """
        对带有占位符的字符串进行格式化处理
        :param original_with_placeholder:带有占位符的字符串
        :param args:
        :param kwargs:
        :return:
        """
        return original_with_placeholder.format(*args, **kwargs)

    @staticmethod
    def upper_all_chars(original_string):
        """
        将给定内容中所有的字母大写表示
        :param original_string:
        :return:
        """
        return original_string.upper()

    @staticmethod
    def lower_all_chars(original_string):
        """
        将给定内容中所有的字母小写表示
        :param original_string:
        :return:
        """
        return original_string.lower()

    @staticmethod
    def upper_first_char(original_string):
        """
        将句子的第一个字母大写
        :param  original_string:
        :return:
        """
        return original_string[:1].upper() + original_string[1:]

    @staticmethod
    def lower_first_char(original_string):
        """
        将句子的第一个字母小写
        :param original_string:
        :return:
        """
        return original_string[:1].lower() + original_string[1:]

    @staticmethod
    def upper_first_char_every_word(original_string):
        """
        将每个单词的首字母大写
        :param original_string:
        :example:
            输入："programming is awesome"
            输出："Programming Is Awesome"
        :return:
        """
        return original_string.title()

    @staticmethod
    def replace(whole_string, old_sub_string, new_sub_string):
        """

        :param whole_string:
        :param old_sub_string:
        :param new_sub_string:
        :return:
        """
        return whole_string.replace(old_sub_string, new_sub_string)
