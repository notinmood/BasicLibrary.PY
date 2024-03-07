import re
import time
from datetime import datetime, timedelta, date
import sxtwl
from BasicLibrary import ObjectHelper
from BasicLibrary.data.chineseData import ChineseData
from BasicLibrary.data.stringHelper import StringHelper


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
        pass

        _type = type(date_time_string)
        if _type is str:
            return datetime.strptime(date_time_string, formatter)
        pass

        if _type is datetime:
            return date_time_string
        else:
            return None
        pass

    pass

    @staticmethod
    def convert_from_compact_string(date_time_string):
        """
        将类似“20210221”的字符串，转化成日期数据（在股市交易中常用）
        :param date_time_string:
        :return:
        """
        return DateTimeHelper.convert_from_string(date_time_string, "%Y%m%d")

    pass

    @staticmethod
    def get_compact_string(date_time_value=None):
        """
        获取“20210221”这种类型的日期字符串（在股市交易中常用）;跟get_compact_date_string功能一样
        :param date_time_value:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, "%Y%m%d")

    pass

    @classmethod
    def get_compact_date_string(cls, date_time_value=None):
        """
        获取“20210221”这种类型的日期字符串（在股市交易中常用）;get_compact_string的别名
        :param date_time_value:
        :return:
        """
        return cls.get_compact_string(date_time_value)

    pass

    @classmethod
    def get_compact_date_time_string(cls, date_time_value=None):
        """
        获取“20210221030526”这种类型的日期时间字符串
        :param date_time_value:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, "%Y%m%d%H%M%S")

    pass

    @staticmethod
    def get_short_string(date_time_value=None, formatter="%Y-%m-%d"):
        """
        获取“2021-02-21”这种短类型格式的日期字符串
        :param date_time_value:
        :param formatter:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, formatter)

    pass

    @staticmethod
    def get_standard_string(date_time_value=None):
        """
        获取给定时间的标准格式日期字符串表示形式(类似2021-10-11 03:34:25)
        :param date_time_value:
        :return:
        """
        return DateTimeHelper.get_string(date_time_value, "%Y-%m-%d %H:%M:%S")

    pass

    @classmethod
    def get_string(cls, date_time_value=None, formatter="%Y-%m-%d %H:%M:%S"):
        """
        获取给定时间的字符串表示形式（默认情况下返回当前的时间数据）
        :param formatter:
        :param date_time_value: 需要展示的日期时间数据，默认不传递此参数则返回当前时间数据
        :return: 给定时间的字符串表示形式
        """
        if date_time_value is None:
            date_time_value = datetime.now()
        pass

        if ObjectHelper.get_type(date_time_value) is str:
            date_time_value = cls.convert_from_string(date_time_value)
        pass

        return date_time_value.strftime(formatter)

    pass

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
        pass

        if type(original_date) is str:
            original_date = DateTimeHelper.convert_from_string(original_date, original_date_formatter)
        pass

        _type = type(original_date)
        if _type is datetime or _type is date:
            return original_date + _delta
        else:
            return None
        pass

    pass

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
        pass

        regex = r'(\d{2}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})'
        if re.search(regex, datetime_string):
            return "%y-%m-%d %H:%M:%S"
        pass

        regex = r'(\d{4}\d{1,2}\d{1,2}\d{1,2}\d{1,2}\d{1,2})'
        if re.search(regex, datetime_string):
            return "%Y%m%d%H%M%S"
        pass

        regex = r'(\d{4}-\d{1,2}-\d{1,2})'
        if re.search(regex, datetime_string):
            return "%Y-%m-%d"
        pass

        regex = r'(\d{4}\d{2}\d{2})'
        if re.search(regex, datetime_string):
            return "%Y%m%d"
        pass

        regex = r'(\d{2}\d{2}\d{2})'
        if re.search(regex, datetime_string):
            return "%y%m%d"
        pass

        return ""

    pass

    @classmethod
    def get_weekday_cn(cls, date_time_value=None):
        """
        获取给定日期的，中文星期表示（比如星期一、星期六等）
        :param date_time_value:
        :return:
        """
        if date_time_value is None:
            date_time_value = datetime.now()
        pass

        if ObjectHelper.get_type(date_time_value) is str:
            date_time_value = cls.convert_from_string(date_time_value)
        pass

        week_cn = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        return week_cn[date_time_value.weekday()]

    pass

    @classmethod
    def get_date_lunar(cls, solar_date=None, result_with_year=True):
        """
        获取给定阳历日期的阴历表示（比如）
        :param result_with_year:结果中是否包含用干支表示的年份
        :param solar_date:待转换的公历日期
        :return:
        """
        if solar_date is None:
            solar_date = datetime.now()
        pass

        if ObjectHelper.get_type(solar_date) is str:
            solar_date = cls.convert_from_string(solar_date)
        pass

        lunar_date = sxtwl.fromSolar(solar_date.year, solar_date.month, solar_date.day)

        result = ""
        if result_with_year is True:
            lunar_year = lunar_date.getYearGZ()
            lunar_year_string = ChineseData.TianG[lunar_year.tg] + ChineseData.DiZ[lunar_year.dz]
            result = StringHelper.format("{0}年", lunar_year_string)
        pass

        if lunar_date.isLunarLeap():
            result += "闰"
        pass

        result += StringHelper.format("{0}月{1}日", ChineseData.YueM[lunar_date.getLunarMonth() - 1],
                                      ChineseData.RiM[lunar_date.getLunarDay() - 1])

        return result

    pass

    @staticmethod
    def sleep(seconds: float):
        """
        线程休眠
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    pass

    @staticmethod
    def get_timestamp(target_date: datetime = None, formatter: float = 10.6) -> float | int:
        """
        获取时间戳（从1970年1月1日0时0分0秒开始计算，到目标时刻的总共时间计量单位（秒、毫秒、微秒等）数）
        :param target_date:
        :param formatter:通常使用以下三种格式：
                    1、 10.6 这是标准格式，前10位表示总共的秒数，后6位表示微秒数
                    2、 10 表示使用秒计量总共的时间耗时
                    3、 13 表示使用毫秒计量总共的时间耗时
                    4、 16 表示使用微秒计量总共的时间耗时
        :return:
        """

        if target_date is None:
            target_date = datetime.now()
        pass

        if formatter == 10:
            return int(target_date.timestamp())
        pass

        if formatter == 13:
            return int(target_date.timestamp() * 1_000)
        pass

        if formatter == 16:
            return int(target_date.timestamp() * 1_000_000)
        pass

        # 其余要求，全部返回默认的"10.6"格式
        return target_date.timestamp()


pass

pass
