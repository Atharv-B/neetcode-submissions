from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                current_r, current_c = q.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    neighbor_r = current_r + dr
                    neighbor_c = current_c + dc
                    if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols and grid[neighbor_r][neighbor_c]=="1":
                        if (neighbor_r, neighbor_c) not in visited:
                            q.append((neighbor_r, neighbor_c))
                            visited.add((neighbor_r, neighbor_c))


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands


    
