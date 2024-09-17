from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = {}
        s1_counter = Counter(s1.split())
        s2_counter = Counter(s2.split())
        tmp = s1_counter + s2_counter
        for i in tmp.elements():
            if tmp[i] == 1:
                res.update({
                    i: i
                })
        return res

