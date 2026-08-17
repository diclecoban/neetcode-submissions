class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        column_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                val = board[row][col]
                box_index = (row // 3) * 3 + (col // 3)

                if(val in row_set[row]):
                    return False
                if(val in column_set[col]):
                    return False
                if(val in square_set[box_index]):
                    return False
                if (val == '.'):
                    continue
                
                row_set[row].add(val)
                column_set[col].add(val)
                square_set[box_index].add(val)

        return True


        