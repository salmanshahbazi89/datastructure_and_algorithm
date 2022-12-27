class HashTable:
    def __init__(self):
        self.max = 11
        self.arr = [[] for element in range(1, self.max)]

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % 10

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for inx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][inx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    # def get(self, key):
    #     return self.arr[self.get_hash(key)]

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        for inx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][inx]


if __name__ == '__main__':
    hash_table = HashTable()
    # hash_table.add("March 1", 12)
    # hash_table.add("March 2", 12)
    # hash_table.add("March 3", 13)
    # hash_table.add("March 1", 11)
    # print(hash_table.get('March 1'))

    hash_table['march 6'] = 6
    hash_table['march 17'] = 17

    print(hash_table.arr)
    del hash_table["march 6"]
    print(hash_table.arr)

    print(hash_table["march 6"])
    print(hash_table["march 17"])

    # print("after deletion is " + str(hash_table["March 1"]))
