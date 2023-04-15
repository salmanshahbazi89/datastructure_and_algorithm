class Solution:
    def longest_palindrome(self, s):
        length = len(s)
        state = [[0 for i in range(length)] for j in range(length)]

        if length <= 1:
            return length

        for i in range(length):
            state[i][i] = True

        for i in range(1, length):
            for j in range(i+1, length):
                if j - i == 1 and s[i] == s[j]:
                    state[i][j] = True
                elif j - i == 2:
                    pass

        return state


if __name__ == '__main__':
    str = 'abcdef'
    s = Solution()
    print(s.longest_palindrome(str))