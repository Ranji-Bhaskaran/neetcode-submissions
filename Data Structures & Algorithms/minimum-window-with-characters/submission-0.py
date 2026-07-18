from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        count = Counter(t)
        req = len(count)

        res = []

        for l in range(len(s)):
            seen = {}
            formed = 0
            for r in range(l, len(s)):
                ch = s[r]
                seen[ch] = 1 + seen.get(ch, 0)
                if count[ch] == seen[ch]:
                    formed += 1

                if formed == req:
                    res.append(s[l:r+1])
                    break

        if not res:
            return ""

        return min(res, key=len)           