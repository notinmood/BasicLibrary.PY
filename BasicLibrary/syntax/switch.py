"""
 * @file   : switch.py
 * @time   : 14:09
 * @date   : 2022/3/12
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# 作者：小鱼二
# 链接：https: // www.zhihu.com / question / 21123544 / answer / 42957820
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Switch(object):
    """
    switch 语句。(特别说明：请使用官方正式的表述方式 - Python3.10 后已经提供了 match/case 结构。)
    使用用例，参考下面的 main方法
    """

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        # raise StopIteration

    def match(self, *args):
        """Indicate whether to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


if __name__ == '__main__':
    v = 'ten'
    v = 'nine'
    for case in Switch(v):
        if case('one'):
            print(1)
            break
        if case('two'):
            print(2)
            break
        if case('nine'):
            pass
        if case('ten'):
            print(10)
            break
        if case('eleven'):
            print(11)
            break
        if case():  # default, could also just omit condition or 'if True'
            print("something else!")
            # No need to break here, it'll stop anyway
