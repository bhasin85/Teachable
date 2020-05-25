class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #self._print(board)
        #print(self.is_empty(board))
        
        #self.fill_cells(board)
        limit = 1
        while self.is_empty(board):
            self.guess_cells(board, limit)
            limit += 1
            
        
    def _print(self, board: List[List[str]]):
        print("-"*18)
        for row in board:
            print(' '.join(row))
        print("-"*18)
    
    def is_empty(self, board: List[List[str]]):
        for row in board:
            # Check not empty
            if "." in row:
                #print("Invalid row empty {}".format(row))
                return True
        return False
            
    def is_valid(self, board: List[List[str]]):
        all_values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        
        # Validate row
        for row in board:
            if len(all_values - set(row)) > 0:
                print("Invalid row diff {}".format(row))
                return False
        
        # Validate column 
        i = 0
        while i < 9:
            j = 0
            col_values = set()
            while j < 9:
                col_values.add(board[i][j])
                
            if len(all_values - col_values) > 0:
                print("Invalid col diff {}".format(col_values))
                return False
        
        # Validate grid
        # grid_values = set()
        
        return True
        
    def fill_cells(self, board: List[List[str]]):
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == '.':
                    possible_values = self.cell_values(i, j, board)
                    if len(possible_values) == 1:
                        board[i][j] = possible_values.pop()
                        #print("{},{} -> {}".format(i, j, board[i][j]))
                        self.fill_cells(board)
                        break
                j += 1
            i += 1
            
    def guess_cells(self, board: List[List[str]], limit):
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == '.':
                    possible_values = self.cell_values(i, j, board)
                    if len(possible_values) <= limit:
                        for possible_value in possible_values:
                            import copy
                            guess_board = copy.deepcopy(board)
                            guess_board[i][j] = possible_value
                            print("Guessing {},{} -> {} limit:{}".format(i, j, guess_board[i][j], limit))
                            self.fill_cells(guess_board)
                            self._print(board)
                            if self.is_empty(guess_board):
                                print("Guess Passed {},{} -> {}".format(i, j, guess_board[i][j]))
                                board = guess_board
                                return
                            else:
                                print("Guess Failed {},{} -> {}".format(i, j, guess_board[i][j]))
                j += 1
            i += 1
                    
                    
    def cell_values(self, row, column, board):
        # 1-9 subtract row+column+grid values
        all_values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row_values = set()
        col_values = set()
        grid_values = set()
        
        
        # row values
        i, j = row, 0
        while j < 9:
            if board[i][j] != '.':
                row_values.add(board[i][j])
            j += 1

        # column values
        i, j = 0, column
        while i < 9:
            if board[i][j] != '.':
                col_values.add(board[i][j])
            i += 1
        
        # grid values
        if row < 3:
            temp_i = 0
        elif row > 5:
            temp_i = 6
        else:
            temp_i = 3
            
        if column < 3:
            temp_j = 0
        elif column > 5:
            temp_j = 6
        else:
            temp_j = 3

        i, j = temp_i, temp_j
        max_i, max_j = i+3, j+3
        
        #print("{},{} grid:({}, {}) ({}, {})".format(row, column, i, j, max_i, max_j))
        while i < max_i:
            j = temp_j
            while j < max_j:
                if board[i][j] != '.':
                    grid_values.add(board[i][j])
                j += 1
            i += 1
            
        
        possible_values = all_values - set(list(row_values) + list(col_values) + list(grid_values))
        # if len(possible_values) == 1:
        #     print("{},{} possible_values:{} row_values:{} col_values:{} grid_values:{}".format(row, column, possible_values, row_values, col_values, grid_values))
        return possible_values
