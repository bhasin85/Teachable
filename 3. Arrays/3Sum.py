# i  0
# p1 0
# p2 
# [-4,-1,-1, 0, 1, 2] 6

# [-2,0,1,1,2]
# [-2,]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print("Sorted {}".format(str(nums)))
        
        size = len(nums)
        result = set()
        
        for i in range(size):
            target = nums[i]
            p1 = 0
            p2 = size - 1
            
            #print("Iterating i:{}".format(str(i)))
            while p1 < p2 and p1 != i and p2 != i:
                #print("target:{} p1:{} p2:{}".format(target, nums[p1], nums[p2]))
                if nums[p1]+nums[p2] == target*-1:
                    list_entry = [nums[p1], nums[p2], target]
                    list_entry.sort()
                    
                    entry = tuple(list_entry)
                    result.add(entry)
                    #print("result: {}".format(result))
                    #break
                    p1 += 1
                    p2 -= 1
                elif nums[p1]+nums[p2] > target*-1:
                    p2 -= 1
                else:
                    p1 += 1
                    
        return list(result)
