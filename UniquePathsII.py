# [
#   [0,0,0],
#   [0,0,0],
#   [0,0,0]
# ]

# 0:0 -> 2
    #0:1 -> 1
        #1:1 -> 0
        #0:2 -> 1
            #1:2 -> 1
                #1:3 -> 0
                #2:2 -> 1
            #0:3 -> 0
    #1:0 -> 1
        #1:1 -> 0 #
        #2:0 -> 1
            #2:1 -> 1
                #2:2 -> 1 #
                #3:1 -> 0
            #3:0 -> 0

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Initialize eq matrix to keep count of possible paths
        pathGrid = [[-1 for y in range(len(obstacleGrid[0])+1)] for x in range(len(obstacleGrid)+1)]
        #print(pathGrid)
        
        # get possible paths from mn to finish
        return self._paths(obstacleGrid, pathGrid, 0, 0)
        
    def _paths(self, obstacleGrid, pathGrid, x, y):
        
        # check if we have already calc
        if pathGrid[y][x] != -1:
            return pathGrid[y][x]
        
        # y > m or x > n output paths are 0
        if y > len(obstacleGrid)-1 or x > len(obstacleGrid[0])-1:
            pathGrid[y][x] = 0
            return 0

        # if hurdle return 0
        if obstacleGrid[y][x] == 1:
            pathGrid[y][x] = 0
            return 0
        
        # for the finish return 1 possible path
        if y == len(obstacleGrid)-1 and x == len(obstacleGrid[0])-1:
            pathGrid[y][x] = 1
            return 1
                
        # total possible paths = right + bottom possible paths
        right  = self._paths(obstacleGrid, pathGrid, x+1, y)
        bottom = self._paths(obstacleGrid, pathGrid, x, y+1)
        pathGrid[y][x] = right + bottom
        
        return right + bottom
