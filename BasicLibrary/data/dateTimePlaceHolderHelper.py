"""
 * @file   : dateTimePlaceHolderHelper.py
 * @time   : 19:46
 * @date   : 2024/3/18
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from datetime import timedelta
from typing import Callable, ParamSpec

from BasicLibrary.data.collectionHelper import CollectionHelper
from BasicLibrary.data.dateTimeHelper import DateTimeHelper
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.model.returnResult import ReturnResult

P = ParamSpec("P")


# TODO:xiedali@2024/03/18 目前支持的时间粒度为日，后续如果业务需要可以升级为秒、分、小时、周、月、年等各种时间间隔
class DateTimePlaceHolderHelper:
    """
    日期占位符工具类
    """

    @classmethod
    def loop_biz_with_date(cls, start_date_string: str, end_date_string: str, biz_string_with_placeholder: str,
                           deal_biz_detail_func: Callable[[str, str, P.kwargs], ReturnResult],
                           **kwargs_for_deal_func):
        """
        处理指定生成开始日期和结束日期内的业务信息
        说明：
        1. 对给定每个时间间隔处理结果的展示，可以通过给 **kwargs_for_deal_func 指定命名参数“recordEveryDealResultType”来实现，
        目前仅支持“console”，即在控制台显示（默认实现）；给定其他值时，不做任何处理。
        2. 如果传统命名参数“dealingDateStrings”(类型可以是：通过逗号或者分号拼接的字符串、list列表、tuple元组)，则会忽略start_date_string开始日期和结束日期end_date_string界定的时间段
        :param start_date_string:8位字符串，格式为 yyyymmdd
        :param end_date_string:8位字符串，格式为 yyyymmdd
        :param biz_string_with_placeholder: 带有占位符的目录，支持 ymdhis的各种标准写法
        :param deal_biz_detail_func:处理具体业务的函数，其参数为：1.具体的业务数据（替换完占位符的真实业务数据）；2.处理业务对应的日期字符串；3.kwargs
        :param kwargs_for_deal_func:
        :return:
        """

        def record_every_deal_result(message: str):
            record_type = kwargs_for_deal_func.get("recordEveryDealResultType", "console").lower()
            if record_type == "console":
                print(message)
            pass

        pass

        def deal_biz_every_date(dealing_date_string: str):
            biz_string: str = cls.replace_placeholder(biz_string_with_placeholder, dealing_date_string)

            # 调用注入的方法，处理业务逻辑
            rr: ReturnResult = deal_biz_detail_func(biz_string, dealing_date_string, **kwargs_for_deal_func)

            # 展示处理结果
            if not rr:
                record_every_deal_result(f"🔵【{dealing_date_string}】处理完成-{DateTimeHelper.get_string()}")
                return
            pass

            if rr.message:
                record_every_deal_result(rr.message)
                return
            pass

            if rr.status:
                record_every_deal_result(f"✅【{dealing_date_string}】处理成功-{DateTimeHelper.get_string()}")
            else:
                record_every_deal_result(f"❌【{dealing_date_string}】处理失败-{DateTimeHelper.get_string()}")
            pass

        dealing_date_strings = kwargs_for_deal_func.get("dealingDateStrings", [])
        dealing_date_strings = CollectionHelper.format(dealing_date_strings)
        # 先判定是否有按照列表传入的需要处理的日期，如果有的话优先处理，并忽略start_date和end_date界定的日期范围
        if dealing_date_strings and len(dealing_date_strings) > 0:
            for _item in dealing_date_strings:
                deal_biz_every_date(_item)
            pass
        else:
            star_date = DateTimeHelper.convert_from_string(start_date_string)
            end_date = DateTimeHelper.convert_from_string(end_date_string)

            while star_date <= end_date:
                _dealing_date_string = DateTimeHelper.get_compact_date_string(star_date)
                deal_biz_every_date(_dealing_date_string)
                # 对日期进行向下推进
                star_date = star_date + timedelta(days=1)
            pass
        pass

    pass

    @classmethod
    def loop_dirs_with_date(cls, start_date_string: str, end_date_string: str, target_dir_with_placeholder: str,
                            deal_dir_detail_func: Callable[[str, str, P], ReturnResult], **kwargs_for_deal_func):
        """
        处理指定生成开始日期和结束日期内路径下的所有的文件
        说明：
        1. 对给定每个时间间隔处理结果的展示，可以通过给 **kwargs_for_deal_func 指定命名参数“recordEveryDealResultType”来实现，
        目前仅支持“console”，即在控制台显示（默认实现）；给定其他值时，不做任何处理。
        2. 如果传统命名参数“dealingDateStrings”(类型可以是：通过逗号或者分号拼接的字符串、list列表、tuple元组)，则会忽略start_date_string开始日期和结束日期end_date_string界定的时间段
        :param start_date_string:8位字符串，格式为 yyyymmdd
        :param end_date_string:8位字符串，格式为 yyyymmdd
        :param target_dir_with_placeholder: 带有占位符的目录，支持 ymd的各种标准写法
        :param deal_dir_detail_func:处理具体目录的函数，其参数为:1.具体目录的全路径;2.包含处理目录对应的日期字符串
        :return:
        """

        cls.loop_biz_with_date(start_date_string, end_date_string, target_dir_with_placeholder, deal_dir_detail_func,
                               **kwargs_for_deal_func)

    pass

    @staticmethod
    def replace_placeholder(biz_string_with_placeholder: str, date_string: str) -> str:
        """
        替换字符串内占位符为实际日期时间
        :param biz_string_with_placeholder:
        :param date_string:
        :return:
        """
        biz_string = StringHelper.format(
            biz_string_with_placeholder,
            dir_ymd=date_string[0:8],
            dir_ym=date_string[0:6],
            yyyymmdd=date_string[0:8],
            yymmdd=date_string[2:8],
            ymmdd=date_string[3:8],
            yyyymm=date_string[0:6],
            mmdd=date_string[4:8],
            yyyy=date_string[0:4],
            yy=date_string[2:4],
            y=date_string[3:4],
            mm=date_string[4:6],
            dd=date_string[6:8],
        )

        return biz_string

    pass


pass
