class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        
        while i < len(tokens):
            print("i:"+str(i)+ " tokens:"+str(tokens))
            if not tokens[i].isnumeric() and tokens[i] != "(" and tokens[i] != ")":
                # Swap digit with operator
                temp = tokens[i-1]
                tokens[i-1] = tokens[i]
                tokens[i] = temp
                print(str(tokens))
                    
                # Inserting closing bracket
                tokens.insert(i+1, ")")
                print(str(tokens))
                    
                # Inserting opening bracket
                j = i-1
                while tokens[j].isnumeric() or tokens[j] == "(":
                    j -= 1
                tokens.insert(j-1, "(")
                print(str(tokens))
                
                # Incrementing because of extra brackets
                i += 2
            i += 1
        print(str(tokens))
        return i
