# [[],[1],[100],[3001],[3002]]
# pings [100, 3001, 3002]
# condition 2  1 3002
# counter 1
# [1, 2, 3, 3]
class RecentCounter:

    def __init__(self):
        self.pings = []

    def cleanup_stale_pings(self, stale_pings):
        for stale_ping in stale_pings:
            self.pings.remove(stale_ping)
        
    def ping(self, t: int) -> int:
        counter = 0
        stale_pings = []
        self.pings.append(t)
        
        for ping in self.pings:
            #print("{} <= {} <= {}".format((t-3000), ping, t))
            if (t-3000) <= ping <= t:
                counter += 1
            else:
                stale_pings.append(ping)
                
        self.cleanup_stale_pings(stale_pings)
        return counter
        
        # keep track of all the pings in a list
        
        # for every ping check how many existing are within [t - 3000, t]
        # keep track of stale pings
        
        # clean the stale pings
        # retun the count
                
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
