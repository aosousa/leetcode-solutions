class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits_str = str(int(''.join([str(digit) for digit in digits])) + 1)
        
        return [int(digit) for digit in digits_str]