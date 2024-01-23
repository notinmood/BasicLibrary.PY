"""
 * @file   : returnResult.py
 * @time   : 22:40
 * @date   : 2024/1/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.dateTimeHelper import DateTimeHelper


class ReturnResult[T]:
    """
    函数格式化的返回结果
    status: 状态(调用成败的状态)
    message: 消息（函数调用的返回消息：尤其是失败的时候可以通过此属性标识失败的原因；调用成功时此值为""或者"ok"）
    data: 数据（函数调用成功后的返回值）
    """

    @staticmethod
    def Empty() -> "ReturnResult[T]":
        return ReturnResult(False, "", None)

    @staticmethod
    def Ok(message="") -> "ReturnResult[T]":
        if not message:
            message = f"✅处理成功-({DateTimeHelper.get_string()})"
        pass

        return ReturnResult(True, message, None)

    @staticmethod
    def Bad(message="") -> "ReturnResult[T]":
        if not message:
            message = f"❌处理失败-({DateTimeHelper.get_string()})"
        pass

        return ReturnResult(False, message, None)

    def __init__(self, status: bool = True, message: str = "", data: T = None):
        self.status: bool = status
        self.message: str = message
        self.data: T = data
