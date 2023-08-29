class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)