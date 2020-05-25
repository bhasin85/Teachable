# abc
# a -> b -> c
#   -> c -> b
# b -> a -> c
#   -> c -> a
# c -> a -> b
#   -> b -> a

class Solution:
    def countSubstrings(self, s: str) -> int:
        output = self.palindromic_substrings(s)
        return len(output)
    
    def palindromic_substrings(self, input_string):
        output = []
        visited = set()
        
        # find all possible substings in the input string
        for length in range(len(input_string)):
            for start in range(len(input_string)):
                end = start + length + 1
                if end <= len(input_string):
                    substring = input_string[start:end]
                    key = "{},{}".format(start, end)
                    if key not in visited and self.is_palindrome(substring):
                        output.append(substring)
                        visited.add(key)
                        print("substring:{} key:{} output:{}".format(substring, len(key), len(output)))
        
        # check if the substring is pallindrom -> add it to list
        
        # return the list
        #print("input:{} substrings:{}".format(input_string, output))
        return output
        
    def permutations(self, prefix, suffixs, permutations):
        print("prefix:{} suffixs:{} permutations:{}".format(prefix, suffixs, permutations))
        if len(suffixs) == 0:
            return permutations
        
        for suffix in suffixs:
            sub = "".join(prefix + [suffix])
            is_palindrome = self.is_palindrome(sub)
            #print("{}->{}".format(sub, is_palindrome))
            if is_palindrome and sub not in permutations:
                permutations.append(sub)
            permutations.append(sub)
            suffixes_copy = suffixs.copy()
            suffixes_copy.remove(suffix)
            permutations += self.permutations(prefix+[suffix], suffixes_copy, [])
            
        return list(set(permutations))
        
    def is_palindrome(self, string):
        length = len(string)
        
        if length == 0 or length == 1:
            return True

        if length%2 == 0:
            # even
            return string[:length//2] == string[length//2:]
        else:
            # odd
            return string[:length//2] == string[length//2+1:]
