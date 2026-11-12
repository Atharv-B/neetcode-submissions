class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for _ in range(len(nums)+1):
            freq.append([])
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for a,v in count.items():
            freq[v].append(a)
        # print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                print(res)
                if len(res) == k:
                    return res