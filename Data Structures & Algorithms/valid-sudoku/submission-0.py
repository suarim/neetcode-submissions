class Solution:
    def isValidSudoku(self, sudoku_board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        box=defaultdict(set)
        def valid(num,i,j):
            if num == ".":
                return True
            if num in rows[i] or num in cols[j] or num in box[(i//3,j//3)]:
                return False
            rows[i].add(num)
            cols[j].add(num)
            box[(i//3,j//3)].add(num)
            return True

        for i in range(9):
            for j in range(9):
                if not valid(sudoku_board[i][j],i,j):
                    return False
                

        return True
