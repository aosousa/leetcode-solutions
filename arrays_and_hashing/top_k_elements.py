class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elements = {}

        for i in nums:
            if i not in elements:
                elements[i] = 0
            
            elements[i] += 1

        sorted_elements = sorted(elements, key=elements.get, reverse=True)
        return sorted_elements[0:k]