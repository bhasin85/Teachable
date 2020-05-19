class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []
        dic_str = dict()
        
        for string in strs:
            sort_string = ''.join(sorted(string))
            #print("sort_string:{}".format(sort_string))
            if sort_string in dic_str:
                l = list(dic_str[sort_string])
                l.append(string)
                #print("l:{}".format(l))
                dic_str[sort_string] = tuple(l)
            else:
                dic_str[sort_string] = tuple([string])
            #print("dict: {}".format(dic_str))
        
        for key in dic_str:
            output.append(list(dic_str[key]))
        
        return output
