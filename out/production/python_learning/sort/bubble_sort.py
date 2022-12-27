import random


def bubble_sort(items, key=None):
    size = len(items)
    swapped = False

    if key is None:
        for i in range(size - 1):
            for j in range(size - 1 - i):
                if items[j] > items[j + 1]:
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp
                    swapped = True
            if not swapped:
                break;
        return items
    else:
        for i in range(size - 1):
            for j in range(size - 1 - i):
                if items[j][key] > items[j + 1][key]:
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp
                    swapped = True
            if not swapped:
                break;
        return items


if __name__ == '__main__':
    # numbers = [5, 4, 6, 78, 24, 12, 11, 13, 37, 48]
    # random_list = []
    # for i in range(0, 10):
    #     n = random.randint(1, 30)
    #     random_list.append(n)
    #
    # sorted_list = bubble_sort(random_list)
    # print(sorted_list)

    elements = [
        {'name': 'salman', 'transaction_amount': 800, 'device': 'phone'},
        {'name': 'ali', 'transaction_amount': 100, 'device': 'atm'},
        {'name': 'hasan', 'transaction_amount': 1120, 'device': 'pc'},
        {'name': 'mehdi', 'transaction_amount': 900, 'device': 'pos'}
    ]
    sorted_elements_by_key = bubble_sort(elements, 'name')
    for element in sorted_elements_by_key:
        print(element)
