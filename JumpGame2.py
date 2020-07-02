# queue - index:hop
# 1:1, 2:1
#  :2, :2, :2
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0 or length == 1:
            return 0
        
        if nums[0] >= length-1:
            return 1
        
        jump, step, next_steps = 1, nums[0], -1
            
        for i in range(1, length-1):
            #print("i:{}, step:{}, next_steps:{}".format(i, step, next_steps))
            step -= 1
            next_steps = max(next_steps, i + nums[i])                
            if step == 0:
                # jump 
                jump += 1 
                step, next_steps = next_steps-i, -1
                #print("jump:{}".format(jump))
                       
        return jump
 
