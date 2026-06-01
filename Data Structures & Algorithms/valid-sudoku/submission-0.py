class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen=set()

        if board ==None:
            return False
        

        for r in range(len(board)):

            for c in range(len(board)):

                value=board[r][c]

                if value=='.':
                    continue
                
                row=("row",r,value)
                column=("col",c,value)
                box=("box",r//3,c//3,value)

                if row in seen or column in seen or box in seen:
                    return False
                
                else:
                    seen.add(row)
                    seen.add(column)
                    seen.add(box)
        

        return True

        
