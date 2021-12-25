# from builtins import *
#
# from hiland.data import Container
#
#
# def __get_container():
#     return Container.get_dict("echo_container")
#
#
# def add_item(target_value, target_title, target_func, args=None):
#     """
#
#     :param target_value:
#     :param target_title:
#     :param target_func:
#     :param args: 如果需要传递多个参数，请把这多个参数放入[]内，形成list再传递
#     :return:
#     """
#     container = __get_container()
#     container[target_value] = (target_title, target_func, args)
#
#
# def console(display_loop_tip=False, tip_content="请输入以下数字序号，选择功能："):
#     container = __get_container()
#     if display_loop_tip:
#         input("按回车继续下一次查询")
#
#     print(tip_content)
#     display_content = ""
#     for item in container:
#         item_tuple = container[item]
#         display_content += "{0}:{1}\r\n".format(item, item_tuple[0])
#
#     print(display_content)
#     _input = input("请告诉我你的选择是:")
#     for item in container:
#         if str(item) == _input:
#             item_tuple = container[item]
#
#             if item_tuple[2] is None:
#                 item_tuple[1]()
#             else:
#                 item_tuple[1](item_tuple[2])
#
#     console(True, tip_content)
#
#
# def foo(*args):
#     print(*args)
#
#
# if __name__ == '__main__':
#     add_item(0, 'a', foo)
#     add_item(1, 'b', foo, 1)
#     add_item(2, 'c', foo, [2, "ggg"])
#     add_item(3, 'd', foo, [2, "ggg", 'hhh'])
#     console()
