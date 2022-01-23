from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nLen = len(nums)
        ans_len = 2*nLen
        ans=[]
        index =0
        while index < ans_len:
            if index < nLen:
                ans.append(nums[index])
            else:
                ans.append(nums[index%nLen])
            
            index+=1
        
        return ans
    
    
    
    
sol = Solution()
print(sol.getConcatenation([1,3,2,1]))
