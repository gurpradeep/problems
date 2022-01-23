from typing import List
from heapq import heapify,heappop,heappush
class Solution:
    def sortColors2(self, nums: List[int]) -> List[int]:
        heap=[]
        heapify(heap)
        for idx in range(len(nums)):
            heappush(heap,nums[idx])
        
        for idx2 in range(len(nums)):
            nums[idx2]=heappop(heap)
        
        return nums


    def sortColors(self, nums: List[int]) -> List[int]:
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

sol = Solution()
nums =  [2,0,2,1,1,0]
print(sol.sortColors(nums))