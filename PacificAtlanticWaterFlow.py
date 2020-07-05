
        
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific = [[False for column in range(len(matrix[0]))] for row in range(len(matrix))]
        atlantic = [[False for column in range(len(matrix[0]))] for row in range(len(matrix))]
        visited = [[False for column in range(len(matrix[0]))] for row in range(len(matrix))]
        
        result = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                _print = True if row == 3 and column ==27 else False
                self._pacificAtlantic(matrix, row, column, result, visited, pacific, atlantic, _print)
                if _print:
                    print("-------->row:{} column:{}".format(row, column))
        return result
        
    def _pacificAtlantic(self, matrix, row, column, result, visited, pacific, atlantic, _print):
        _print = True if row == 3 and column ==27 else False
        if _print:
            print("row:{} column:{}".format(row, column))
        
        if [row, column] in result:
            if _print:
                print("row:{} column:{} already found {}:{}".format(row, column, pacific[row][column], atlantic[row][column]))
            return True, True 
        
        if not visited[row][column]:
            visited[row][column] = True
        else:
            if _print:
                print("row:{} column:{} already visited {}:{}".format(row, column, pacific[row][column], atlantic[row][column]))
            return pacific[row][column], atlantic[row][column]
        
        # Pacific shore points
        if row == 0 or column == 0:
            pacific[row][column] = True
            
        # Atlantic shore points
        if row == len(matrix)-1 or column == len(matrix[0])-1:
            atlantic[row][column] = True
            
        # Check is shore point
        if pacific[row][column] and atlantic[row][column]:
            result.append([row, column])
            if _print:
                print("row:{} column:{} shore {}:{}".format(row, column, pacific[row][column], atlantic[row][column]))            
            return pacific[row][column], atlantic[row][column]
            
        # find neighbours
        up    = [row-1, column] if row-1>=0 else [-1, -1]
        down  = [row+1, column] if row+1<=len(matrix)-1 else [-1, -1]
        left  = [row, column-1] if column-1>=0 else [-1, -1]
        right = [row, column+1] if column+1<=len(matrix[0])-1 else [-1, -1]
        if _print:
            print("row:{} column:{} up:{} down:{} left:{} right:{}".format(row, column, up, down, left, right))
            
        if up != [-1, -1] and matrix[row][column] >= matrix[up[0]][up[1]]:
            self._pacificAtlantic(matrix, up[0], up[1], result, visited, pacific, atlantic, _print)
            pacific[row][column] =  pacific[row][column] or pacific[up[0]][up[1]]
            atlantic[row][column] =  atlantic[row][column] or atlantic[up[0]][up[1]]  
            if _print:
                print("row:{} column:{} up {}:{}".format(row, column, pacific[up[0]][up[1]], atlantic[up[0]][up[1]]))
                
        if down != [-1, -1] and matrix[row][column] >= matrix[down[0]][down[1]]:
            self._pacificAtlantic(matrix, down[0], down[1], result, visited, pacific, atlantic, _print)
            pacific[row][column] =  pacific[row][column] or pacific[down[0]][down[1]]
            atlantic[row][column] =  atlantic[row][column] or atlantic[down[0]][down[1]]
            if _print:
                print("row:{} column:{} down {}:{}".format(row, column, pacific[down[0]][down[1]], atlantic[down[0]][down[1]]))
            
        if left != [-1, -1] and matrix[row][column] >= matrix[left[0]][left[1]]:
            self._pacificAtlantic(matrix, left[0], left[1], result, visited, pacific, atlantic, _print)
            pacific[row][column] =  pacific[row][column] or pacific[left[0]][left[1]]
            atlantic[row][column] =  atlantic[row][column] or atlantic[left[0]][left[1]]
            if _print:    
                print("row:{} column:{} left {}:{}".format(row, column, pacific[left[0]][left[1]], atlantic[left[0]][left[1]]))
            
        if right != [-1, -1] and matrix[row][column] >= matrix[right[0]][right[1]]:
            self._pacificAtlantic(matrix, right[0], right[1], result, visited, pacific, atlantic, _print) 
            pacific[row][column] =  pacific[row][column] or pacific[right[0]][right[1]]
            atlantic[row][column] =  atlantic[row][column] or atlantic[right[0]][right[1]]
            if _print:
                print("row:{} column:{} right {}:{}".format(row, column, pacific[right[0]][right[1]], atlantic[right[0]][right[1]]))
            
        if pacific[row][column] and atlantic[row][column]:
            result.append([row, column])
            
        if _print:    
            print("row:{} column:{} return {}:{}".format(row, column, pacific[row][column], atlantic[row][column])) 
        return pacific[row][column], atlantic[row][column]
    
    # result +ve
    # failed -ve
    
    # iterate every point
        # given point
            # Pacific
                # first row, first column or neighbour is touching pacific <= current
                # if the neighbour is in result and current >= neighboure return true
                # if the neighbour is in failed and current <= neighboure return false
                # if neighbour true return else continue exploring other neighbours
            # Atlantic
                # last row, last column or neighbour is touching atlantic <= current  
                # if the neighbour is in result and current >= neighboure return true
                # if the neighbour is in failed and current <= neighboure return false                
                # if neighbour true return else continue exploring other neighbours
            # both condition met add it to result
