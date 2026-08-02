class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            u,v = words[i] , words[i+1]
            minLen = min(len(u), len(v))

            if len(u) > len(v) and u[:minLen] == v[:minLen]:
                return ""

            for j in range(minLen):
                if u[j] != v[j]:
                    adj[u[j]].add(v[j])
                    break

        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
    



