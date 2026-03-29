class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_counter_s = {}
        frequency_counter_t = {}

        for i in s:
            if i in frequency_counter_s:
                frequency_counter_s[i] += 1
            else:
                frequency_counter_s[i] = 1
        
        for j in t:
            if j in frequency_counter_t:
                frequency_counter_t[j] += 1
            else:
                frequency_counter_t[j] = 1

        if frequency_counter_s == frequency_counter_t:
            return True
        else:
            return False