class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dup = sorted(set(nums))
        print (dup)
        count = 1
        maxi = 1
        i = 0
        n = len(dup)
        for i in range(n-1):
            if dup[i] == dup[i+1] - 1:
                count+=1
                i+=1
            else:
                maxi = max(maxi, count)
                count =1
        return max( maxi, count)   