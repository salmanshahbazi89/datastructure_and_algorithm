class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr_node = self.head
            while itr_node.next:
                itr_node = itr_node.next
            itr_node.next = Node(data, None)

    def insert_values(self, value_list):
        self.head = None

        for value in value_list:
            node = Node(value, self.head)
            self.head = node

    def get_length(self):
        cnt = 0
        itr_node = self.head
        while itr_node is not None:
            itr_node = itr_node.next
            cnt = cnt + 1

        return cnt

    def remove_at(self, index):
        length = self.get_length()

        if index > length - 1:
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        else:
            counter = 0
            itr_node = self.head
            itr_node_next = itr_node.next

            while counter < index - 1:
                itr_node = itr_node.next
                itr_node_next = itr_node.next
                counter = counter + 1

            itr_node.next = itr_node_next.next

    def insert_after_value(self, data_after, data_to_insert):
        itr_node = self.head
        itr_node_next = itr_node.next

        while itr_node.data != data_after:
            itr_node = itr_node.next
            itr_node_next = itr_node.next

        node_to_add = Node(data_to_insert, itr_node_next)
        itr_node.next = node_to_add

    def remove_by_value(self, data):
        itr_node = self.head
        itr_node_next = itr_node.next

        if self.head.data == data:
            self.head = self.head.next
            return

        while itr_node.next is not None and itr_node.next.data != data:
            itr_node = itr_node.next
            itr_node_next = itr_node.next

        if itr_node.next is None:
            print("the given data does not exist in the list.")
        else:
            itr_node.next = itr_node_next.next

    def print(self):
        contents = []
        traverse_node = self.head
        while traverse_node is not None:
            contents.append(traverse_node.data)
            traverse_node = traverse_node.next
        print(' ---> '.join(map(str, contents)))


if __name__ == "__main__":
    print("main method started.")
    linked_list = LinkedList()

    # linked_list.insert_at_beginning("0")
    # linked_list.insert_at_beginning("1")
    # linked_list.insert_at_end("-1")
    # linked_list.insert_at_end("-2")
    # linked_list.insert_at_beginning("2")
    # linked_list.insert_at_beginning("3")
    # linked_list.insert_at_beginning("4")

    # linked_list.insert_values(['1', '2', '3', '4', '5', '6'])

    # linked_list.print()
    # print("length:" + str(linked_list.get_length()))

    # linked_list.remove_at(6)
    # linked_list.print()

    # linked_list.insert_after_value('4', '100')

    # linked_list.remove_by_value('16')
    linked_list.print()
