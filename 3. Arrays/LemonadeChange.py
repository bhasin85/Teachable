class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        register = {'5': 0,'10': 0, '20': 0}
        
        for i in range(len(bills)):
            
            bill = bills[i]
            change = bill - 5
            
            while change != 0:
                # Change $15 -> Using $10 note
                if change == 15 and register['10']>0:
                    change -= 10
                    register['10'] -= 1
                # Change $5 or $10 or $15 -> Using $5 note
                elif (change == 5 and register['5']>=1) or (change == 10 and register['5']>=2) or (change == 15 and register['5']>=3):
                    change -= 5
                    register['5'] -= 1                    
                else:
                    return False
            
            register[str(bill)] += 1
            
        return True
            
