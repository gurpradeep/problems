from typing import List

def search(nums: List[int], target: int) -> int:
    return searchHelper(nums,target,0,len(nums)-1)

def searchHelper(nums,target,left,right):
    while left <= right:
        mid = (left + right)//2 
        possibleMatch = nums[mid]
        leftNum = nums[left]
        rightNum = nums[right]
        if target==possibleMatch:
            return mid
        elif leftNum <= possibleMatch:
            if target < possibleMatch and target >= leftNum:
                right = mid-1
            else:
                left = mid+1
        else:
            if target > possibleMatch and target <=rightNum:
                left = mid+1
            else:
                right = mid-1
    
    return -1

def searchHelper2(nums,target,left,right):
    if left > right:
        return -1
    mid = (left + right)//2 
    possibleMatch = nums[mid]
    leftNum = nums[left]
    rightNum = nums[right]
    if target==possibleMatch:
        return mid
    elif leftNum <= possibleMatch:
        if target < possibleMatch and target >= leftNum:
            return searchHelper(nums,target,left,mid-1)
        else:
            return searchHelper(nums,target,mid+1,right)
    else:
        if target > possibleMatch and target <=rightNum:
              return searchHelper(nums,target,mid+1,right)
        else:
            return searchHelper(nums,target,left,mid-1)


aList = [4,5,6,7,0,1,2]
print(search(aList,0))