class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1 
            window.add(s[right])
            result = max(result, len(window))
        return result

        

            
        