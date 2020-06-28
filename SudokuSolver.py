# solve - 0, 0
    # solve - 0, 1
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # board[2][0] = '3'
        # print(self.is_valid(board, 2, 0) )
        self.solve(board)
        # for row in board:
        #     print(row)
    
    def find_next_empty_cell(self, board):
        for row in range(9):
            for col in range(9):
                # find empty cell
                if board[row][col] == ".":
                    return row, col
        return -1, -1
    
    def solve(self, board):
        row, col = self.find_next_empty_cell(board)
        
        if row == -1 and col == -1:
            return True
        
        for value in range(1, 10):
            board[row][col] = str(value)
            
            if self.is_valid(board, row, col) and self.solve(board):
                return True
            
            board[row][col] = "."
            
        return False
        
    def is_valid(self, board, row, col):            
        # row check
        seen = []
        for entry in board[row]:
            if entry is not ".":
                if entry in seen:
                    #print("Invalid board[{}][{}]->{}".format(row, col, entry))
                    return False
                else:
                    seen.append(entry)
                #print("entry:{} seen:{}".format(entry, seen))
        #print("Row check passed")
        
        # column check
        seen = []
        for i in range(9):
            entry = board[i][col]
            if entry is not ".":
                if entry in seen:
                    #print("Invalid board[{}][{}]->{}".format(row, col, entry))
                    return False
                else:
                    seen.append(entry)
                #print("entry:{} seen:{}".format(entry, seen))
        #print("Column check passed")    
            
        # square check
        seen = []
        row_start = (row//3)*3
        col_start = (col//3)*3
        for y in range(row_start, row_start + 3):
            for x in range(col_start, col_start + 3):
                entry = board[y][x]
                if entry is not "." and entry in seen:
                    #print("Invalid board[{}][{}]->{}".format(row, col, entry))
                    return False  
                else:
                    seen.append(entry)           
        #print("Valid board[{}][{}]->{}".format(row, col, board[row][col]))
        
        return True
        # fill each value 1-9, check rule voilation
            # rule voilated -> go back
            # rule not voilated -> recursive call
            
            
        
