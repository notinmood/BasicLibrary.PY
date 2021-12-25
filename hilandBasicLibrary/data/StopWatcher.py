# import time
#
# __start_time = None
#
#
# def start():
#     __start_time = time.time()
#     return __start_time
#
#
# def stop():
#     if __start_time is None:
#         return None
#     else:
#         return time.time() - __start_time
#
#
# if __name__ == '__main__':
#     start()
#     time.sleep(1)
#     s = stop()
#     print(s)
