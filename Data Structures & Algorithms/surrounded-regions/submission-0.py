class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        # Stage 1: We convert all the "O" on the border to some temp "T"
        def dfs(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in directions:
                    dfs(r+dr, c+dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1]) or (c in [0, COLS-1]):
                    dfs(r,c)

        # Stage 2: Conver all O into X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Stage 3: revert T into O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        

        