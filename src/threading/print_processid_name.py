# import threading
# import os
#
#
# def task1():
#     print("thread-1 process_id:{}, name: {}".format(os.getpid(), threading.current_thread().name))
#
#
# def task2():
#     print("thread-2 process_id:{}, name: {}".format(os.getpid(), threading.current_thread().name))
#
#
# if __name__ == "__main__":
#     print("main thread process_id:{}, name: {}".format(os.getpid(), threading.main_thread().name))
#     thread1 = threading.Thread(target=task1, name='t1')
#     thread2 = threading.Thread(target=task2, name='t2')
#
#     thread1.start()
#     thread2.start()
#
#     # we use join method to stop execution of current program until a thread is completed
#     thread1.join()
#     thread2.join()
#
#     print("Done!\n")
