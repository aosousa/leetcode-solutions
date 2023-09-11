class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            middle_index = i + (j - i) // 2

            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                i = middle_index + 1
            else:
                j = middle_index - 1

        return -1