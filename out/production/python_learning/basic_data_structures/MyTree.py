# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         current_parent = self.parent
#
#         while current_parent is not None:
#             level += 1
#             current_parent = self.parent
#
#         return level
#
#     def add_child(self, data):
#         child = TreeNode(data)
#         child.parent = self
#         self.children.append(child)
#
#     def print_tree(self):
#         space = ' ' * self.get_level() * 3
#         print(space + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()


if __name__ == "__main__":
    print("hell")
    print("fuck")
    # root = TreeNode("Electronics")
    #
    # laptop = TreeNode("Laptop")
    #
    # root.children.append(laptop)
    # apple = TreeNode("Apple")
    # dell = TreeNode("Dell")
    # laptop.children.append(apple)
    # laptop.children.append(dell)
    # laptop.children.append(dell)
    # tv = TreeNode("Tv")
    # samsung = TreeNode("Samsung")
    # lg = TreeNode("LG")
    # tv.children.append(samsung)
    # tv.children.append(lg)
    # mobile = TreeNode("Mobile")
    # nokia = TreeNode("Nokia")
    # xiaomi = TreeNode("Xiaomi")
    # mobile.children.append(nokia)
    # mobile.children.append(xiaomi)
    #
    # root.children.append(laptop)
    # root.children.append(tv)
    # root.children.append(mobile)

    # root.print_tree()
