class Solution:
    def isValid(self, s: str) -> bool:
        closing_set = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        # a string of odd length can never have all valid parenthesis
        if len(s) % 2 != 0:
            return False

        for c in s:
            """
            append to stack if it is an opening parenthesis

            otherwise, confirm that the parenthesis matches the 
            parenthesis at the top of the stack

            if the stack is empty at the time of checking, it is 
            invalid because there should always be at least one
            opening parenthesis to compare to
            """

            if c in closing_set:
                if len(stack) > 0:
                    if stack.pop() != closing_set[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
 
        return len(stack) == 0