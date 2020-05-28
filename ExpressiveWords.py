class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # iterate words one by one
        matching_words = 0
        S_char_count = self.char_counts(S)
        #print("Char Count for {} is {}".format(S, S_char_count))
        
        for word in words:
            stretchy_char_count = list(S_char_count)
            char_count = self.char_counts(word)
            word_matched = True
            #print("Char Count for {} is {}".format(word, char_count))
            
            if len(char_count) != len(stretchy_char_count):
                break
                
            for i in range(len(stretchy_char_count)):
                s_key = next(iter(stretchy_char_count[i]))
                s_count = stretchy_char_count[i][s_key]
                
                key = next(iter(char_count[i]))
                count = char_count[i][key]
                
                #print("Matching S->{}:{} to W->{}:{}".format(s_key, s_count, key, count))
                if s_key == key and (s_count == count or (s_count >= 3 and s_count > count)):
                    pass
                else:
                    word_matched = False
                    break
                    
            if word_matched:
                matching_words += 1
                
        return matching_words
  
    def char_counts(self, word):
        prev_char = None
        count = 0
        char_counts = []
        
        for pos in range(len(word)):
            if prev_char is None:
                prev_char = word[pos]
                count += 1
            else:
                if prev_char == word[pos]:
                    count += 1
                else:
                    char_counts.append({prev_char:count})
                    # Update for next charachter
                    prev_char = word[pos]
                    count = 1
              
            if pos == len(word)-1:
                char_counts.append({prev_char:count})
                
        return char_counts
        # check if each char of the word is present in S
        # h-> "heeellooo"
        # i-> "eeellooo" return not qualify
        
        # remove the char if present and count more occurances
        # count 0 h-> "heeelloooh" -> "eeelloooh" -> count 0 : start from pointer 0 keep looking 
        # for h till you find some other char
        # count 0 e-> "eeellooo" -> count 2 
        # count 0 l-> "llooo" -> "looo" -> count 1 >= 2  it's not stretchy

        # count 0 h-> "heeellooo" -> "eeellooo" -> count 0
        
        # subtract the word char from copy of S
        # In the result("eeoo"), all the char present should be >=3 -> increment counter
        return 0
