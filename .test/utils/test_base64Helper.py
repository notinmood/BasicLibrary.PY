"""
 * @file   : test_base64Helper.py
 * @time   : 21:55
 * @date   : 2024/1/21
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.base64Helper import Base64Helper

# 以下是为了消除ide拼写错误的警告而做的PolyFill
# noinspection all
hello_world_bytes = b'SGVsbG8sIFdvcmxkIQ=='
nihao_shijie_bytes = b'5L2g5aW977yM5LiW55WM77yB'


def test_encode_string():
    # 编码测试
    actual = Base64Helper.encode_string("Hello, World!")
    expected = hello_world_bytes
    assert actual == expected

    actual = Base64Helper.encode_string("你好，世界！")
    expected = nihao_shijie_bytes
    assert actual == expected


def test_decode_string():
    actual = Base64Helper.decode_string(hello_world_bytes)
    expected = 'Hello, World!'
    assert actual == expected

    actual = Base64Helper.decode_string(nihao_shijie_bytes)
    expected = '你好，世界！'
    assert actual == expected
