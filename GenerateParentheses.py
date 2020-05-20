# 1
# '()'

# 2
# '()()'
# '(())'

# 3 

class Solution(object):
    def generateParenthesis(self, N):
        arr = []
        self._generateParenthesis(S='', left=0, right=0, N=N, arr=arr)
        return arr
        
    def _generateParenthesis(self, S, left, right, N, arr):
        if left == right == N:
            arr.append(S)
            return
        
        if left < N:
            self._generateParenthesis(S+"(", left+1, right, N, arr)
        
        if right < left:
            self._generateParenthesis(S+")", left, right+1, N, arr)    
        
