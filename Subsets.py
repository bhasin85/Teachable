# [1,2,3,4,5,6,7,8,10,0]

# 1, 2, 3

# i: 0 next_combination: []
  # i: 1 next_combination: []
    # i: 2 next_combination: []
        # i: 3 next_combination: []
        # i: 3 next_combination: [2]    
    # i: 2 next_combination: [2]
  # i: 1 next_combination: [1]
    # i: 2 next_combination: []
    # i: 2 next_combination: [2]



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        length = len(nums)

        def helper(i, next_combination, prefix):
            #next_combination.sort()
            answers.add(tuple(next_combination))
            #print("i: {} next_combination:{} answers:{}".format(i, next_combination, answers))
            #print("{}> i: {} next_combination:{}".format(prefix, i, next_combination))
            
            if i >= length:
                return
            
            helper(i+1, next_combination, prefix + "----")
            helper(i+1, next_combination + [nums[i]], prefix + "----")
                
        helper(0, [], "----")
        return list(answers)
      

        
        
        
    def subsets_rec(self, nums, memo) -> List[List[int]]:
        distinct = [[]]
        if len(nums) == 0:
            return distinct
        
        nums.sort()
        key = ''.join(str(e) for e in nums)
        #print("Looking for key {} in memo {}".format(key, memo))
        if key in memo:
            subsets = memo[key]
            print("Key Found {}->{} nums:{}".format(key, memo[key], nums))
            #return subsets
                
        for i in range(len(nums)):
            sub_nums = nums.copy()
            sub_nums.remove(nums[i])
            #print("nums[i]:{} sub_nums:{}".format(nums[i], sub_nums))
            subsets = self.subsets_rec(sub_nums, memo)
             
            for subset in subsets:
                #print("Appending {} to list {}".format(nums[i], subset))
                subset.append(nums[i])
                #print("Appended {}".format(subset))
                subset.sort()
                
                if subset not in distinct:
                    distinct.append(subset)
                    #print("For {} added {} to {}".format(nums[i], subset, distinct))

        #print("Input:{} Output:{}".format(nums, distinct))
        memo[key] = distinct
        #print("Memo Updated {}".format(memo)) 
        return distinct

        
