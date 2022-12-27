# import threading
# import time
# import random
# from src.basic_data_structures.queue import Queue
#
# order_queue = Queue()
#
#
# def place_order(orders):
#     while True:
#         order_idx = random.randint(0, 4)
#         print("Placing order for:", orders[order_idx])
#         order_queue.enqueue(orders[order_idx])
#         print(order_queue)
#         time.sleep(1)
#
#
# def serve_order():
#     while True:
#         order = order_queue.dequeue()
#         print("Now serving: ", order)
#         print(order_queue)
#         time.sleep(2)
#
#
# if __name__ == "__main__":
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     place_order_thread = threading.Thread(target=place_order, name='place_order_thread', args=(orders,))
#
#     serve_order_thread = threading.Thread(target=serve_order, name='serve_order_thread', args=(orders,))
#
#     place_order_thread.start()
#
#     time.sleep(1)
#
#     serve_order_thread.start()
