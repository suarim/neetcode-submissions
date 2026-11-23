class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        boxes={}
        for i in range(len(board[0])):
            rows[i]=[]
            cols[i]=[]
            boxes[i]=[]
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                box = (i//3)*3+(j//3)
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[box]:
                    return False
                rows[i].append(board[i][j])    
                cols[j].append(board[i][j])    
                boxes[box].append(board[i][j])
        return True