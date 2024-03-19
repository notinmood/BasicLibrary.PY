"""
 * @file   : **.py
 * @time   : 16:26
 * @date   : 2021/11/8
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import re

from BasicLibrary import ObjectHelper
from BasicLibrary.data.listHelper import ListHelper
from BasicLibrary.data.regexHelper import RegexHelper


class StringHelper:
    """
    字符串处理工具类
    """

    @staticmethod
    def add_padding(original, all_length, padding_char='0', pad_at_before=True):
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
            pass
        pass

        return result

    pass

    @staticmethod
    def insert_fixer(original_content, patten, padding, prefix=True):
        """
        在给定的字符串中匹配符号模式的字符，在匹配到的字符前（或者后）方添加新的字符缀
        :param original_content:
        :param patten:正则表达式的模式字符串
        :param padding:待填充进去的字符串
        :param prefix:是在匹配的字符串前还是后添加字符（默认是True在前添加）
        :return:
        """
        if prefix is True:
            padding_format = rf'{padding}\1'
        else:
            padding_format = rf'\1{padding}'
        pass

        result = re.sub(f"({patten})", padding_format, original_content)
        return result

    pass

    # TODO:xiedali@2024/03/11 需要为add_seperator添加单元测试
    @staticmethod
    def add_seperator(whole: str, seperator='\n', every=14):
        """
        在指定的字符串中每隔every个字符添加分隔符
        :param whole:
        :param seperator:
        :param every:
        :return:
        """
        return seperator.join(whole[i:i + every] for i in range(0, len(whole), every))

    pass

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
        pass

        return whole

    pass

    @staticmethod
    def get_after_content(whole, separator):
        """
        在指定的字符串中获取分隔符后面的内容
        :param whole:
        :param separator:
        :return:
        """
        pos = str.find(whole, separator)
        if pos >= 0:
            pos += len(separator)
            result = whole[pos:]
            return result
        pass

        return whole

    pass

    @staticmethod
    def get_length(data):
        """
        获取数据的长度
        :param data:
        :return:
        """
        return len(data)

    pass

    @staticmethod
    def remove_head(whole, head=" "):
        """
        移除字符串头部指定的字符，如果字符串头部不是指定的字符，则返回原字符串
        :param whole:
        :param head:
        :return:
        """
        if StringHelper.is_start_with(whole, head):
            return whole[len(head):]
        pass

        return whole

    pass

    @staticmethod
    def remove_tail(whole, tail=" "):
        """
        移除字符串尾部指定的字符，如果字符串尾部不是指定的字符，则返回原字符串
        :param whole:
        :param tail:
        :return:
        """
        if StringHelper.is_end_with(whole, tail):
            return whole[:-len(tail)]
        pass

        return whole

    pass

    @staticmethod
    def reverse(original):
        """
        翻转字符串
        :param original:
        :return:
        """
        return original[::-1]

    pass

    @staticmethod
    def is_end_with(whole, sub_string):
        """
        判断字符串是否以指定的子字符串结尾
        :param whole:
        :param sub_string:
        :return:
        """
        return str.endswith(whole, sub_string)

    pass

    @staticmethod
    def is_start_with(whole, sub_string):
        """
        判断字符串是否以指定的子字符串开头
        :param whole:
        :param sub_string:
        :return:
        """
        return str.startswith(whole, sub_string)

    pass

    @staticmethod
    def is_contains(whole, sub_string):
        """
        判断字符串是否包含指定的子字符串
        :param whole:
        :param sub_string:
        :return:
        """
        result = whole.find(sub_string) >= 0
        return result

    pass

    @staticmethod
    def is_empty(data):
        """
        判断字符串是否为空
        :param data:
        :return:
        """
        # if data is None or data == "":
        #     return True
        # else:
        #     return False
        # pass
        return not data

    pass

    @staticmethod
    def implode(collection_data, separator=',') -> str:
        """
        将集合类型的各个元素聚合成用分隔符分割的字符串
        :param collection_data: 集合类型，可以是set，list
        :param separator:
        :return:
        """
        return separator.join(collection_data)

    pass

    @staticmethod
    def explode(string_data: str, separators: str | list[str] = ",") -> list:
        """
        将字符串类型按照分隔符分割成list
        :param string_data:
        :param separators:
        :return:
        """
        if ObjectHelper.get_type(separators) is str:
            separators = [separators]
        pass

        if len(separators) < 1:
            return [string_data]
        pass

        result = string_data.split(separators[0])
        for _index, delimiter in enumerate(separators):
            if _index > 0:
                for result_item in result:
                    temp = result_item.split(delimiter)
                    if len(temp) > 1:
                        result.remove(result_item)
                        result = ListHelper.merge(result, temp)
                    pass
                pass
            pass
        pass

        return result

        # return string_data.split(separators)

    pass

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

    pass

    @staticmethod
    def upper_all_chars(original_string):
        """
        将给定内容中所有的字母大写表示
        :param original_string:
        :return:
        """
        return original_string.upper()

    pass

    @staticmethod
    def lower_all_chars(original_string):
        """
        将给定内容中所有的字母小写表示
        :param original_string:
        :return:
        """
        return original_string.lower()

    pass

    @staticmethod
    def upper_first_char(original_string):
        """
        将句子的第一个字母大写
        :param  original_string:
        :return:
        """
        return original_string[:1].upper() + original_string[1:]

    pass

    @staticmethod
    def lower_first_char(original_string):
        """
        将句子的第一个字母小写
        :param original_string:
        :return:
        """
        return original_string[:1].lower() + original_string[1:]

    pass

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

    pass

    @staticmethod
    def replace(whole_string: str, old_sub_string: str, new_sub_string: str, use_regex_mode=True) -> str:
        """
        字符串替换
        :param use_regex_mode: 使用正则表达式模式
        :param whole_string:
        :param old_sub_string:被替换掉的字符串或者是正则表达式
        :param new_sub_string:新字符串（可以带由 pattern 形成的分组号，分组号用 \1 \2 这样的格式表示（正则表达式中分组号是从1开始的，不是0））
        :return:替换后的新字符串
        :example:
        text = '今天是：11/28/2018'
        actual = StringHelper.replace(text, r"(\\d{2})/(\\d{2})/(\\d{4})", r"\3年\1月\2日")
        expected = '今天是：2018年11月28日'
        assert actual == expected
        """
        if use_regex_mode:
            return RegexHelper.replace(whole_string, old_sub_string, new_sub_string)
        pass

        return whole_string.replace(old_sub_string, new_sub_string)

    pass

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
        pass

        end_position = start_position + length
        end_position = min(end_position, all_length)
        return whole_string[start_position: end_position]

    pass
