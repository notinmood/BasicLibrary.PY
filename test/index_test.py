"""
 * @file   : index_test.py
 * @time   : 9:43
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import pytest

"""
说明：
    - 单元测试采用PyTest工具
    - PyTest工具兼容unitTest
"""


def test_upper():
    assert 'foo'.upper() == 'FOO'


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        with pytest.raises(TypeError):
            x + []
