class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        boxes={}
        for i in range(len(board)):
            rows[i]=[]
            cols[i]=[]
        for r in range(len(board)):
            for c in range(len(board[0])):
                boxes[(r//3,c//3)]=[]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3,c//3)]:
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                boxes[(r//3,c//3)].append(board[r][c])
        return True
