"""
 * @file   : uuidHelper.py
 * @time   : 上午10:52
 * @date   : 2024/6/15
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import ulid


class UUIDHelper:
    """
    使用ulid生成UUID。
    优势：
    1. 可以保证UUID的唯一性。
    2. 可以保证UUID的顺序性。
    3. 可以保证UUID的随机性。
    说明：
    格式如下：t*10+r*16
    其中：    t is Timestamp；    r is Randomness
    """

    @staticmethod
    def new():
        return ulid.new()


pass
