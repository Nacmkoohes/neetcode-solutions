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
        s_counter=Counter(s)
        t_cunter=Counter(t)
        if s_counter == t_cunter:
            return True
        return False

test=Solution()
print(test.isAnagram(s = "rat", t = "car"))