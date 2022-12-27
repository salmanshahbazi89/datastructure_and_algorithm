def insertion_sort(items_to_sort):
    for i in range(1, len(items_to_sort)):
        current_value = items_to_sort[i]
        for j in range(i - 1, -1, -1):
            if j == i - 1:
                if items_to_sort[i] < items_to_sort[j]:
                    temp = items_to_sort[j]
                    items_to_sort[j] = current_value
                    items_to_sort[i] = temp
                else:
                    break
            else:
                if items_to_sort[j + 1] < items_to_sort[j]:
                    temp = items_to_sort[j]
                    items_to_sort[j] = items_to_sort[j + 1]
                    items_to_sort[j + 1] = temp


def find_median(items_to_find_median):
    result = []
    result.append(items_to_find_median[0])
    for i in range(1, len(items_to_find_median)):
        current_value = items_to_find_median[i]
        for j in range(i - 1, -1, -1):
            if j == i - 1:
                if items_to_find_median[i] < items_to_find_median[j]:
                    temp = items_to_find_median[j]
                    items_to_find_median[j] = current_value
                    items_to_find_median[i] = temp
                else:
                    break
            else:
                if items_to_find_median[j + 1] < items_to_find_median[j]:
                    temp = items_to_find_median[j]
                    items_to_find_median[j] = items_to_find_median[j + 1]
                    items_to_find_median[j + 1] = temp
        if i % 2 == 0:
            result.append(items_to_find_median[i // 2])
        else:
            avg = (items_to_find_median[i // 2] + items_to_find_median[i // 2 + 1]) / 2
            result.append(avg)

    return result


if __name__ == '__main__':
    items = [2, 1, 5, 7, 2, 0, 5]
    # insertion_sort(items)
    # print(items)
    medians = find_median(items)
    print(medians)
