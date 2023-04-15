# noinspection PyMethodMayBeStatic
class Solution:
    def length_of_longest_substring_1(self, s: str) -> int:
        queue = []
        length_of_substr = 0
        for current_ch in s:
            if current_ch not in queue:
                queue.append(current_ch)
            else:
                if len(queue) > length_of_substr:
                    length_of_substr = len(queue)
                del queue[:queue.index(current_ch) + 1]
                queue.append(current_ch)

        if len(queue) > length_of_substr:
            length_of_substr = len(queue)
        return length_of_substr

    def length_of_longest_substring_2(self, s: str) -> int:
        length_of_substr, queue = 0, ''
        for current_ch in s:
            if current_ch not in queue:
                queue += current_ch
            else:
                queue = queue[queue.index(current_ch) + 1:] + current_ch

            if len(queue) > length_of_substr:
                length_of_substr = len(queue)

        return length_of_substr


if __name__ == '__main__':
    solution = Solution()
    l1 = solution.length_of_longest_substring_1("ababxyzwmn")
    l2 = solution.length_of_longest_substring_2("ababxyzwmn")
    print(l1)
    print(l2)