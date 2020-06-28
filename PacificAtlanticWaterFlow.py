# maintain visited nodes state in pacificGrid and atlanticGrid
    # -1 -> Not calculated
    #  0 -> flow not possible
    #  1 -> flow possible
# flow check - for pacific and atlantic
        # if x or y is 0 -> can reach pacific
        # if x or y is equal to max x or max y -> can reach atlantic
        # check pacific and atlantic for l,r,u,d if current value is > l,r,u,d value    
        # return pacific and atlantic values
        
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacificGrid = [[-1 for y in range(len(matrix))] for x in range(len(matrix[0]))]
        atlanticGrid= [[-1 for y in range(len(matrix))] for x in range(len(matrix[0]))]
        flow_points = []
        
        #print("pacificGrid :{}".format(pacificGrid))
        #print("atlanticGrid:{}".format(atlanticGrid))
                
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                _print = True #if y == 1 and x == 3 else False
                is_pacific, is_atlantic = self._calc(y, x, pacificGrid, atlanticGrid, matrix, "--", _print)
                print("y:{}, x:{} --> is_pacific:{} is_atlantic:{}".format(y, x, is_pacific, is_atlantic))
                if is_pacific and is_atlantic:
                    flow_points.append([y, x])
                    
                
        return flow_points
        
    def _calc(self, y, x, pacificGrid, atlanticGrid, matrix, prefix, _print):        
        if _print:
            print("{}> y:{}, x:{}".format(prefix, y, x))
            
        # if y < 0 or x < 0 or y > len(matrix)-1 or x > len(matrix[0])-1:
        #     return False, False
        
        # Already calculated
        if pacificGrid[y][x] != -1 and atlanticGrid[y][x] != -1:  
            if _print:
                print("pacificGrid :{}".format(pacificGrid))
                print("atlanticGrid:{}".format(atlanticGrid))                
                print("{}> y:{}, x:{} already calculated".format(prefix, y, x))            
            return True if pacificGrid[y][x] == 1 else False, True if atlanticGrid[y][x] == 1 else False
        
        is_pacific, is_atlantic = False, False
        atlanticGrid[y][x], pacificGrid[y][x] = 0, 0
        
        if y == 0 or x == 0:
            pacificGrid[y][x] = 1
            is_pacific = True
            
        if y == len(matrix)-1 or x == len(matrix[0])-1:
            atlanticGrid[y][x] = 1
            is_atlantic = True
            
        # corner points - no need to calculate further
        if is_pacific and is_atlantic:
            return is_pacific, is_atlantic
        
        # up
        if y-1 >= 0 and pacificGrid[y][x] > pacificGrid[y-1][x]:
            if _print:
                print("{}> y:{}, x:{} Going up".format(prefix, y, x))            
            up_is_pacific, up_is_atlantic = self._calc(y-1, x, pacificGrid, atlanticGrid, matrix, prefix + "--", _print)  
        else: 
            up_is_pacific, up_is_atlantic = False, False
        
        # left
        if y-1 >= 0 and pacificGrid[y][x] > pacificGrid[y-1][x]:
            if _print:
                print("{}> y:{}, x:{} Going left".format(prefix, y, x))              
            left_is_pacific, left_is_atlantic = self._calc(y, x-1, pacificGrid, atlanticGrid, matrix, prefix + "--", _print)  
        else: 
            left_is_pacific, left_is_atlantic = False, False
        
        # down
        if y+1 <= len(matrix)-1 and pacificGrid[y][x] > pacificGrid[y+1][x]:
            if _print:
                print("{}> y:{}, x:{} Going down".format(prefix, y, x))              
            down_is_pacific, down_is_atlantic = self._calc(y+1, x, pacificGrid, atlanticGrid, matrix, prefix + "--", _print)  
        else: 
            down_is_pacific, down_is_atlantic = False, False
        
        # right
        if x+1 <= len(matrix[0])-1 and pacificGrid[y][x] > pacificGrid[y][x+1]:
            if _print:
                print("{}> y:{}, x:{} Going right".format(prefix, y, x))              
            right_is_pacific, right_is_atlantic = self._calc(y, x+1, pacificGrid, atlanticGrid, matrix, prefix + "--", _print)  
        else: 
            right_is_pacific, right_is_atlantic = False, False

        if up_is_pacific or left_is_pacific or down_is_pacific or right_is_pacific:
            if _print:
                print("{}> y:{}, x:{} is pacific".format(prefix, y, x))              
            pacificGrid[y][x] = 1
            is_pacific = True 

        if up_is_atlantic or left_is_atlantic or down_is_atlantic or right_is_atlantic:
            if _print:
                print("{}> y:{}, x:{} is atlantic".format(prefix, y, x))               
            atlanticGrid[y][x] = 1
            is_atlantic = True  

        return is_pacific, is_atlantic
