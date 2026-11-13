class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                curr_r, curr_c = q.popleft()
                for dr, dc in directions:
                    neighbor_r = dr+curr_r
                    neighbor_c = dc+curr_c
                    if 0<= neighbor_r < row and 0<=neighbor_c<col and grid[neighbor_r][neighbor_c]==1:
                        fresh -= 1
                        grid[neighbor_r][neighbor_c]=2
                        q.append([neighbor_r, neighbor_c])
            time+=1
        return time if fresh==0 else -1


        