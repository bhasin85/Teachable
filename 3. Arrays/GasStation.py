class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If gas > cost, only then solution exist
        if sum(gas) >= sum(cost):
            start = 0
            tank = 0
            # Iterate the stations and start at 0
            for i in range(len(gas)):
                # Calculate tank at each station
                tank = tank + gas[i] - cost[i]
                #print("i:{} tank:{}".format(i, tank))
                # If tank is negetive, reset tank and start from next station
                if tank < 0:
                    tank = 0
                    start = i + 1
                    #print("resetting i:{} tank:{}".format(i, tank))
            return start
        else:
            return -1
