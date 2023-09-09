class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric characters
        converted_s = ''.join([i for i in s.lower() if i.isalnum()])

        # compare the converted string to the reverse converted string
        return converted_s == converted_s[::-1]
    
    def isAlphanumeric(self, c: str):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))


    def isPalindromeTwoPointer(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:
            # avoid pointer going out of bounds
            while left_pointer < right_pointer and not self.isAlphanumeric(s[left_pointer]):
                left_pointer += 1

            # avoid pointer going out of bounds
            while right_pointer > left_pointer and not self.isAlphanumeric(s[right_pointer]):
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            left_pointer += 1
            right_pointer -= 1
        
        return True
