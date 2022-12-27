# import threading
#
#
# def print_square(num):
#     print("the square is: {}\n".format(num * num))
#
#     cnt = 0
#     for i in range(1000000000):
#         cnt += 1
#
#     print("count is: {}\n".format(cnt))
#
#
# def print_cube(num):
#     print("the cube is: {}\n".format(num * num * num))
#
#     cnt = 0
#     for i in range(1000000000):
#         cnt += 1
#
#     print("count is: {}\n".format(cnt))
#
#
# if __name__ == "__main__":
#     thread1 = threading.Thread(target=print_square, args={10})
#     thread2 = threading.Thread(target=print_cube, args={10})
#
#     thread1.start()
#     thread2.start()
#
#     print("main is running - 1\n")
#
#     # we use join method to stop execution of current program until a thread is completed
#     thread1.join()
#     thread2.join()
#
#     print("main is running - 2\n")
#
#     print("Done!\n")
