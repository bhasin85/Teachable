class Solution:
    def isValid(self, S: str) -> bool:
        S = list(S)
        while len(S) > 0:
            # abc substring exist remove it and keep iterating till all abc are removed
            # in the end nothing should left

            abc_found = False
            for i in range(len(S)):
                #print("i:{} S: {}".format(i,S))
                if i+2<len(S) and S[i] == 'a' and S[i+1] == 'b' and S[i+2] == 'c':
                    # abc found
                    del S[i]
                    del S[i]
                    del S[i]
                    abc_found = True
                    #print("intermediate: {}".format(S))
                    break
                
            if abc_found:
                continue
            else:
                #print("left: {}".format(S))
                return False
            
        return True
