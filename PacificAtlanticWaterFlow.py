# flow check
    # check for pacific
        # if x or y is 0 -> can reach pacific
        # check pacific for l,r,u,d if current value is > l,r,u,d value
    # check for atlantic
        # if x or y is equal to max x or max y -> can reach atlantic
        # check atlantic for l,r,u,d if current value is > l,r,u,d value    
        
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if len(matrix) == 0:
            return matrix
        pacific_memo, atlantic_memo = {}, {}
        pacific_atlantic = []
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                max_value = matrix[y][x]
                prin = True if y == 2 and x == 1 else False
                print("x:{} y:{}".format(x, y))
                pacific = self._DFS_pacific(y, x, matrix, pacific_memo, max_value, prefix)
                atlantic = self._DFS_atlantic(y, x, matrix, atlantic_memo, max_value, prefix)
                flow = pacific and atlantic
                print("y:{} x:{} flow:{}".format(y, x, flow))
                print("pacific_memo:  {}".format(pacific_memo))
                print("atlantic_memo: {}".format(atlantic_memo))
                if flow:
                    pacific_atlantic.append([y, x])
                    
        return pacific_atlantic
    
    def _DFS_pacific(self, y, x, matrix, pacific_memo, max_value, prefix):
        key = "{}:{}".format(y, x)
        
        if key in pacific_memo and max_value >= matrix[y][x]:
            return pacific_memo[key]
            
        if x == 0 or y == 0:
            pacific_memo[key] = True
            return True

        if y == len(matrix)-1 or x == len(matrix[0])-1:
            pacific_memo[key] = False
            return False
        
        if matrix[y][x] > max_value: 
            pacific_memo[key] = False
            return False
        
        up = self._DFS_pacific(y-1, x, matrix, pacific_memo, max_value, prefix)
        left = self._DFS_pacific(y, x-1, matrix, pacific_memo, max_value, prefix)
        bottom = self._DFS_pacific(y+1, x, matrix, pacific_memo, max_value, prefix)
        right = self._DFS_pacific(y, x+1, matrix, pacific_memo, max_value, prefix)  
        pacific = True if up or left or bottom or right else False
        
        pacific_memo[key] = pacific
        return pacific
    
    def _DFS_atlantic(self, y, x, matrix, atlantic_memo, max_value, prefix):
        key = "{}:{}".format(y, x)
        
        if key in atlantic_memo and max_value >= matrix[y][x]:
            return atlantic_memo[key]
        
        if x == 0 or y == 0:
            atlantic_memo[key] = False
            return False
        
        if y == len(matrix)-1 or x == len(matrix[0])-1:
            atlantic_memo[key] = True
            return True
        
        if matrix[y][x] > max_value: 
            atlantic_memo[key] = False
            return False
        
        up = self._DFS_atlantic(y-1, x, matrix, atlantic_memo, max_value, prefix)
        left = self._DFS_atlantic(y, x-1, matrix, atlantic_memo, max_value, prefix)
        bottom = self._DFS_atlantic(y+1, x, matrix, atlantic_memo, max_value, prefix)
        right = self._DFS_atlantic(y, x+1, matrix, atlantic_memo, max_value, prefix)  
        atlantic = True if up or left or bottom or right else False
        
        atlantic_memo[key] = atlantic
        return atlantic
        
    def _DFS(self, y, x, matrix, memo, max_value, prefix):
        key = "{}:{}".format(y, x)
        
        if key in memo and max_value >= matrix[y][x]:
            return memo[key]
            
        if x == 0 or y == 0:
            pacific_memo[key] = True
            return True

        if y == len(matrix)-1 or x == len(matrix[0])-1:
            pacific_memo[key] = False
            return False
        
        if matrix[y][x] > max_value: 
            pacific_memo[key] = False
            return False
        
        up = self._DFS_pacific(y-1, x, matrix, pacific_memo, max_value, prefix)
        left = self._DFS_pacific(y, x-1, matrix, pacific_memo, max_value, prefix)
        bottom = self._DFS_pacific(y+1, x, matrix, pacific_memo, max_value, prefix)
        right = self._DFS_pacific(y, x+1, matrix, pacific_memo, max_value, prefix)  
        pacific = True if up or left or bottom or right else False
        
        pacific_memo[key] = pacific
        return pacific
