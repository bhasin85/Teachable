class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for i in range(len(gas)):
            j = i
            tank = gas[j]
            count = 0
            #print("i:{} j:{} tank:{}".format(i,j,tank))
            for k in range(len(gas)+1):
                # loop detected
                if j == i:
                    count += 1
                    
                prev_j = j
                if j+1 == len(gas):
                    j = 0
                else:
                    j += 1
                
                # Out of budget
                if tank <= 0 or count == 2 or tank < cost[prev_j]:
                    break
                    
                ff = "{}-{}+{}".format(tank, cost[prev_j], gas[j])
                tank = tank - cost[prev_j] + gas[j]
                #print("loop i:{} j:{} tank {}={}".format(i,j,ff,tank))
                
            if count == 2: 
                return i
            
        return -1
