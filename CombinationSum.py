 # 2, 3, 5 target -> 8
 # 2 -> 2
 #   -> 3 -> 2
 #   ->   -> 3
 #   ->   -> 5
 #   -> 5 -> 2 
 #   ->   -> 3
 #   ->   -> 5

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        return self.com_sum(candidates, target, [], [])
    
    def com_sum(self, candidates, target, inputs, solution):
        if sum(inputs) == target:
            inputs.sort()
            if inputs not in solution:
                solution.append(inputs)
        elif sum(inputs) > target:
            pass
        elif sum(inputs) < target:
            for candidate in candidates:
                self.com_sum(candidates, target, inputs + [candidate], solution)
                
        return solution
