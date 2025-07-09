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
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
                       
s = Solution()
print(s.containsDuplicate([1, 2, 3, 4]))       # Should print False
print(s.containsDuplicate([1, 2, 3, 1]))       # Should print True
