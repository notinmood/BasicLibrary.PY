import re

from BasicLibrary.data.regexHelper import RegexHelper


class StringHelper:
    """

    """

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
    def reverse(original):
        """
        翻转字符串
        :param original:
        :return:
        """
        return original[::-1]

    @staticmethod
    def is_end_with(whole, sub_string):
        return str.endswith(whole, sub_string)

    @staticmethod
    def is_start_with(whole, sub_string):
        return str.startswith(whole, sub_string)

    @staticmethod
    def is_contains(whole, sub_string):
        """

        :param whole:
        :param sub_string:
        :return:
        """
        result = whole.find(sub_string) >= 0
        return result

    @staticmethod
    def is_empty(data):
        """
        判断字符串是否为空
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
        对带有占位符的字符串进行格式化处理，其中占位符用 {0}、{1}等来表示
        :param original_with_placeholder:带有占位符的字符串（其中占位符用 {0}、{1}等来表示）
        :param args:
        :param kwargs:
        :return:
        :example:

        name = "小明"
        height = 175

        print("────────────────────────PY系统的缺省方法────────────────────────")
        print(f"{name}的身高是{height}cm")

        print("────────────────────────使用 DIY方法1────────────────────────")
        whole = StringHelper.format("{name}的身高是{height}", name=name, height=height)
        print(whole)

        print("────────────────────────使用 DIY方法2────────────────────────")
        whole = StringHelper.format("{0}的身高是{1}", name, height)
        print(whole)
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
        字符串替换
        :param whole_string:
        :param old_sub_string:被替换掉的字符串或者是正则表达式
        :param new_sub_string:新字符串（可以带由 pattern 形成的分组号，分组号用 \1 \2 这的格式表示）
        :return:替换后的新字符串
        :example:
        text = '今天是：11/28/2018'
        actual = StringHelper.replace(text, r"(\d{2})/(\d{2})/(\d{4})", r"\3年\1月\2日")
        expected = '今天是：2018年11月28日'
        assert actual == expected
        """
        # return whole_string.replace(old_sub_string, new_sub_string)
        return RegexHelper.replace(whole_string, old_sub_string, new_sub_string)

    @staticmethod
    def sub_string(whole_string, start_position=0, length=0):
        """
        截取字符串
        :param whole_string:
        :param start_position:开始位置（如果是负数就从右往左取，但最右侧一个永远取不到，因为最右侧一个的数的index是-1）
        :param length:截取长度（如果start_position为正数，就表示从左往右取多少个；如果start_position为负数，就表示从右往左取多少个）
        :return:
        """
        all_length = len(whole_string)

        if start_position < 0:
            end_position = start_position - length
            if abs(end_position) > all_length + 1:
                end_position = 0 - all_length
            pass
            return whole_string[end_position:start_position]
        else:
            end_position = start_position + length
            if end_position > all_length:
                end_position = all_length
            pass
            return whole_string[start_position: end_position]
        pass

    pass
