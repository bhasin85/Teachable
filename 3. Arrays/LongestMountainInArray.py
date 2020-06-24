class Solution:
    def longestMountain(self, A: List[int]) -> int:
        print(len(A))
        longest = 0

        # start from left and keep going till you find peak and than end of mountain
        # update the longest length, if curr_longest > = 3
        # start again till all the entries are traversed

        curr_longest = 0
        peak = False
        for i in range(1, len(A)-1):
            #print("i:{} A[i]:{} peak:{} curr_longest:{}".format(i, A[i], peak, curr_longest))
            
            if A[i-1] < A[i] < A[i+1]:
                # going up
                curr_longest = curr_longest + 1
            elif A[i-1] < A[i] > A[i+1]:
                # peak found
                curr_longest = curr_longest + 1
                peak = True
            elif A[i-1] > A[i] > A[i+1]:
                # going down
                curr_longest = curr_longest + 1
            else:
                # update longest if peak was found
                if peak:
                    curr_longest = curr_longest + 2
                    if curr_longest >= 3:
                        longest = max(longest, curr_longest)
                # reset
                curr_longest = 0
                peak = False  
                
        # update longest if peak was found
        if peak:
            curr_longest = curr_longest + 2
            if curr_longest >= 3:
                longest = max(longest, curr_longest)
                        
        return longest
