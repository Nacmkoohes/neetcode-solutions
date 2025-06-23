class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,n in enumerate(nums):
# enumerate gives us both index and value
            diff=target-n 
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[n]=i

