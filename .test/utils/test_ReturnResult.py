"""
 * @file   : test_ReturnResult.py
 * @time   : 10:23
 * @date   : 2024/2/1
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.model.returnResult import ReturnResult


def test_empty():
    actual = ReturnResult.Empty()
    expected = ReturnResult(False, "", None)
    assert actual.message == expected.message
    assert actual.status == expected.status
    assert actual.data == expected.data


pass
