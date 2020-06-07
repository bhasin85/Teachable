class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if len(grid) == 0:
            return -1
        
        fresh, rotten = [], []
        x_limit, y_limit = len(grid) , len(grid[0])
        #print("limit x:{}, y{}".format(x_limit, y_limit))
        for y in range(y_limit):
            for x in range(x_limit):
                print("{}:{}".format(x, y))
                cell = grid[x][y]
                if cell == 1:
                    fresh.append([x, y])
                elif cell == 2:
                    rotten.append([x, y])
                
        minutes = 0
        #print("Playing for fresh:{}     rotten:{}".format(fresh, rotten))
        fresh, new_rotten = self.play(fresh, rotten)
        if len(new_rotten) > 0:
            minutes += 1
            
        #print("Output      fresh:{} new_rotten:{}".format(fresh, new_rotten))
        
        while len(new_rotten) > 0 and len(fresh) > 0:
            rotten = rotten + new_rotten
            #print("Playing for fresh:{}     rotten:{}".format(fresh, rotten))
            fresh, new_rotten = self.play(fresh, new_rotten)
            #print("Output      fresh:{} new_rotten:{}".format(fresh, new_rotten))
            if len(new_rotten) > 0:
                minutes += 1
        
        if len(fresh) > 0:
            return -1
        else:
            return minutes
    
    def play(self, fresh, rotten):
        
        new_rotten = []
        for x, y in rotten:
            # For every rotten, check adj cell
            #print("Checking adj cells for rotten:[{}, {}]".format(x, y))
            adj1, adj2, adj3, adj4 = [x+1, y], [x-1, y], [x, y+1], [x, y-1]

            for cell in [adj1, adj2, adj3, adj4]:
                #print("Adj cell: {}".format(cell))
                if cell in fresh:
                    #print("New rotten found")
                    fresh.remove(cell)
                    new_rotten.append(cell)
              
        #print("New rotten:{}".format(new_rotten))
        return fresh, new_rotten
