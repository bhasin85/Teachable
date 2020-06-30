class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = []
        visited_amounts = set()
        curr_amount, combinations = 0, 0

        for coin in coins:
            new_amount = curr_amount + coin
            new_combinations = combinations + 1

            if new_amount == amount:
                return new_combinations
            elif new_amount < amount and new_amount not in visited_amounts:
                queue.append((new_amount, new_combinations))
                visited_amounts.add(new_amount)
            else:
                # new_amount exceeds the required amount
                continue
                    
        while len(queue)>0:
            entry = queue.pop(0)
            curr_amount, combinations = entry[0], entry[1]
            
            for coin in coins:
                new_amount = curr_amount + coin
                new_combinations = combinations + 1
                
                if new_amount == amount:
                    return new_combinations
                elif new_amount < amount and new_amount not in visited_amounts:
                    queue.append((new_amount, new_combinations))
                    visited_amounts.add(new_amount)
                else:
                    # new_amount exceeds the required amount
                    continue
        return -1
