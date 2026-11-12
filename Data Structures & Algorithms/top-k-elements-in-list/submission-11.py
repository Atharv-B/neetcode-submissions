class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        # create nested lists for storing the frequency
        for _ in range(len(nums)+1):
            freq.append([])

        # frequency counter basically
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        # Most important step as this counts the number
        # of times an element has occured in nums.
        for a,v in count.items():
            freq[v].append(a)
        
        res = []

        # Then easily you can return the top K elements 
        # by traversing the list in return.
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                print(res)
                if len(res) == k:
                    return res