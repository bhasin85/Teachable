class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        maximum = 0
        left, right = 0, 0
        
        if len(s) < 1:
            return maximum
        
        while left < len(s) and right < len(s) and left <= right:
            c = s[right]
            
            if c in unique:
                left += 1
                right = left
                unique = set()
            else:
                unique.add(c)
                maximum = max(maximum, len(unique))
                right += 1
            #print("char:{} unique:{} maximum:{}".format(c, str(unique), str(maximum)))
         
        maximum = max(maximum, len(unique))
        return maximum
