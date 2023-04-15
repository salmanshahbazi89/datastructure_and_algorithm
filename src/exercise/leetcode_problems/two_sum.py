# noinspection PyMethodMayBeStatic
class Solution:
    # Brute Force Approach
    def two_sum_1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Optimized Approach
    def two_sum_2(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i in range(len(nums)):
            other_side = target - nums[i]
            if other_side in num_to_index:
                return [num_to_index[other_side], i]
            num_to_index[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.two_sum_2([2, 7, -1, 8, 12, 12, 13], 7))