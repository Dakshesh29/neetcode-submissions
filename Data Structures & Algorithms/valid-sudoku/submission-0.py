class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        num = board[i][j]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
