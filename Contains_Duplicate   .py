#Brute force solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range (i+1, len(nums)):
#                 if nums[i]==nums[j]:
#                     return True
#         return False
# hash set solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
