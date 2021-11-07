from utils.data.StringHelper import *

if __name__ == '__main__':
    result = StringHelper.format("我的名字是{0},我的年龄是{1}", "zhangsan", 20)
    print(result)
