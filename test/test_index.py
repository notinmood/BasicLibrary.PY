"""
 * @file   : test_index.py
 * @time   : 9:43
 * @date   : 2021/11/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import pytest

"""
这是一个关于Pytest的说明与简单演示文件

1、说明：
    - 单元测试采用PyTest工具
    - PyTest工具兼容unitTest
────────────────────────
2、命名约定：
    - 文件名称、方法名称全部以test_开头
    - 类型名称以 Test 开头
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
