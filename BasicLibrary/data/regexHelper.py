import re

from BasicLibrary import ObjectHelper


class RegexHelper:
    """

    """

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
        :example:
        text = '今天是：11/28/2018'
        actual = RegexHelper.replace(text, r"(\d{2})/(\d{2})/(\d{4})", r"\3年\1月\2日")
        expected = '今天是：2018年11月28日'
        assert actual == expected
        """
        regex = re.compile(pattern)
        return regex.sub(new_sub_string, whole)

    pass


pass
