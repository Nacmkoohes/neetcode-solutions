from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        #sort items with the item,frequency from high to low
        sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True) 
        result=[]
        for item in sorted_items[:k]:
            #append the item's name (not the freq) to the result
            result.append(item[0])
        return result

