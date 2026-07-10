from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)

        return list(res.values())
        
        
        
        # for word in strs:
        #     count = [0] * 26

        #     for letter in word:
        #         count[ord(letter) - ord("a")]+=1

        #     res[tuple(count)].append(word)

        # return list(res.values())