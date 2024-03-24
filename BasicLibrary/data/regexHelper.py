import re

from BasicLibrary import ObjectHelper


class RegexHelper:
    """
    正则表达式帮助类
    """

    @staticmethod
    def get_all_meta_chars():
        """
        正则表达式所有的元字符
        如果要使用数组形式的元字符串，可以list(get_all_meta_chars())
        :return:
        """
        # All_Meta_Chars = ["*", "+", "?", "$", "^", ".", "|", "\\", "(", ")", "{", "}", "[", "]"]
        return r"\^$*+?.()[]{}|"

    pass

    @classmethod
    def keep_prototypical(cls, some_string: str):
        """
        保留正则表达式的原义（即把正则表达式的各个元字符当做普通字符数使用）
        :param some_string:
        :return:
        """

        # 以下代码r"\\\1"中，前两个\\表示“\”,最后一个\是跟1在一起的，表示“\1”，即捕获匹配后的第一个分组。
        # 以下是为了消除ide的警告而做的PolyFill
        # noinspection all
        return re.sub(r"([\^\$\.\*\+\?\(\)\|\[\]\{\}\\])", r"\\\1", some_string)

    pass

    @staticmethod
    def get_patten_of_html_tag():
        """
        HTML标签的正则表达式模式
        :return:
        """
        patten = r"</?[^>]+>"
        return patten

    pass

    @classmethod
    def get_items(cls, whole, pattern):
        """
        获取匹配成功的结果数组(方法 `get_matched_items` 的别名)
        :param whole:
        :param pattern:
        :return:
        """
        return cls.get_matched_items(whole, pattern)

    pass

    @staticmethod
    def get_matched_items(whole, pattern):
        """
        获取匹配成功的结果数组
        :param str whole :
        :param str pattern :
        :return list<str>: 字符串数组（没有任何匹配成功的信息，返回空数组。）
        """
        regex = re.compile(pattern)
        return regex.findall(whole)

    pass

    @classmethod
    def determine_is_matched(cls, whole, pattern):
        """
        判断是否匹配成功
        :param str whole:
        :param str pattern:
        :return:
        """
        matched = cls.get_matched_items(whole, pattern)
        return ObjectHelper.is_exist(matched)

    pass

    @staticmethod
    def replace(whole, pattern, new_sub_string):
        """
        字符串替换
        :param str whole:
        :param str pattern:要匹配的模式
        :param str new_sub_string:新字符串（可以带由 pattern 形成的分组号，分组号用 \1 \2 这的格式表示）
        :return str:替换后的新字符串
        """
        # :example:
        # text = '今天是：11/28/2018'
        # actual = RegexHelper.replace(text, r"(\d{2})/(\d{2})/(\d{4})", r"\3年\1月\2日")
        # expected = '今天是：2018年11月28日'
        # assert actual == expected

        regex = re.compile(pattern)
        return regex.sub(new_sub_string, whole)

    pass


pass
