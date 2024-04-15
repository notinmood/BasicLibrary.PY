"""
 * @file   : lunarDate.py
 * @time   : 下午3:30
 * @date   : 2024/4/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from datetime import datetime

import sxtwl

from BasicLibrary.data.chineseData import ChineseData


class LunarDate:
    def __init__(self, solar_year=None, solar_month=None, solar_day=None):
        if not solar_year:
            solar_year = datetime.year
        pass

        if not solar_month:
            solar_month = datetime.month
        pass

        if not solar_day:
            solar_day = datetime.day
        pass

        lunar_date = sxtwl.fromSolar(solar_year, solar_month, solar_day)
        lunar_year = lunar_date.getYearGZ()

        self.isLunarLeap = lunar_date.isLunarLeap()
        self.year = ChineseData.TianG[lunar_year.tg] + ChineseData.DiZ[lunar_year.dz]
        self.month = ChineseData.YueM[lunar_date.getLunarMonth() - 1]
        self.day = ChineseData.RiM[lunar_date.getLunarDay() - 1]

        # self.year_TG = ChineseData.TianG[lunar_year.tg]
        # self.year_DZ = ChineseData.DiZ[lunar_year.dz]
        ## self.SX = lunar_year.ShX  # TODO: 农历生肖

    def __str__(self):
        return self.get_string()

    def get_string(self, formatter: str = "{yy}年{mm}月{dd}日"):
        """
        获取格式化的农历日期字符串
        :param formatter: 格式化字符串，支持的格式化参数有：yy(年), mm(月), dd(日)
        :return:
        """
        month = self.month
        if self.isLunarLeap:
            month = "闰" + self.month
        pass

        return formatter.format(yy=self.year, mm=month, dd=self.day)
