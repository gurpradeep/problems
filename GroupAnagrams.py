from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        group_list=[]
        dict_ana = defaultdict(list)
        for uni in strs:
            sortedstr="".join(sorted(uni))
            dict_ana[sortedstr].append(uni)

        for key in dict_ana:
            list_ana = dict_ana[key]
            group_list.append(list_ana)

        return group_list

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()   

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))