from src.basic_data_structures.MyQueue import Queue

if __name__ == "__main__":
    numbers_queue = Queue()

    numbers_queue.enqueue('1')

    for i in range(15):
        top_element = numbers_queue.front()
        print("   ", top_element)
        numbers_queue.enqueue(top_element + '0')
        numbers_queue.enqueue(top_element + '1')
        numbers_queue.dequeue()