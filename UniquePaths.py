# ["3", "2", "1"]
# ["1", "1", "1"]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pathGrid = [[-1 for x in range(m+1)] for y in range(n+1)] 
        return self._paths(0, 0, m, n, pathGrid, "--")
    
    def _paths(self, y, x, m, n, pathGrid, prefix):
        #print("{}> y:{} x:{}".format(prefix, y, x))

        # check if we have already calc
        if pathGrid[y][x] != -1:
            return pathGrid[y][x]

        # y > m or x > n output paths are 0
        if y > n-1 or x > m-1:
            pathGrid[y][x] = 0
            return 0

        # for the finish return 1 possible path
        if y == n-1 and x == m-1:
            pathGrid[y][x] = 1
            return 1

        # total possible paths = right + bottom possible paths
        right  = self._paths(y, x+1, m, n, pathGrid, prefix)
        bottom = self._paths(y+1, x, m, n, pathGrid, prefix)
        pathGrid[y][x] = right + bottom

        return right + bottom
