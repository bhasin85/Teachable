class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        
        for c in s:
            index = ord(c)-ord('a')
            count[index] += 1
            
        for c in t:
            index = ord(c)-ord('a')
            count[index] -= 1
            
            
        for c in count:
            if c != 0:
                return False
            
        return True
