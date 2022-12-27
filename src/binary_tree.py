class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data_to_add):
        if self.data == data_to_add:
            return

        if self.data > data_to_add:
            if self.left:
                self.left.add_child(data_to_add)
            else:
                self.left = BinarySearchTree(data_to_add)

        if self.data < data_to_add:
            if self.right:
                self.right.add_child(data_to_add)
            else:
                self.right = BinarySearchTree(data_to_add)

    def inorder_travers(self):
        elements = []

        if self.left:
            elements += self.left.inorder_travers()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_travers()

        return elements

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self


def build_binary_tree(elements):
    binary_search_tree = BinarySearchTree(elements[0])

    for element in numbers_to_add:
        binary_search_tree.add_child(element)

    return binary_search_tree


if __name__ == '__main__':
    numbers_to_add = [8, 9, 15, 4, 2, 18, 19, 25]
    binary_tree = build_binary_tree(numbers_to_add)
    print(binary_tree.inorder_travers())
    print(binary_tree.search(150))

    new_binary_tree = binary_tree.delete(19)
    print(new_binary_tree.inorder_travers())

