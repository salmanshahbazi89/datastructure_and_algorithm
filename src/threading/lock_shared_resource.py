# import threading
#
# x = 0
#
#
# def increment():
#     global x
#     x += 1
#
#
# def thread_task(lock):
#     for i in range(10000000):
#         lock.acquire()
#         increment()
#         lock.release()
#
#
# def main_task():
#     lock = threading.Lock()
#     thread1 = threading.Thread(target=thread_task, args=(lock,), name='t1')
#     thread2 = threading.Thread(target=thread_task, args=(lock,), name='t2')
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
#
# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print("iteration i: {}, value of global variable x: {}".format(i, x))
#         x = 0
