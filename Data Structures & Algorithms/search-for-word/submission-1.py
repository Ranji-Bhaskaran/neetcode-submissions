class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word): return True
            if (min(r,c) < 0 or r >= Rows or c >= Cols or word[i] != board[r][c] or (r,c) in visit):
                return False

            visit.add((r,c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            visit.remove((r,c))
            return res


        for r in range(Rows):
            for c in range(Cols):
                if dfs(r, c, 0): return True

        return False