class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            comple = target - n
            if comple in seen:
                return [seen[comple], i]
            seen[n] = i