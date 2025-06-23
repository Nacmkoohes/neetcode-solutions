#using sort and comparing the, 
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s=sorted(s)
#         t=sorted(t)
#         if s==t:
#             return True
#         return False
# o(nlogn)
#using Counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s=Counter(s)
        counter_t=Counter(t)
        if counter_s==counter_t:
            return True
        return False
