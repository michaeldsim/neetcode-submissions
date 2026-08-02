class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                number = board[i][j]
                if number == '.':
                    continue

                square = (i // 3) * 3 + (j // 3)
                if number in rows[i] or number in cols[j] or number in squares[square]:
                    return False
                
                rows[i].add(number)
                cols[j].add(number)
                squares[square].add(number)
        
        return True