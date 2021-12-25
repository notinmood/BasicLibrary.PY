class RegexHelper:
    @staticmethod
    def get_patten_of_html_tag():
        """
        HTML标签的正则表达式模式
        :return:
        """
        patten = r"</?[^>]+>"
        return patten
