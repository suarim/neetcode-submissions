class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        boxes={}
        for i in range(len(board)):
            rows[i]=[]
            cols[i]=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                boxes[(i//3,j//3)]=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3,j//3)]:
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                boxes[(i//3,j//3)].append(board[i][j])


        return True