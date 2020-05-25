class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        steps = 0
        
        if endWord not in wordList:
            return steps

        queue = [(beginWord, 1)]
        while len(queue) > 0:
            #print('queue:{} wordList:{}'.format(len(queue), len(wordList)))

            #print('queue:{} wordList:{}'.format(queue, wordList))
            entry = queue.pop(0)
            queue_word, length = entry[0], entry[1]       
            #print('queue_word:{}'.format(queue_word)
            
            if queue_word == endWord:
                return length
            
            remove_words = []
            for word in wordList.copy():
                # word similar to beginword -> one letter change
                if self.similar_words(word, queue_word):             
                    queue.append((word, length + 1))
                    # removed the word added to queue from wordList
                    #remove_words.append(word)
                    wordList.remove(word)
                    #print('similar_words {}->{}'.format(queue_word, word))
            
            # for word in self.word_combinations(queue_word):
            #     if word in wordList:
            #         queue.append((word, length + 1))
            #         wordList.remove(word)
                  
            #print('Length queue:{} wordList:{}'.format(len(queue), len(wordList)))
        return steps

    def word_combinations(self, word):
        combinations = set()
        count = 0
        
        while count < len(word):
            for i in range(1,25):
                modified_word = list(word)
                if ord(modified_word[count]) + i > 122:
                    modified_word[count] = chr(ord(modified_word[count]) + i - 26)
                else:
                    modified_word[count] = chr(ord(modified_word[count]) + i)
                combinations.add(''.join(modified_word))
            count += 1
        
        print("word {} combinations {}".format(word, combinations))
        return list(combinations)
    
    def similar_words(self, word1, word2):
        # word similar to beginword -> one letter change
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
