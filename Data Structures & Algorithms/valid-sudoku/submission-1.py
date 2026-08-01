class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()
            for j in range(9):
                value=board[i][j]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
                
        for i in range(9):
            seen=set()
            for j in range(9):
                value=board[j][i]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for row_start in range(0,9,3):
            for col_start in range(0,9,3):
                seen=set()
                for i in range(3):
                    for j in range(3):

                        value=board[row_start+i][col_start+j]
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value) 
        return True

        