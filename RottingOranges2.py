class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 0:
            return -1
        
        fresh_count, rotten_queue = self.adj_list(grid)
        if len(rotten_queue) > 0:
            last_rotten = rotten_queue[-1]
        minutes = 0
        visited = []

        # print("fresh_count:{} last_rotten:{} rotten_queue:{}".format(fresh_count, last_rotten, rotten_queue))
        while rotten_queue:
            rotten = rotten_queue.pop(0)
            #print("rotten:{}".format(rotten))
            
            # find 4 neighbours and append to rotten_queue # and update visited
            y, x = rotten[0], rotten[1]
            
            # up
            if y-1>=0 and grid[y-1][x] == 1:
                grid[y-1][x] = 2
                rotten_queue.append([y-1, x])
                fresh_count -= 1
                
            # left
            if x-1>=0 and grid[y][x-1] == 1:
                grid[y][x-1] = 2
                rotten_queue.append([y, x-1])   
                fresh_count -= 1
                
            # right
            if x+1<len(grid[0]) and grid[y][x+1] == 1:
                grid[y][x+1] = 2
                rotten_queue.append([y, x+1])  
                fresh_count -= 1
                
            # down
            if y+1<len(grid) and grid[y+1][x] == 1:
                grid[y+1][x] = 2
                rotten_queue.append([y+1, x])  
                fresh_count -= 1

            # if last rotton increment minutes
            if rotten == last_rotten:
                if len(rotten_queue) > 0:
                    last_rotten = rotten_queue[-1]
                    minutes += 1
                    # print("Updated last_rotten:{} rotten_queue:{}".format(last_rotten, rotten_queue))
                    
#             print("fresh_count:{} last_rotten:{} rotten_queue:{}".format(fresh_count, last_rotten, rotten_queue))
        
        if fresh_count > 0:
            return -1
        
        return minutes
    
    def adj_list(self, grid):
        fresh_count, rotten_queue = 0, []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    fresh_count += 1
                elif grid[y][x] == 2:
                    rotten_queue.append([y, x])
                
        return fresh_count, rotten_queue
