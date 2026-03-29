class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = True
        string = ""
        string = s.replace(" ", "")
        string = string.replace("?", "").lower()
        string = string.replace(",", "")
        string = string.replace("'", "")
        string = string.replace(".", "")
        string = string.replace(":", "")

        print(string)
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                palindrome = False
                break
            left+=1
            right-=1
        return palindrome
            
            
                
        
        
        
        