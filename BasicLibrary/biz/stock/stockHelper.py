import re

from BasicLibrary.data.stringHelper import StringHelper


class StockHelper:
    @staticmethod
    def get_stock_exchange_name(stock_code):
        """
        获取股票交易所名称(SEN,Stock Exchange Name)
        :param stock_code:
        :return:
        """
        stock_code = StockHelper.get_standard_code(stock_code)
        exchange_name = "SZ"
        if stock_code.startswith("6"):
            exchange_name = "SH"

        if stock_code.startswith("9"):
            exchange_name = "SH"

        if stock_code.startswith("7"):
            exchange_name = "SH"

        return exchange_name

    @staticmethod
    def get_standard_code(stock_code):
        """
        获取6位数的标准股票代码
        :param stock_code:
        :return:
        """
        pattern = r"[0|3|6|7|8|9]\d{5}"
        matched = re.search(pattern, stock_code)
        if matched:
            return matched.group(0)
        else:
            return ""

    @staticmethod
    def format_stock_code(stock_code, prefix="[SEN]", postfix=""):
        """
        格式化股票代码信息
        :param stock_code:
        :param prefix:前缀信息(带[]或者不带[]).
                             []外的信息,固定不变;
                             []内的信息是会根据具体情况改变，其中
                             - 如果取SEN(StockExchangeName股票交易所名称),将会替换成SH(上海)或者SZ(深圳)
                             - 如果取sen(StockExchangeName股票交易所名称),将会替换成sh(上海)或者sz(深圳)
        :param postfix:后缀信息.(格式同$prefix)
        :return:
        """
        stock_code = StockHelper.get_standard_code(stock_code)
        if not stock_code:
            return ""
        else:
            standard_code = stock_code
            biz_code = "{}{}{}".format(prefix, standard_code, postfix)
            stock_exchange_name_upper = StockHelper.get_stock_exchange_name(standard_code)
            stock_exchange_name_lower = StringHelper.lower_all_chars(stock_exchange_name_upper)

            target = biz_code

            """
            明确指定的都转换为小写的交易所名称
            """
            target = re.sub(r"\[sen]", stock_exchange_name_lower, target)

            """
            添加其他替换过滤条件
            """

            """
            其他非明确指定的都换成大写交易所的名称
            """
            return re.sub(r"\[SEN]", stock_exchange_name_upper, target, 0, re.IGNORECASE)
