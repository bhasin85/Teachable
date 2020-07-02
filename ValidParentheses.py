class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "[":"]", "{":"}"}
        stack = []
        
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                starting_bracket = stack.pop()
                if brackets[starting_bracket] != c:
                    return False
                
        return True if len(stack) == 0 else False
