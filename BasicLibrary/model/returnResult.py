"""
 * @file   : returnResult.py
 * @time   : 22:40
 * @date   : 2024/1/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


@dataclass
class ReturnResult(Generic[T]):
    """
    函数格式化的返回结果
    status: 状态(调用成败的状态)
    message: 消息（函数调用的返回消息：尤其是失败的时候可以通过此属性标识失败的原因；调用成功时此值为""或者"ok"）
    data: 数据（函数调用成功后的返回值）
    """
    status: bool = True
    message: str = ""
    data: T = None
