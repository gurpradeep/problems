from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged
        
          


sol = Solution()
intervals1 = [[1,3],[2,6],[8,10],[9,18]]
intervals2 = [[1,4],[5,6]]
intervals = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]
print(sol.merge(intervals))