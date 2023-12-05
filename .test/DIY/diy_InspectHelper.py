"""
 * @file   : diy_InspectHelper.py
 * @time   : 12:17
 * @date   : 2023/11/28
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.environment.inspectHelper import InspectHelper


def debug():
    call_name = InspectHelper.get_stack()

    count = len(call_name)
    print("inspect调用堆栈上对象的总长度为：{}".format(count))

    print("────────────────────────")
    print("以下内容为第0个元素的信息：(第0个对象就是被调用方，包含被调用方的各种信息)")
    e0 = call_name[0]
    print(e0)
    print(e0.filename)
    print(e0.function)

    print("────────────────────────")
    print("以下内容为第1个元素的信息：(第1个对象就是调用方，就是当前方法所在的对象的各种信息)")
    e1 = call_name[1]
    print(e1)
    print(e1.filename)
    print(e1.function)

    print("════════════════════════")
    print("使用包装后的方法")
    print(InspectHelper.get_current_method_name())
    print(InspectHelper.get_current_file_name())


if __name__ == '__main__':
    debug()

    print("***********************")
    print("因为当前不在在某个方法内调用，以下方法获取不到方法名称")
    print(InspectHelper.get_current_method_name())
