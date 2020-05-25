class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s
        
        #print("Input length {} n2:{}".format(len(s), len(s)*len(s)))
        return self.permutation_substring(s)
        
    def permutation_substring(self, string):
        counter = 0
        for length in range(len(string), 0, -1):
            for start in range(len(string)):
                end = start + length
                if end <= len(string):
                    substring = string[start:end]
                    counter += 1
                    if self.is_palindrome(substring):
                        #print("counter {}".format(counter))
                        return substring                  
                    
    def is_palindrome(self, string):
        if len(string)%2 == 1:
            # odd
            mid = len(string)//2
            #reverse = "".join(reversed(string[mid+1:])) 
            reverse = string[mid+1:][::-1]
            #print("Odd {} mid:{} {} == {}".format(string, mid, string[:mid], reverse))
            return string[:mid] == reverse
        else:
            # even
            mid = len(string)//2
            #reverse = "".join(reversed(string[mid:]))
            reverse = string[mid:][::-1]
            #print("Even {} mid:{} {} == {}".format(string, mid, string[:mid], reverse))
            return string[:mid] == reverse           
    
        
