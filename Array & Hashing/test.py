from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=Counter(nums)
        sorted_items=sorted(frequency.items(), key= lambda x:x[1],reverse=True)
        result=[]
        for item in sorted_items[:k]:
            result.append(item[0])
        return result
