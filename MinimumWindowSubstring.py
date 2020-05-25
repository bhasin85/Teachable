class Solution:
     def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        min_window = None
        
        while right < len(s) and left < len(s):
            window = s[left:right+1]
            is_desired = True
            for c in t:
                if c not in window:
                    is_desired = False
            
            print("window:{} {}:{} is_desired:{}".format(window, left, right, is_desired))
            if is_desired:
                # update min window
                if min_window is None or len(window) < len(min_window):
                        min_window = window
                        print("min_window {}".format(min_window))
                        
                # move left pointer
                left += 1
            else:
                # move right pointer
                right += 1
            
            
        if min_window:
            return min_window
        else:
            return ""
