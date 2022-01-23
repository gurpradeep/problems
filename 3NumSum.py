from typing import Set


def threeNumberSum2(array, targetSum):
    possibleArr=[]
    array.sort()
    for index  in range(len(array)-2):
        
        if index > 0 and array[index]==array[index-1]:
            continue
        left = index+1
        right = len(array)-1
        while (left < right):
            sum = array[index] + array[left]+array[right]
            if sum== targetSum:
                possibleArr.append((array[index],array[left],array[right]))
                left+=1
                right-=1
            if sum < targetSum:
                left+=1
            if sum > targetSum:
                right-=1
    return possibleArr

def threeSum(array, targetSum):
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(array):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(array[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res

#print(threeNumberSum([12,3,1,2,-6,5,-8,6],0))
print(threeSum([-1,0,1,2,-1,-4],0))
