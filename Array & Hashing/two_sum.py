class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        # seen is a dictionary that for each value -> index
        for i,n in enumerate(nums):
            #enumerate means index and value
            different=target-n
            if different in seen:
                return [seen[different],i]
            else:
                seen[n]=i