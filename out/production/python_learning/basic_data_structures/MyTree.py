class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        current_parent = self.parent

        while current_parent:
            level += 1
            current_parent = current_parent.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, key=None):
        prefix = '|---'
        space = ' ' * self.get_level() * 4
        if key is not None:
            if key == 'both':
                values = ' - '.join([str(x) for x in self.data.values()])
                print(space + prefix + values)
            else:
                print(space + prefix + self.data[key])
        else:
            print(space + prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(key)


if __name__ == "__main__":
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    apple = TreeNode("Apple")
    dell = TreeNode("Dell")
    laptop.add_child(apple)
    laptop.add_child(dell)

    tv = TreeNode("Tv")
    samsung = TreeNode("Samsung")
    lg = TreeNode("LG")
    tv.add_child(samsung)
    tv.add_child(lg)

    mobile = TreeNode("Mobile")
    nokia = TreeNode("Nokia")
    xiaomi = TreeNode("Xiaomi")
    mobile.add_child(nokia)
    mobile.add_child(xiaomi)

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(mobile)

    root.print_tree()
