class StringHelper:
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
