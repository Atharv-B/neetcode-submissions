class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')':'(', '}':'{', ']':'['} 
        for i in s:
            if i in matches:
                if not stack or stack[-1] != matches[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
            print(stack)
        return len(stack)==0                    