class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #key:value
        freq = [[] for i in range(len(nums)+1)] #[1 1 1 1 1]

        for n in nums:
            count[n] = 1+ count.get(n , 0) #n=1 count = {1:1} n=2 {1:1, 2:2}

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

