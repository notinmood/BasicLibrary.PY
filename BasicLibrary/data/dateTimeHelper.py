import re
from datetime import datetime, timedelta, date


# +--------------------------------------------------------------------------
# |::说明：| Python内置两个方法的说明
# |·······|     strptime()方法,里面的p是parse的意思，就是把字符串解析成日期时间类型
# |·······|     strftime()方法,里面的f是format的意思，就是把日期时间类型格式化为某种格式的字符串
# +--------------------------------------------------------------------------

class DateTimeHelper:
    @staticmethod
    def convert_from_string(date_time_string, formatter=""):
        """
        从字符串转换为日期时间
        :param date_time_string:
        :param formatter: 待解析字符串中包含的日期时间格式，如果为""时候系统自动推断(仅限常见的格式可以推断)
        :return:
        """
        if formatter == "":
            formatter = DateTimeHelper.get_format(date_time_string)

        _type = type(date_time_string)
        if _type is str:
            return datetime.strptime(date_time_string, formatter)
        else:
            if _type is datetime:
                return date_time_string
            else:
                return None

    @staticmethod
    def convert_from_compact_string(date_time_string):
        """
        将类似“20210221”的字符串，转化成日期数据（在股市交易中常用）
        :param date_time_string:
        :return:
        """
        return DateTimeHelper.convert_from_string(date_time_string, "%Y%m%d")

    @staticmethod
    def get_compact_string(date_time_value=None):
        """
        获取“20210221”这种类型的日期字符串（在股市交易中常用）
        :param date_time_value:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, "%Y%m%d")

    @staticmethod
    def get_short_string(date_time_value=None, formatter="%Y-%m-%d"):
        """
        获取“2021-02-21”这种短类型格式的日期字符串
        :param date_time_value:
        :param formatter:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, formatter)

    @staticmethod
    def get_standard_string(date_time_value=None):
        """
        获取给定时间的标准格式日期字符串表示形式(类似2021-10-11 03:34:25)
        :param date_time_value:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_string(date_time_value=None, formatter="%Y-%m-%d %H:%M:%S"):
        """
        获取给定时间的字符串表示形式（默认情况下返回当前的时间数据）
        :param formatter:
        :param date_time_value: 需要展示的日期时间数据，默认不传递此参数则返回当前时间数据
        :return: 给定时间的字符串表示形式
        """
        if date_time_value is None:
            date_time_value = datetime.now()

        result = date_time_value.strftime(formatter)
        return result

    @staticmethod
    def add_days(original_date=None, delta=1, original_date_formatter="%Y%m%d"):
        """

        :param original_date: 可以是日期类型，也可以是字符串类型
        :param delta: 增加或者减少的天数
        :param original_date_formatter: 日期格式。如果是字符串类型的original_date，那么需要指定本参数
        :return:
        """
        _delta = timedelta(days=delta)
        if original_date is None:
            original_date = datetime.now()

        if type(original_date) is str:
            original_date = DateTimeHelper.convert_from_string(original_date, original_date_formatter)

        _type = type(original_date)
        if _type is datetime or _type is date:
            return original_date + _delta
        else:
            return None

    @staticmethod
    def get_format(datetime_string):
        """
        从字符串推断日期时间格式
        :param datetime_string:
        :return:
        """
        regex = r'(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})'
        if re.search(regex, datetime_string):
            return "%Y-%m-%d %H:%M:%S"

        regex = r'(\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})'
        if re.search(regex, datetime_string):
            return "%y-%m-%d %H:%M:%S"

        regex = r'(\d{4}\d{1,2}\d{1,2}\d{1,2}\d{1,2}\d{1,2})'
        if re.search(regex, datetime_string):
            return "%Y%m%d%H%M%S"

        regex = r'(\d{4}-\d{1,2}-\d{1,2})'
        if re.search(regex, datetime_string):
            return "%Y-%m-%d"

        regex = r'(\d{4}\d{2}\d{2})'
        if re.search(regex, datetime_string):
            return "%Y%m%d"

        regex = r'(\d{2}\d{2}\d{2})'
        if re.search(regex, datetime_string):
            return "%y%m%d"

        return ""
