"""
 * @file   : test_DatabaseDemo.py
 * @time   : 11:58
 * @date   : 2021/12/25
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import pytest


@pytest.fixture(scope='function')
def test_setup():
    print('setup ing')


def test_a(test_setup):
    print('aaa')
