class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in strs:
            key = sorted(i)
            key = "".join(key)
            # print(key)
            if key not in groups:
                groups[key] = []
            groups[key].append(i)
        print(groups)
        print(list(groups.values()))
        return list(groups.values())

        
                
        