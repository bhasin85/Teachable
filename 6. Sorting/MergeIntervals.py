# [[3,3],[1,1],[0,2],[2,2],[1,2],[1,3],[1,1],[3,3],[2,3],[4,6]]
# [[1,1],[0,2],[3,3]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals
        
        result = list()
        prev, curr = 0, 1
        again = False
        
        for i in range(len(intervals)):
            if len(result) > 0:
                local_again, overlap_res = self.mergeOverlap(result[-1], intervals[i])
                result = result[:-1] + overlap_res
                
                # Swap detected -> one more sort loop
                if not again and local_again:
                    again = True
            else:
                result = [intervals[i]]
                
        if again:
            return self.merge(result)
        else:
            return result
    
    def mergeOverlap(self, listA, listB):
        # Check overlap
        if listA[0] < listB[0] and listA[0] < listB[1] and listA[1] < listB[0] and listA[1] < listB[1]:
            return False, [listA, listB]
        elif listA[0] > listB[0] and listA[0] > listB[1] and listA[1] > listB[0] and listA[1] > listB[1]:
            return True, [listB, listA]        
        else:
            _min = min(listA[0], listA[1], listB[0], listB[1])
            _max = max(listA[0], listA[1], listB[0], listB[1])
            return True, [[_min, _max]]
        
        
        
