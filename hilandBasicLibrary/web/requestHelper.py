import requests
from bs4 import BeautifulSoup


class RequestHelper:
    """

    """

    @staticmethod
    def get_content(url, return_formatter='original', **kwargs):
        """

        :param url:
        :param return_formatter: 返回的数据格式为original（原始格式） 、soup（BeautifulSoup）
        :return:
        """
        params = None
        headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                   'Accept - Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                   'Connection': 'Keep-Alive',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
                   }

        if kwargs and "params" in kwargs:
            params = kwargs["params"]

        if kwargs and "headers" in kwargs:
            headers = kwargs["headers"]

        request_data = requests.get(url, params=params, headers=headers)  # Get方式获取网页数据
        request_content = request_data.content

        return_formatter = return_formatter.lower()

        if return_formatter == "soup" or return_formatter == "beautifulsoup":
            return BeautifulSoup(request_content, 'lxml')
        else:
            return request_content

    @classmethod
    def get_items(cls, url, selector, **kwargs):
        """
        获取页面中指定选择器的内容

        :param url: 获取数据信息的url地址
        :param selector: html格式的selector
        :return:返回值为符合选择器内容的Tag集合；
        """
        soup = cls.get_content(url, 'soup', **kwargs)
        content_set = soup.select(selector)

        return content_set

