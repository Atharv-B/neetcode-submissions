class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # having a loop or a cycle returns false
        # to check if we have loops we can use a set()
        # hashmap = crs | preq
        #           0   | [] {done = 2}
        #           1   | []
        #           2   | []
        # Then we do dfs on every crs and and the preq and see if they can be completed.

        # This hashmap maps each course to preq list
        hashmap = {}
        for num in range(numCourses):
            hashmap[num] = []
        
        for courses, preqs in prerequisites:
            hashmap[courses].append(preqs)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if hashmap[crs] == []:
                return True
            visited.add(crs)
            # we want to run recursive dfs on the preqs
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            hashmap[crs] = []
            return True
        
        for crs_ in range(numCourses):
            if not dfs(crs_): return False
        return True

