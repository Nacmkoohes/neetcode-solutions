class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            m=l+(r-l)//2
            #why r-1:to not overflow
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        return -1
       

            
