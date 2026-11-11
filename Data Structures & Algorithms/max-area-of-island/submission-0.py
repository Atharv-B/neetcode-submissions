from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        output = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r,c))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            counter = 0
            while q:
                current_r, current_c = q.popleft()
                counter+=1
                for dr, dc in directions:
                    neighbor_r = current_r + dr
                    neighbor_c = current_c + dc
                    if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols and grid[neighbor_r][neighbor_c]==1:
                        if (neighbor_r, neighbor_c) not in visited:
                            q.append((neighbor_r, neighbor_c))
                            visited.add((neighbor_r, neighbor_c)) 
            return counter

        area = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    output = max(output, bfs(r,c))
                    # bfs(r,c)
                    # output+=1
                    
        return output




        